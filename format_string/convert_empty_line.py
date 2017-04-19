#!/usr/bin/python3
# encoding:utf-8

def select_file(*args):
    import os
    suffix=['.cc', '.py', '.txt', '.md']
    if len(args): suffix.extend(args)
    flist = [f for f in os.listdir('./') if os.path.splitext(f)[1] in suffix] 
    files = ''.join([ str(idx+1) + ' ' + f + '\n' for (idx, f) in enumerate(flist)])
    fidx = input('%s选择文件(输入数字)：'%files)
    if fidx.isdigit() and 0<int(fidx)<=len(flist):
        return flist[int(fidx)-1]

def detect_encode(fname):
    # enter file name, at current dir
    # return file's encode 
    import os
    if fname not in os.listdir():
        print( 'file not find... ')
        return False
    codebook = ['utf-8', 'gbk', 'gb2312' ]
    for encod in codebook:
        f = open(fname, encoding=encod)
        try:
            f.readline()
        except:
            f.close()
            if encod == codebook[-1]:
                print('unknow encode...')
                return False
            continue
        f.seek(0)
        break
    f.close()
    return encod

fname = select_file()
fencode = detect_encode(fname)
symbol = input("输入用来代替空行的符号: ") + '\n' 

with open(fname, encoding=fencode) as f:
    context = ''
    for line in f:
        line = symbol if line.strip() == '' else line
        context += line

with open(fname+'.txt', 'w', encoding=fencode) as f:
    f.write(context)



