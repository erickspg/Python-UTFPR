import numpy as np

#tipos dados
# i - integer (inteiro)
# ? - boolean (booleano)
# u - unsigned integer (inteiro sem sinal)
# f - float (ponto flutuante)
# c - complex float (número complexo)
# m - timedelta (diferença de tempo)
# M - datetime (data e hora)
# O - object (objeto Python)
# S - string (texto em bytes, ex: b'string')

cores = np.array(['Fernando', 'Julia', 'Silmara', 'Jason'])
print(cores.dtype)

pesos = np.array([56.2, 64.1, 90.2, 20.8, 47.1])
print(pesos)
print(pesos.dtype)

pesos2 = pesos.astype('i')
print(pesos2)
print(pesos2.dtype)

alturas = np.array([1.88, 1.95, 1.64, 1.65, 1.72])
novaAlturas = alturas[0:2].copy()
print(novaAlturas)

precosPorCategoria = np . array ([[10.50 , 9.54 , 1.08 , 7.98] , [3.69 , 5.49 , 6.39 , 4.20]])
print(precosPorCategoria.shape)

#matriz -> funciona apenas com divisoes exatas
numeros = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12])
matriz = numeros.reshape(4 , 3).copy()
print(matriz)

#IMPORTANTE: Se nao usar o copy ele tratara atribuicoes de arrays sempre como visao
# de forma que alterar o array 'copiado'ira alterar tambem o original
# Para nao alterar o array original é necessário usar o COPY