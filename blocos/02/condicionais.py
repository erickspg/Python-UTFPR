#exemplo condicional simples, usa identacao ao inves de chaves
idade = int(input('Informe a sua idade: '))

if (idade > 18):
    print('Ja pode tomar uma gelada!')
elif(idade == 18):
    print('18tao ja pode ser preso.')
else:
    print('Vai ter que tomar água.')


print('match case:   1 - Falar com atendente  2 - Duvidas')
opcao = int(input('Escolha uma das opcoes: '))

match opcao:
    case 1:
        print('Falar com atendente')
    case 2:
        print('Duvidas')
    case _:
        'Opcao invalida!'

# exemplo com or para python 3.10+
# https://www.infoworld.com/article/2262867/how-to-use-structural-pattern-matching-in-python.html#:~:text=Using%20Python%20structural%20pattern%20matching,might%20be%20a%20better%20option.
status_code = 400
match status_code:
    case 400 | 401 | 403:
        print('Erro!')
    case 200:
        print('Sucesso!')
    case _:
        print('Codigo de status desconhecido')