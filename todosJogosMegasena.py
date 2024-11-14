import requests

reqs = requests.get("https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/",verify=False)

ultimo = reqs.json()
ultimoSorteio = ultimo["numero"]

reqs.close()

numeros = list()
for i in range(60):
    numeros.append(0)

for i in range(1,ultimoSorteio+1):
    try:
        reqs2 = requests.get(f'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/{i}',verify=False)
    except requests.exceptions.Timeout:
        print('Acabou tempo, e tentar de novo')
        reqs2 = requests.get(f'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/{i}',verify=False)
    megaSena = reqs2.json()
    numerosSorteados = megaSena["listaDezenas"]
    print(f'{i} >> {numerosSorteados}')
    for j in numerosSorteados:
        numeros[int(j)-1] += 1
    reqs2.close()

resultados = []

for l in range(60):
    t = (l+1,numeros[l])
    resultados.append(t)

try:
    file = open("resultado.txt","w")
except FileExistsError:
    file = open("resultado.txt","x")

ordenado = sorted(resultados,key=lambda x:x[1])[::-1]
for k in range(60):
    m = ordenado[k]
    text = f'{k} --- {m[0]} --- {m[1]} --- {100*m[1]/ultimoSorteio}%'
    print(text)
    file.write(text+"\n")
    if k == 14:
        file.write("\n")
        file.write("----------------------------------------")
        file.write("\n")

file.close()

