#assim como nos exemplos abaixo o for tambeḿ pode usar o break e continue
produtos = ["notebook", "mesa", "celular"]

for p in produtos:
    print(f"Produto {p}")

nome = "Erick"
for letra in nome:
    print(letra)

#range(start, stop, step)
#range retorna uma lista de 5 itens, do 0 ao 4
for i in range(5):
    print(i)

#range começando em 5 e terminando em 9
for i in range(5, 10):
    print(i)

#range começando em 0 e terminando em 9, porem pulando de 2 em 2
for i in range(0, 10, 2):
    print(i)
else:
    print('Laço de repeticao terminou sem o ultimo valor 9, pois pulou de 2 em 2')


#laço de repetição while completo
count = 1
while (count <= 10):
    print(count)
    count += 1
print("Laço de repetição concluído")

#laço de repetição while interrompido
count = 1
while (count <= 10):
    print(count)
    if (count == 5):
        break
    count += 1
print(f"Laço de repetição interrompido no {count}")

#pulando um item do laço com continue
count = 1
while (count <= 10):
    if (count == 5):
        count += 1
        continue
    print(count)
    count += 1
print("Laço de repetição pulando o item 5")


#else no while
count = 11
while (count <= 10):
    print(count)
    count += 1
else:
    print("O valor de count é igual ou maior a 10")
