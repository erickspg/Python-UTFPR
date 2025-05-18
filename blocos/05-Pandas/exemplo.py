import pandas

dados = {
    'cliente' : ["Jonas", 'Erick', 'Brenda'],
    'idade' : [10, 29, 26]
}

df = pandas.DataFrame(dados)

#imprimir apenas primeira e segunda linha do data frime
print(df.loc[0])

#imprimir todo dataframe
print(df)

#Exemplos aula
#https://colab.research.google.com/drive/1HxspDYITQjQJ-OrIAVaWheRcJnMWIcRb