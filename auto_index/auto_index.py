import os
from get_encode import *

def add_num(fname, sp=' '):
    # add number
    encode = detect_encode(fname)
    if not encode:
        print('unknow encode...')
        return False
    with open(fname, encoding=encode) as f:
        strlist0 =[]
        i = 1
        for s in f:
            tmps = s.strip()
            if len( tmps) > 1:
                n = str(i)
                strlist0.append( n+sp+tmps+'\n')
                i += 1
    res=''
    res = res.join(strlist0)
    # print(res.join(strlist0))
    with open('addNum_'+fname, 'w', encoding=encode) as f:
        f.write(res)
    input('已经添加序号，保存为：addNum_%s'%fname)


def remove_num(fname, sp=' '):
    encode = detect_encode(fname)
    if not encode:
        print('unknow encode...')
        return False
# remove identifier
    with open(fname, encoding=encode) as f:
        strlist = []
        for s in f:
            tmps=''
            s = s.strip()
            # find first space
            s = s[s.find(sp)+1:]
            strlist.append(s+'\n')
    str1 = ''.join(strlist)
    with open('removNum_'+fname, 'w', encoding=encode) as f:
        f.write(str1)
    input('已经移除序号，保存为：removNum_%s'%fname)


if __name__=='__main__':
    func = [0, add_num, remove_num]
    while True:
        ch = input('输入：1-添加序号，2-移除序号：')
        if ch in ['1','2']:
            # 只留下 txt
            flist = [f for f in os.listdir() if os.path.splitext(f)[1]=='.txt'] 
            files = ''.join([ str(idx+1) + ' ' + f + '\n' for (idx, f) in \
                              enumerate(flist)])
            fidx = input('%s选择文件(输入数字)：'%files)
            if fidx.isdigit() and 0<int(fidx)<=len(flist):
                # call function
                func[int(ch)](flist[int(fidx)-1])
                break
            else:
                print('文件不存在\n')
            


