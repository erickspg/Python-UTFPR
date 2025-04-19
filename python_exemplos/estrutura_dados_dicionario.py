#dicionarios armazen no formato chave:valor (json?) , elementos ordenados e mutáveis, não permite elementos duplicados
#declaracao:
meu_dicionario = {
    'Nome': 'Erick',
    'Idade': 29,
    'Esportes': ['Futebol', 'Surf', 'Tênis']
}

print(meu_dicionario)

#tamanho de um dicionario:
print(len(meu_dicionario))

#acessando itens do dicionario por indice:
print(meu_dicionario['Nome'])
print(meu_dicionario.get('Nome'))

#obter todas as chaves do dicionario:
print(meu_dicionario.keys())

#obter todos as valores do dicionario:
print(meu_dicionario.values())

#validar se o indice/chave existe
if 'Nome' in meu_dicionario:
    print('Existe a chave Nome no dicionario')

#alterar valores de um dicionario
meu_dicionario['Nome'] = 'Brenda'
meu_dicionario.update({
    'Nome' : 'Brenda',
    'Idade' : 26
})

#adicionar novos itens no dicionario
meu_dicionario['Sexo'] = 'Masculino'
meu_dicionario.update({
    'Sexo' : 'Feminino'
})

#remover item do dicionario
meu_dicionario.pop('Esportes')
#remover ultima chave dicionario
meu_dicionario.popitem()

#iterar sobre os elementos de um dicionario
for item in meu_dicionario:
    print(meu_dicionario[item])

#copiar dicionario para outra variavel
meu_dicionario2 = meu_dicionario.copy()

#aninhamento de dicionarios
outro_dicionario = {
    'Pessoa1' : {
        'Nome': 'Marcia',
        'Idade': 60,
        'Esportes': ['Netflix']
    },
    'Pessoa2' : {
        'Nome': 'Nicole',
        'Idade': 28,
        'Esportes': ['Academia']
    }
}

print(outro_dicionario['Pessoa2']['Esportes'])