# encoding:utf-8
# 先判断每行是否已经规范化了
def add_symbol(text, head_str, rear_str, **kw):
    str_recon = ''
    for line in text:
        # single line
        new_line = ''
        beg, end= -1, -1
        for idx, char in enumerate(line):
            if char in kw['head']:
                beg = idx+1
                new_line += line[:beg] + head_str
                break
        if len(new_line):
            for idy, char in enumerate(line[beg:]):
                if char in kw['rear']:
                    end = beg + idy +1
                    new_line += line[beg:end] + rear_str + line[end:]
                    break
        if beg!=-1 and end!=-1:
            str_recon += new_line
        else:
            str_recon += line
    return str_recon

if __name__=='__main__':
    with open('./test_str/add_symbol') as txt:
        head_str = ' **'
        rear_str = '** '
        splt = {'head':['-', '*'], 'rear':[':', '：']}
        args = [txt, head_str, rear_str]
        new_str = add_symbol(*args, **splt)

    with open('new_str.txt', 'w') as f:
        f.write(new_str)



