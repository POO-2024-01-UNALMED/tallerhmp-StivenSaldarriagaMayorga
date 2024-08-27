from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, anosPracticando, deporte="Futbol"):
        super().__init__(nombre, edad, altura, sexo)
        self.__deporte = deporte
        self.__anosPracticando = anosPracticando

    ##getters
    def getDeporte(self):
        return self.__deporte

    def getAnosPracticando(self):
        return self.__anosPracticando

    #setters
    def setDeporte(self, deporte):
        self.__deporte = deporte

    def setAñosPracticando(self, anosPracticando):
        self.__anosPracticando = anosPracticando