# Com assert podemos testar as classes e seus métodos 
# podendo verificar objetos da classe e 
# o resultado de seus comportamentos

class Product:
    def __init__(self, name:str, price:float)->None:
        self.name = name
        self.price = price

    @property
    def name(self)->str:
        return self.__name
    @property
    def price(self)->float:
        return self.__price

    @name.setter
    def name(self, name:str)->None:
        self.__name = name

    @price.setter
    def price(self, price:float)->None:
        try:
            self.__price = float(price)
        except ValueError as e:
            raise ValueError('O valor nao pode ser convertido para float') from e
    
nome = 'Comp'
preco = 2000
prod1 = Product(nome, preco)

# testando se o objeto da classe é do tipo esperado e assim tentando o construtor
assert type(prod1) == Product
assert isinstance(prod1, Product)

# testando o get e o set de name
assert prod1.name == nome 
assert type(nome) == type(prod1.name)
assert prod1.name is nome

# testando o get e o set de price
assert prod1.price == preco 
assert isinstance(prod1.price, float)

# testando se a exceção é gerada pelo setter do price
preco = 'R$2000'
try:
    prod1.price = preco
except Exception as e:
    assert isinstance(e, ValueError)
    
