# calculo do IMC
#
altura = input('qual a sua altura ?')
peso = input('qual o seu peso?')
total = float(peso)/float(altura)
if(total <= 18.4):
  print('imc invalido')
elif(total >= 18.5 and total <= 24.9):
  print('normal')
elif(total >= 25.0 and total <= 29.9):
  print('sobrepeso')
else:
 print('obsidade')
 print(total)
  
 //edição teste
