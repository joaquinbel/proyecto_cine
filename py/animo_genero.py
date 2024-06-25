class Animo_Genero:
    def __init__(self, animo_id, genero_id):
        self.__animo_id = animo_id
        self.__genero_id = genero_id
    def __str__(self):
        return f"Ánimo Genero: {self.__animo_id} - {self.__genero_id}"
    @property
    def animo_id(self):
        return self.__animo_id 
    @property
    def genero_id(self):
        return self.__genero_id 