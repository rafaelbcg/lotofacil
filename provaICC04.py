def ehPrimo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

inicio = int(input('inicio: '))
fim = int(input('fim: '))

i = fim
while i >= inicio and not ehPrimo(i):
    i-= 1
if ehPrimo(i):
    print(f'{i} eh o  maior numero primo do intervalo')
else:
    print(f'o intervalo {inicio} a {fim} não tem numero primo')
