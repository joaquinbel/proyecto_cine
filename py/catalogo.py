class Catalogo:
    __peliculas = []
    def __init__(self, id, titulo, descripcion):
        self.__id = id
        self.__titulo = titulo
        self.__descripcion = descripcion
    def __str__(self):
        return f"Titulo: {self.__titulo} - Descripción: {self.__descripcion}"
    def Agregar_Pelicula(self, unaPelicula):
        self.__peliculas.append(unaPelicula)
    def Eliminar_Pelicula(self, unaPelicula):
        self.__peliculas.remove(unaPelicula)
    def Devolver_Peliculas(self):
        return self.__peliculas
    @property
    def id(self):
        return self.__id 
    @property
    def titulo(self):
        return self.__titulo   
    @property
    def descripcion(self):
        return self.__descripcion  
# p1 = Pelicula(1, 'locos adams', 'la serie', 1965, 30)
#  c1 = Catalogo(3, 'mi catalogo', 'esta muy bueno')
# c1.Agregar_Pelicula(p1)
# p2 = c1.Devolver_Peliculas()
# c1.Eliminar_Pelicula(p1)
