# soma, sub, mult, div
def soma(numero1:float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2) :   
        resultado = numero1 + numero2
        return resultado

def subtracao(numero1:float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2) :   
        resultado = numero1 - numero2
        return resultado

def multiplicacao(numero1:float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2) :   
        resultado = numero1 * numero2
        return resultado

def divisao(numero1:float, numero2:float)->float:
    try:
        if valida_float(numero1) and valida_float(numero2) :   
            resultado = numero1 / numero2
            return resultado
    except ZeroDivisionError as e_zero:
        raise e_zero

def valida_float(numero:float)->bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f'Valor informado {numero} não é float')


