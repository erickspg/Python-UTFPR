import math
a=5
b=2

#operadores basicos
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#potencia
print(5**2)
print(5**3)

#apenas parte inteira da divisao
print(a//b)
#resto da divisao
print(a%b)

#operadores de atribuicao
a+=5
print(a)
a-=1
print(a)
c = -10.5
print(abs(c))

#retorna valor inteiro + resto em forma de vetor
print(divmod(a,b))

#testando lib math
x = 7.5
#num inteiro
print(math.trunc(x))
#inteiro p baixo
print(math.floor(x))
#inteiro p cima
print(math.ceil(x))
#fatorial
print(math.factorial(int(x)))

#operadores logicos
x = True
y = True

print(x and y)
print(x or y)

x = True
y = False

print(x and y)
print(x or y)


x = False
y = False

print(not x and y)
print(not x or y)

#operadores de comparacao iguais a PHP
# == igual
# != diferente
# > maior
# < menor
# >= maior ou igual
# <= menor ou igual


#operador de filiacao
lista = [1, 2, 3, 4, 5]
valor = 3
print(valor in lista)
print(6 in lista)
print(10 not in lista)