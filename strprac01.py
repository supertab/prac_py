# format string
# add an '`' when met the first space or \t

f= open('prac01', 'r')
s_tmp=''
def add_symbol(str):
    for i, val in enumerate(str):
        if val in [' ','\t'] and str[i-1]==')':
            pos = i
            break
    return str[:pos]+'`'+str[pos:]

for i in f:
    s_tmp += r'- `' + add_symbol(i)

print(s_tmp)

with open('temp_res','w') as out:
    out.write(s_tmp)
