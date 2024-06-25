class Ocasion_Genero:
    def __init__(self, ocasion_id, genero_id):
        self.__ocasion_id = ocasion_id
        self.__genero_id = genero_id
    def __str__(self):
        return f"Ocasión Genero: {self.__ocasion_id} - {self.__genero_id}"
    @property
    def ocasion_id(self):
        return self.__ocasion_id 
    @property
    def genero_id(self):
        return self.__genero_id 