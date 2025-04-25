#Funcoes
def calcular_valores(a, b = 2):
    soma = a+b
    print(f'A soma de {a} mais {b} é {soma}')

calcular_valores(3)

#funcao com numero de params indefinidos / lista
def somar_lados(*lados):
    soma = 0 #obrigatorio -> 'UnboundLocalError: local variable 'soma' referenced before assignment'
    for lado in lados:        
        soma += lado
    return soma

print(somar_lados(1,2,4))

#funcao chamando parametros desordenadamente
def printProdutos(p3, p2, p1):
    print(f'O valor do parametro p3 é: {p3}')

printProdutos(p1 = 'Alface', p2 = 'Brocolis', p3 = 'Tomate')

#retornar multiplos valores em python
def calcular_dados(numero):
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2
    return (dobro, triplo, quadrado)

d, t, q = calcular_dados(5)
print("Dobro:", d)
print("Triplo:", t)
print("quadrado:", q)

#funcao lambda é uma pequena funcao anonim que pode ter varios argumetos mas apenas 1 expressao
calcular_area_quadrado = lambda lado : lado * lado
print(calcular_area_quadrado(2))

#exemplo aula, calcular media de uma lista de valores numericos
def getValues():
    lista = []
    valor = 0

    while valor!='*':
        valor = input("Digite um valor numerico ou '*' para para de inserir valores: ")
        if valor == '*':
            break
        lista.append(float(valor))

    return lista

def calcular_media(numeros):
    total = 0
    soma = 0
    for numero in numeros:
        soma += numero
        total += 1
    
    return (soma/total)

media = calcular_media(getValues())
print(f'A media dos valores é: {media}')
print('A media dos valores é: {}'.format(media))

#IMC questao 5 - questionario
n = input()
p = float(input())
a = float(input())

def computeIMC(n, p, a):
    if n is None or p is None or a is None:
        return "Não foi possível calcular o IMC."
    imc = (p / (a * a))
    return f"{n} tem {p} kg e {a:.2f} metros de altura. O seu IMC é {imc:.2f}"

print(computeIMC(n, p, a))

#code soma questao 6 - questionario
def computeSum(*valores):
    soma = 0
    for valor in valores:
        soma += valor
    
    if soma > 0:
        return soma
    else:
        return "Nenhum valor recebido."
    

print(computeSum(10.0, 20.0, 30.0))
#print(computeSum(5.0, 25.2))
#print(computeSum(6.3, 50.3, 0, 29.4, 1205))
#print(computeSum(5.1))
print(computeSum())