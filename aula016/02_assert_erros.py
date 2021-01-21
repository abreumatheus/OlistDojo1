# Nos exemplos a seguir o assert é utilizado em expressões falsas 
# portanto o código não será executado completamente, parando no primeiro erro (AssertionError)
# para verificar a execução de cada linha, comente as demais

assert False
assert 10 == 10.1
assert 10 is 10.0
assert isinstance(numero, float)
assert type(numero) == float
nome = 'Josué Ávila'
assert nome == 'josué avila'
assert 'j' in nome
# A string colocada logo após a vírgula é atribuida a mensagem de erro
# caso a expressão retorne False e assim o assert gere uma exceção
assert 'evila' in nome, 'Nao existe'
