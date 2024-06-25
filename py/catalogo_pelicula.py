class Catalogo_Pelicula:
    def __init__(self, catalogo_id, pelicula_id):
        self.__catalogo_id = catalogo_id
        self.__pelicula_id = pelicula_id
    def __str__(self):
        return f"Catálogo Película: {self.__catalogo_id} - {self.__pelicula_id}"
    @property
    def catalogo_id(self):
        return self.__catalogo_id 
    @property
    def pelicula_id(self):
        return self.__pelicula_id 