#tupla - semelhante a uma lista constante, pois é imutavel, tbm permite itens duplicados e nao permite insercao ou remocao
minha_tupla = (1 , 2, 3, 'Erick', 'Imbituba', 4, 'Charqueadas')
minha_tupla2 = ('Marcia', 5)

#erro:
#minha_tupla[0] = 50

#declarar variaveis contendo os valores da tupla
(v1, v2, v3, v4, v5, v6, v7) = minha_tupla
print(v4)

#percorrendo tupla, normal
for dado in minha_tupla:
    print(dado)

#concatenar ou mesclar tuplas
tupla_completa = minha_tupla + minha_tupla2
print(tupla_completa)

#duplicar tupla
tupla_multiplicada = minha_tupla2 * 3
print(tupla_multiplicada)

#validar qual index esta o valor
print(minha_tupla.index('Erick'))

#quantidade de valores na tupla
print(tupla_multiplicada.count('Marcia'))

#demais funcoes vistas em listas que nao alteram valores do array da tupla podem ser usadas com tupla