from televisores.tv import TV

class Control:
    def __init__(self):
        self._tv=TV 

    def enlazar(self, TV):
        self._tv=TV
        TV.setControl(self)


    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canalN):
        if (TV._estado and canalN>=1 and canalN<=120):
            self._tv.setCanal(canalN)

    def setVolumen(self, volumenN):
        if (TV._estado and volumenN>=0 and volumenN<=7):
            self._tv.setVolumen(volumenN)

    def setTv(self, TV):
        self._tv=TV

    def getTv(self):
        return self._tv