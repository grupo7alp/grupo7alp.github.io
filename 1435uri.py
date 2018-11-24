while True:
    numero = int(input())
    if numero == 0 or numero < 0 or numero > 100:
        break
    principal = []

    for i in range(numero):
        auxiliar = []
        for j in range(numero):
            auxiliar.append(1)
        principal.append(auxiliar)
    valor = 1
    primeira_linha = 0
    primeira_coluna = 0
    ultima_linha = numero - 1
    ultima_coluna = numero - 1

    if numero % 2 == 0:
        meio_matriz = numero / 2
    else:
        meio_matriz = (numero + 1) / 2

    while valor <= meio_matriz:
        i = primeira_coluna
        while i <= ultima_coluna:
            principal[primeira_linha][i] = valor
            principal[ultima_linha][i] = valor
            i = i + 1
            
        i = (primeira_linha + 1)
        
        while i < ultima_linha:
            principal[i][primeira_coluna] = valor
            principal[i][ultima_coluna] = valor
            i+=1

        valor = valor + 1
        primeira_linha = primeira_linha + 1
        ultima_linha = ultima_linha - 1
        primeira_coluna = primeira_coluna + 1
        ultima_coluna = ultima_coluna - 1

    for i in range(numero):
        linha = ''
        for j in range(numero):
            linha = linha + ' %3d' % principal[i][j]
        print(linha[1:])
    print('')
