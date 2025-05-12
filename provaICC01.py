def conversao(bina):
    return sum([int(bina[i])*2**(len(bina)-i-1) for i in range(len(bina))])


teste = ['00011011','00001001','11001100','00110001']

for j in teste:
    print(f'{j} ~= {conversao(j)}')