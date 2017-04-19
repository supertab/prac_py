#!/usr/bin/python3
# encoding:utf-8

def select_file(*args):
    import os
    suffix=['.cc', '.txt', '.md']
    if len(args): suffix.extend(args)
    flist = [f for f in os.listdir('./') if os.path.splitext(f)[1] in suffix] 
    files = ''.join([ str(idx+1) + ' ' + f + '\n' for (idx, f) in enumerate(flist)])
    fidx = input('%s选择文件(输入数字)：'%files)
    if fidx.isdigit() and 0<int(fidx)<=len(flist):
        return flist[int(fidx)-1]

print(select_file('.py'))
