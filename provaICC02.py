def nFatorial(num:int):
    fat = 1
    for i in range(1,num+1):
        fat = fat*i
    aux = fat
    while aux%10 == 0:
        aux = aux//10
        r = aux%10
    print(f'{num}! = {fat} ------- {r}')


teste = [i for i in range(11,20,3)]

for j in teste:
    nFatorial(j)
