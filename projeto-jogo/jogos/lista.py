lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
primeiroElemento = lista[0]
ocorrenciasPrimeiroElemento = 0
media = 0
somaNegativos = 0
for index in range(0, len(lista)):
    if(maiorValor < lista[index]):
        maiorValor = lista[index]

    if(menorValor > lista[index]):
        menorValor = lista[index]

    if(lista[index] % 2 == 0):
        listaPares.append(lista[index])

    if(lista[index] == primeiroElemento):
        ocorrenciasPrimeiroElemento += 1

    if(lista[index] < 0):
        somaNegativos += lista[index]

    media += lista[index]

media = media/len(lista)

print(maiorValor)
print(menorValor)
print(listaPares)
print("Ocorrencias do primeiro elemento: ", ocorrenciasPrimeiroElemento)
print("Media dos valores: ", media)
print("Soma dos valores negativos: ", somaNegativos)