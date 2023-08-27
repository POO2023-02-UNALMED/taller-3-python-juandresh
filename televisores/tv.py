class TV:
    def _init__(self,marca, canal, precio, estado, volumen, control):
        self._marca=marca
        self._canal=canal
        self._precio=precio
        self._estado=estado
        self._volumen=volumen
        self._control=control

    def _init__(self):
        self._canal=1
        self._volumen=1
        self._precio=500
    
    numTV=0

    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca=marca

    def getCanal(self):
        return self._canal
    def setCanal(self, canal):
        self._canal=canal

    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._nombre=precio

    def getVolumen(self):
        return self._volumen
    def setVolumen(self, volumen):
        self._volumen=volumen

    def getControl(self):
        return self._control
    def setControl(self, control):
        self._control=control

    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False

    def getEstado(self):
        return self._estad
    
    def canalUp(self):
        if(self._estado and self._canal<120):
            self._canal += 1
    def canalDown(self):
        if(self._estado and self._canal>1):
            self._canal -= 1

    def volumenUp(self):
        if(self._estado and self._volumen<7):
            self._volumen += 1 

    def volumenDown(self):
        if(self._estado and self._volumen>0):
            self._volumen -= 1