import os
def detect_encode(fname):
    # enter file name, at current dir
    # return file's encode 
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
    return(encod)

def batch_convert():
    # get .md, .txt from current dir
    dirname = 'convert'
    if dirname not in os.listdir():
        os.mkdir(dirname+'/')
    flist = [f for f in os.listdir() if os.path.splitext(f)[1] in ['.txt', '.md']]
    for each_file in flist:
        encode = detect_encode(each_file)
        if not encode:
            continue
        with open(each_file, encoding=encode) as fin:
            with open(dirname+'/'+each_file, 'w') as fout:
                fout.write(fin.read())
                print('convert', each_file)


if __name__ == '__main__':
    batch_convert()
