def raizExata(n):
    for i in range(2,n//2):
        if n == i**2:
            return True
    
    return False

def listaRaiz(numeros):
    return [i for i in numeros if raizExata(i)]


import random

numeros = [random.randint(2,200) for i in range(20)]

resposta = listaRaiz(numeros)

print(numeros)
print(resposta)
print()