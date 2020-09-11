def teste_kwargs(**kwargs):
  for key, value in kwargs.items():
    print('{0} = {1}'.format(key, value))
  print('-'*10)

# Passando apenas uma chave
teste_kwargs(nome='fellipe')

# Passando mais de uma chave
teste_kwargs(nome='fellipe', idade=28)

dados = {"nome" : 'fellipe', "idade" : 28}

# TypeError: teste_kwargs() takes 0 positional arguments but 1 was given
#teste_kwargs(dados)
print("imprimindo dados direto: ", dados)

# TypeError: teste_kwargs() takes 0 positional arguments but 2 were given
#teste_kwargs(*dados)
print(*dados)
print("imprimindo dados com um *: ", *dados)

teste_kwargs(**dados)

# O método print não tem um parâmetro nomeado como 'nome'
# TypeError: 'nome' is an invalid keyword argument for print()
#print("imprimindo dados com um *: ", **dados)

# 
print("{nome} -- {idade} ".format(**dados))
