def jogar():
  print('****************************************************')
  print('*               Jogo da adivinhação                *')
  print('****************************************************')

  tentativas = {
    1: 20,
    2: 10,
    3: 5
  }

  print("Escolha um nível de dificuldade:")
  print("1 - Fácil (20 tentativas)")
  print("2 - Médio (10 tentativas)")
  print("3 - Difícil (5 tentativas)")

  nivel_dificuldade = int(input("Nível de dificuldade: "))


  numero_secreto = 42
  total_de_tentativas = tentativas.get(nivel_dificuldade, tentativas[2])
  total_de_pontos = 1000

  for rodada in range(1, total_de_tentativas + 1):
    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
    print('Total de pontos: {}'.format(total_de_pontos))
    chute = int(input('Digite o seu chute: '))
    print('Você digitou:', chute)


    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
      print("\nVocê acertou")
      print('Placar final de pontos: {}'.format(total_de_pontos))
      break
    elif (maior):
      print("\nVocê errou! Seu chute foi maior que o número secreto")
    elif (menor):
      print("\nVocê errou! Seu chute foi menor que o número secreto")
    
    total_de_pontos -= abs(numero_secreto - chute)
  