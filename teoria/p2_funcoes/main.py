from calculadora import soma

valor1 = input('Digitar um numero: ')
valor2 = input('Digitar um segundo numero: ')
resultado = soma(valor1, valor2)
print(f"{resultado:.2f}") #__str__