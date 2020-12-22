from calculadora import soma, subtracao, multiplicacao, divisao

    try:
        valor1 = float(input('Digitar um numero: '))
        valor2 = float(input('Digitar um segundo numero: '))
        resultado = divisao(valor1, valor2)
        print(f"{resultado:.2f}") #__str__
    except ZeroDivisionError as e_z:
        print('Erro de divisao por zero')
    except Exception as e:
        print('Erro qualquer')