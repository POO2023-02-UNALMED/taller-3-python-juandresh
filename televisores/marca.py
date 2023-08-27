class Marca:
    def __init__(self, nombre):
        self._nombre=nombre
    
    #def __init__(self):
    #    self._marca=Marca

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre=nombre