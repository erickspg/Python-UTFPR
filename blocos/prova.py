import math
import numpy as np
#print(math.trunc(9.8))
#print(math.ceil(5.6))
#print(math.factorial(6))
#print(math.floor(5.6))
#print(abs(-185.2))
#print(int(1.6))
#print(divmod(3,2))


entrada = (1, 3, 5, 9, 12, 14, 16, 18, 19, 20, 21)

impares = 0
pares = 0

for n in entrada:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

#print(f'Pares: {pares}')
#print(f'Ímpares: {impares}')


# Implementar a função validaSenha abaixo:
def validaSenha(password):
    if len(password) < 5 or len(password) > 15:
        return False
    
    cont_numeros = 0
    cont_maiusculas = 0

    for x in password:
        if x.isdigit():
            cont_numeros += 1
        elif x.isupper():
            cont_maiusculas += 1

    if cont_numeros >= 2 and cont_maiusculas >= 2:
        return True
    else:
        return False
    
    

#Não alterar o código abaixo
myPass = input()

if (validaSenha(myPass)):
    print("Senha válida")
else:
    print("Senha inválida")



# Implemente uma função retorne os valores das chaves de um dicionário em uma lista
def DictToList(dict):
    valores = list()


    for v in dict:
        valores.append(dict.get(v))
    return valores

faturamento = {
    "01/01/2023": 5500,
    "02/01/2023": 8850,
    "03/01/2023": 10500,
    "04/01/2023": 6000,
    "05/01/2023": 4500,
    "06/01/2023": 11000,
    "07/01/2023": 1260
}

lista_faturamento = DictToList(faturamento)

# Imprima a soma dos valores contidos em lista_faturamento usando uma função de soma do NumPy
print(np.sum(lista_faturamento))