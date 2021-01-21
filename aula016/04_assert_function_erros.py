
def soma(n1, n2):
    if isinstance(n1, float) and isinstance(n2, float):
        return n1 + n2
    else:
        raise TypeError('Valores devem ser float')

def divi(n1, n2):
    try:
        return float(n1) / float(n2)            
    except ZeroDivisionError as divi_by_zero:
        raise ZeroDivisionError('n2 nao pode ser zero') from divi_by_zero
    except ValueError as value_error:
        value_error.args = ('valores invalidos, informe um numero inteiro ou ponto flutuante',) 
        raise value_error
    except Exception as error:
        raise error

assert divi(5,5) == 1.0

try:
    divi(5,0)
except Exception as e:
    assert isinstance(e, ZeroDivisionError)

try:
    divi('a',1)
except Exception as e:
    assert isinstance(e, ValueError)
