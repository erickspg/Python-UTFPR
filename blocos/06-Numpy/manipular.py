import numpy as np

#unir arrays
usersFromSource1 = np.array([
    'john@email.com', 'sara@email2.com', 'crist@laznnn.com'
])
usersFromSource2 = np.array([
    'linda@email.com', 'hommer@email2.com', 'muhim@czwwz.com'
])
users = np.concatenate((usersFromSource1, usersFromSource2))
print(users)

#dividir arrays
results = np.array([
    'magazine', 'guidance', 'message', 'recognition', 'office', 'cheek',
    'length', 'stranger', 'trainer', 'ability', 'permission', 'singer',
    'protection', 'manager', 'collection', 'selection', 'effort',
    'promotion', 'village', 'solution'
])

resultsPage = np.array_split(results, 5)
for page in resultsPage:
    print(page)

# buscar em arrays com where
produtos = np.array([
    'salame', 'cerveja', 'queijo', 'salame', 'palmito', 'p~ao de alho'
])

results = np.where(produtos == 'salame')
print(results)

#ordenar array
produtos = np.array(['salame', 'cerveja', 'queijo', 'salame', 'palmito', 'p~ao de alho'])
produtosOrdenados = np.sort(produtos)
print(produtosOrdenados)

# Ordenação de IDs
ids = np.array([1593, 292, 375, 8381, 84111, 558961, 110, 158, 5])
idsOrdenados = np.sort(ids)
print(idsOrdenados)

#filtrar
produtos = np.array(['salame', 'cerveja', 'queijo', 'salame', 'palmito', 'p~ao de alho'])
indexSemSalame = np.where(produtos != 'salame')
print(indexSemSalame)
arraySemSalame = produtos[indexSemSalame]
print(arraySemSalame)