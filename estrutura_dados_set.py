#set - imutavel e nao possui uma coleção ordenada, nao permite valores duplicados/repetidos
#ao usar boleanos e inteiros, nao usar 0 e 1 junto com boolean, pois o set nao permite duplicados e entende como duplicados
meu_conjunto = {2, 3, 'Erick', 'Brenda', 4, True}
meu_conjunto2 = set((1, 2, 3, 'Erick', 'Brenda', 'Marcelo'))

#print(meu_conjunto)

#set nao possui indexacao, unica forma de acessar ou iterar dados é percorrendo, ex:
for dado in meu_conjunto:
    print(dado)

#nao permite alterar valores, mas permite adicionar e remover novos, ex:
meu_conjunto.add('Marcia')
meu_conjunto.remove('Erick') #Lanca erro caso elemento nao existir
meu_conjunto.discard('Erick') #Nao lanca erro caso nao achar elemento, apenas segue o fluxo
print(meu_conjunto)

#unir dois conjuntos/sets
conjunto_geral = meu_conjunto.union(meu_conjunto2)
print(conjunto_geral)

#obter dados que estao nos 2 conjutos:
minha_interseccao = meu_conjunto.intersection(meu_conjunto2);
print(minha_interseccao)

#obter dados que estao exclusivamente em cada conjunto, sem constar no outro
dados_unicos = meu_conjunto.symmetric_difference(meu_conjunto2)
print(dados_unicos)