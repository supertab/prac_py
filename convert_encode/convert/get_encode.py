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
    return(encod)

if __name__ == '__main__':
    fname = 'new_str.txt'
    print( detect_encode(fname))
