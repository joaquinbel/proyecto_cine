class Pelicula:
    def __init__(self, id, titulo, descripcion, anio, duracion):
        self.__id = id
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__anio = anio
        self.__duracion = duracion
    def __str__(self):
        return f"Película: {self.__titulo} - {self.__descripcion}"
    @property
    def id(self):
        return self.__id 
    @property
    def titulo(self):
        return self.__titulo   
    @property
    def descripcion(self):
        return self.__descripcion      
    @property
    def anio(self):
        return self.__anio    
    @property
    def duracion(self):
        return self.__duracion  
    