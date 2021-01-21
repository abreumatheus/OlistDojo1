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