print('****************************************************')
print('*               Jogo da adivinhação                *')
print('****************************************************')

numero_secreto = 42

chute = int(input('Digite o seu chute: '))
print('Você digitou:', chute)


acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
  print('Você acertou')
elif (maior):
  print('Você errou! Seu chute foi maior que o número secreto')
elif (menor):
  print('Você errou! Seu chute foi menor que o número secreto')