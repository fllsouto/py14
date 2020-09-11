def calculadora(x, y):
  return x+y, x-y, x*y, divisao(x,y)

def divisao(x, y):
  if(y == 0):
    return 0
  
  return x/y

def velocidade_media(distancia, tempo):
  velocidade = distancia / tempo
  print(velocidade)
  return velocidade

def velocidade_media2(distancia, tempo):
  velocidade = divisao(distancia, tempo)
  print(velocidade)
  return velocidade


velocidade_media(100, 20)
velocidade_media(150, 22)
velocidade_media(200, 30)
velocidade_media(50, 3)

print(calculadora(10, 13))