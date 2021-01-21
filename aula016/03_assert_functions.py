# Com assert podemos testar funções 
# verificando se estão sendo executadas corretamente

def soma(n1, n2):
    return n1 + n2

def subt(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divi(n1, n2):
    return n1 / n2

assert soma(10, 20) == 30
assert soma('maicon ', 'granemam')  == 'maicon granemam'
assert subt(10, 20) == -10
assert mult(5, 20) == 100
assert divi(10, 5) == 2