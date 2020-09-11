def dados(nome, idade=None):
  print('-'*10)
  print('nome: {}'.format(nome))
  if(idade is not None):
    print('idade: {}'.format(idade))
  else:
    print('idade não informada')

def dados2(nome=None, idade=None):
  print('-'*10)
  if(nome is not None):
    print('nome: {}'.format(nome))
  else:
    print('nome não informada')

  if(idade is not None):
    print('idade: {}'.format(idade))
  else:
    print('idade não informada')

# Passando os dois parâmetros
dados('Fellipe', 28)

# Passando apenas um parâmetro
dados('Fellipe')

# Passando um parâmetro nomeado e o outro normal
# SyntaxError: positional argument follows keyword argument
#dados(nome='Fellipe', 10)

# Passando os dois parâmetros nomeados em ordem
dados(nome='Fellipe', idade=28)

# Passando os dois parâmetros fora de ordem
dados(idade=28, nome='Fellipe xpto')

# Passando um parâmetro nomeado
# TypeError: dados() missing 1 required positional argument: 'nome'
#dados(idade=28)

# Passando os dois parâmetros fora de ordem
dados2(idade=28, nome='Fellipe')

#Passando os dois parâmetros fora de ordem e não nomeado
dados2(28, 'Fellipe')

