class Category:
    def __init__(self, name:str, description:str, id:int = None)->None:
        self.id = id
        self.name = name
        self.description = description