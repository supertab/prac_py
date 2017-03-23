#混淆：密钥字母后面接一个明文字母，之后随机插入0-3个字符再出现下一个密钥明文对
#1.密钥串的循环 2.排除密钥字母 3插入混淆字符
#tip:morsecode yourname MIGI+泉新一
#映射 morse code: 字母间以空格分隔，//[]单词间以/分隔
#已解决morse码中含有回车问题


#bugger:
#1.end char err
#2.do not random the end char always same
import random
#from encryption_gui import * 

#key = "dsf"
#msg = "iloveyou"#如何处理空格
#print("msg:%s"%(msg))

#encryption
#step 1: mix
def encrypt(msg, key="dsf"):
    #去除空格回车
    msg = [ x for x in msg if x not in [' ','\n'] ]
    if not len(msg):
        return "请先输入文字..."
    #判断明文
    if msg[0] in '.-':
        return "请按解密按钮哦~"
    #生成不包括key的字母字表
    alpha = "abcdefghijklmnopqrstuvwxyz"
    encryt_table = [x for x in alpha if x not in key ]

    randmsg = ""
    pos=0
    msg_len = len(msg)
    while True:
        for c in key:
            #disturb_char_count = random.randint(0, 3)#插入3个随机字符
            #for i in range(disturb_char_count):
            #列表中随机选3个
            randmsg += ''.join( random.sample(encryt_table, random.randint(0, 3)))
            randmsg += c
            randmsg += msg[pos]
            pos += 1
            if pos == msg_len:
                break
        if pos == msg_len:
            break
    ##print( "randmsg:%s"%(randmsg) )

#step 2: reflect morse code
    alpha = "abcdefghijklmnopqrstuvwxyz"
    pot = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
           "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
           "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
           "-.--", "--.."]

    #generate morse dictionary 
    morse_table = {}
    for c in alpha:
        morse_table[c] = pot[ alpha.index(c)]

    morse_code = ""
    for c in randmsg:
        morse_code += morse_table[c]
        morse_code += ' '#最后会多一个空格
    #print("morse_code:%s"%(morse_code))
    return morse_code

#crack
def crack( morse_code, key="dsf" ):
    morse_code = morse_code.replace('\n',' ')#去除\n
    if len(morse_code)==0:
        return "请先输入文字..."
    if morse_code[0] not in '.-':
        return "请按加密按钮哦~"
    morse_code += ' '
    #demorse code
    alpha = "abcdefghijklmnopqrstuvwxyz"
    pot = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
           "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
           "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
           "-.--", "--.."]
    #generate morse dictionary
    morse_table_reverse = {}
    for c in pot:
        morse_table_reverse[c] = alpha[ pot.index(c)]

    morse_table_reverse[''] = ''
    randmsg = ""
    temp = ""
    for c in morse_code:
        #按空格合并,处理最后一个字符
        if c != ' ':
            temp += c
            continue
        else:
            randmsg += morse_table_reverse[temp]
            temp = ""
        
    #print("randmsg:%s"%(randmsg))

    #acquire msg
    msg = ""
    index = 0
    randmsg_len = len(randmsg)
    while True:
        if randmsg[index] in key:
            #逻辑：找到一个后从下个开始防止 ddx 的情况
            msg += randmsg[index+1]#index是从头索引
            index += 1
        index += 1
        if index >= randmsg_len:
            break
    #print("msg:%s"%(msg))
    return msg

def save_info(msg, cipher):
    f=open("record.txt", mode='w')
    f.write(msg+'\n'+cipher)
    f.close()
    return "保存成功~"

if __name__ == "__main__":
    morse_code = encrypt( msg )
    crack( morse_code )   

#print( random.randint(0, 3) )
