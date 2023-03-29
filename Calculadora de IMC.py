print("CALCULADORA DE IMC")
print("Insira seu peso: (em kg)")
peso = float(input())
print("Insira sua altura: (em metros)")
altura = float(input())
IMC = peso / (altura**2)
print("Seu IMC é de {}.".format(IMC))

if IMC < 18.5:
    print("Você está abaixo do peso.")
if IMC > 18.5 and IMC < 24.9:
    print("Você está em um peso normal.")
if IMC > 25 and IMC < 29.9:
    print("Você está com sobrepeso.")
if IMC > 30 and IMC < 34.9:
    print("Você está com Obesidade grau I.")
if IMC > 35 and IMC < 39.9:
    print("Você está com Obesidade grau II.")
else:
    print("Você está com Obesidade grau III (obesidade mórbida)")
