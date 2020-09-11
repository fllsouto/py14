def teste_args(arg, *args):
  print("primeiro argumento normal: {}".format(arg))
  for argumento in args:
    print("outro argumento: {}".format(argumento))
  print('-'*10)

teste_args('python', 'é', 'muito', 'legal')

lista = ['é', 'muito', 'legal']

# Vai imprimir a lista como sendo um parâmetro simples
teste_args('python', lista)

# Vai imprimir as listas como sendo parâmetros simples
teste_args('python', lista, lista)


teste_args('python', *lista)

tupla = ['é', 'muito', 'legal']

teste_args('python', tupla)

teste_args('python', *tupla)

