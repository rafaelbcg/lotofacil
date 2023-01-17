import requests
concurso = input(f'informe o concurso que deseja acessar: ')

req = requests.get(f'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/{concurso}',verify=False)
# a variável lotofacil conterá  uma série de informações
lotofacil = req.json()
dezenas = lotofacil['listaDezenas']

jogos = open('jogos.txt','r')
apostas = jogos.readlines()
pontos11 = 0
pontos12 = 0
pontos13 = 0
pontos14 = 0
pontos15 = 0
jogos.close()
print(f'para concurso {concurso} foi sorteados os numeros: {dezenas}')
for i in apostas:
    pontos = 0
    for d in dezenas:
        if d in i:
            pontos += 1
    match pontos:
        case 11:
            pontos11 +=1
        case 12:
            pontos12 +=1
        case 13:
            pontos13 += 1
        case 14:
            pontos14 += 1
        case 15:
            pontos15 += 1
    print(f'o jogo {i} fez {pontos} pontos')

print(f'jogos com 11 pontos {pontos11}')
print(f'jogos com 12 pontos {pontos12}')
print(f'jogos com 13 pontos {pontos13}')
print(f'jogos com 14 pontos {pontos14}')
print(f'jogos com 15 pontos {pontos15}')



