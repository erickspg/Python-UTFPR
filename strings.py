msg = "Strings em python"
msg2 = " - concatenação usa sintaxe + como no JS."
#print(msg,msg2)
print(msg + msg2)

multiplicador = "vamo inter! " *5
print(multiplicador);

uper = multiplicador.upper()
print(uper)

lower = uper.lower()
print(lower)

print('erick'.capitalize())

teste_find = "Realizando um teste com o metodo find"
posicao = teste_find.find("metodo")
print(f"A palavra 'metodo' se encontra na posição {posicao}")

teste = "10"
print(teste.isnumeric())

msg_fake = 'O gremio é campeão mundial fifa!'
msg_ok = msg_fake.replace('gremio', 'inter')
print(msg_ok)

nome = input('Digite o seu nome:')
print(f"O nome informado foi: {nome}")

#inportante fazer o casting quando for receber int ou float
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso/(altura**2)

print("{} tem {} metros e {} kg. O seu IMC é {}.".format(nome.capitalize(), altura, peso, imc))