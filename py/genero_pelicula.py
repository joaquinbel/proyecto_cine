class Genero_Pelicula:
    def __init__(self, genero_id, pelicula_id):
        self.__genero_id = genero_id
        self.__pelicula_id = pelicula_id
    def __str__(self):
        return f"Genero Película: {self.__genero_id} - {self.__pelicula_id}"
    @property
    def genero_id(self):
        return self.__genero_id 
    @property
    def pelicula_id(self):
        return self.__pelicula_id 