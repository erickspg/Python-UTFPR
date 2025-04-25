#manipulação de arquivos com metodos nativos em python
#modos de acesso
# 'r' -> leitura de arquivo, se não existir o arquivo retornará ume erro
# 'a' -> insere mais conteúdo no arquivo e caso não exista ele cria novo arquuivo
# 'w -> abre arquivo para escrita, se não existir ele cria
# 'x' -> cria um arquivo especifico e retorna um erro caso ja exista

#tipo do arquivo
# 't' -> padrao texto
# 'b' -> binario para imagens, videos etc

#exemplos
arquivo = open('meuArquivo.txt') #por defaul igual a open('meuArquivo.txt', 'rt')
texto_arquivo = arquivo.read()
print(texto_arquivo)
arquivo.close()

#ler arquivos de outros diretórios
#arquivo2 = open('../03/arquivo.txt')
#print(arquivo2.read())

#ler linha por linha
arquivo = open('meuArquivo.txt')
linha1 = arquivo.readline()
print(linha1)
# for linha in arquivo:
#     print(linha)
arquivo.close()


#adição de conteudo
arquivo = open('meuArquivo2.txt', 'a')
arquivo.write('\nInserindo uma nova linha de conteudo no meu arquivo')
arquivo.close()


#inserindo conteudo mas removendo tudo que existia nele anteriormente
arquivo = open('meuArquivo.txt', 'w')
arquivo.write('Criando um novo conteudo para o arquivo')
arquivo.write('\nEsse é um exemplo de manipulação de arquivos.')
arquivo.close()

#excluir um arquivo utilizando a lib os
import os
if (os.path.exists('meuArquivo2.txt')):
    os.remove('meuArquivo2.txt')
else:
    print('Arquivo nao existe')

#excluir um diretorio vazio
if (os.path.exists('../00')):
    os.rmdir('../00') #apenas pasta vazia
else:
    os.mkdir('../00')

#excluir um diretorio com todo seu conteudo
import shutil
shutil.rmtree('../00')