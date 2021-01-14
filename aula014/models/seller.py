class Seller:
    def __init__(self, name:str, phone:str, email:str, id:int=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email