nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome em minúsculas é: {}.'.format(nome.lower()))
print('O seu nome tem {} caracteres sem contar espaços.'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem {} letras.'.format(nome.find(' ')))
novo = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(novo[0], len(novo[0])))