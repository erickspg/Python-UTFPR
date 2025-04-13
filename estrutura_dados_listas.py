#listas - inserção ordenada por padrao, permite mutablidade e valores duplicados

lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8]
lista_string = ['Charqueadas', 'Imbituba', 'Porto Alegre', 'Floripa']
lista_instancia = list([1, 'Erick', '4', 6])
cidade = 'Imbituba1'

print(lista_string[1])
#print(lista_instancia)

#tipo lista
print(type(lista_instancia))

#tamanho lista
print(len(lista_string))

#curiosidade: obter ultima posicao da lista, ou percorrer pelo final sem tratar tamanho
print(lista_string[-1])
#print(lista_string[-2])

#imprimir um intervalo da lista por sublistas
print(lista_string[2:4])
print(lista_string[:2]) #obter apenas os 2 primeiros itens

#exemplo de 'in_array' do python
if cidade in lista_string:
    print(f'Existe a cidade de {cidade} na lista')
else:
    print(f'Nao existe a cidade {cidade} na lista')

#atribuicao duplia
lista_string[1:3] = ['Sao Jeronimo', 'Butia']
#print(lista_string)

#insercao semelhante ao array_push inserindo elemento no fim da lista
lista_string.append('São Paulo')
#insercao em posicao especifica, empurra os demais
lista_string.insert(1,'Campinas')
#print(lista_string)

#removendo elementos por valor
lista_string.remove('São Paulo')
#removendo ultimo indice
lista_string.pop()
#remove por indice
lista_string.pop(2)
#print(lista_string)

#copiando lista para preservar ordenacao original
lista_string2 = lista_string.copy()

#ordenando a lista com sort por ordem alfabetica
lista_string2.sort()

#mesclar listas semelhante ao array merge
lista_string.extend(lista_numerica)
#print(lista_string)

#contar quantas vezes o elemento aparece na lista
qtd_ch = lista_string.count('Charqueadas')

#limpar lista
lista_string.clear()