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

def batch_convert(path, encod='gbk', override=True):
    try:
        os.chdir(path)
    except: return 1
    dirname=''
    if not override:
        dirname = 'convert/'
        if dirname[:-1] not in os.listdir():
            os.mkdir(dirname)
    # get .md, .txt from current dir
    flist = [f for f in os.listdir() if os.path.splitext(f)[1] in ['.txt', '.md']]
    for each_file in flist:
        encode = detect_encode(each_file)
        if not encode:
            continue
        with open(each_file, encoding=encode) as fin:
            content = fin.read()
        with open(dirname+each_file, 'w', encoding=encod) as fout:
            fout.write(content)
            print('convert', each_file)
    return 0


if __name__ == '__main__':
    keepon =input( "Warning it will override all the txt files, continue?[Y]/N: ")
    if keepon in ['y','Y']:
        enter=True
        while enter:
            path = input('enter the path[./]: ')
            enter = batch_convert( path )
