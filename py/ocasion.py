class Ocasion:
    def __init__(self, id, descripcion):
        self.__id = id
        self.__descripcion = descripcion
    def __str__(self):
        return f"Ocasión: {self.__descripcion}"
    @property
    def id(self):
        return self.__id 
    @property
    def descripcion(self):
        return self.__descripcion  