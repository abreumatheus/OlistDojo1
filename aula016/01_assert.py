# Testes unitários utilizando assert sem uso de Framework

# Palavra reservada assert serve para testar uma condição 
# caso a condição seja falsa é gerado uma exceção do tipo AssertionError

# Nos exemplos a seguir o assert é utilizado em expressões verdadeiras 
# portanto o codigo será executado com sucesso.

assert True
assert 10 == 10.0
n1 = 10
n2 = 10
assert n1 is n2
assert id(n1) == id(n2)
numero : float = 10
assert isinstance(numero, int)
assert type(numero) == int
nome = 'Josué Ávila'
assert nome == 'Josué Ávila'
assert 'Josué' in nome
assert 'Josu' in nome
assert ' ' in nome
