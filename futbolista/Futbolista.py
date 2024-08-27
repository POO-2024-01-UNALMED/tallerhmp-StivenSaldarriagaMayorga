from deportista import Deportista

class Futbolista(Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, golesMarcados, tarjetasRojas, piernaHabil, anosPracticando):
        super().__init__(self, nombre, edad, altura, sexo, anosPracticando) 
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    #getters
    def getGolesMarcados(self):
        return self.__golesMarcados

    def getTarjetasRojas(self):
        return self.__tarjetasRojas

    def getPiernaHabil(self):
        return self.__piernaHabil

    #setters
    def setGolesMarcados(self, golesMarcados):
        self.__golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self.__tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self.__piernaHabil = piernaHabil

    # Método __str__ para imprimir la información del futbolista
    def __str__(self):
        return (f"Mi nombre es {self.getNombre()} soy profesional en el deporte "
                f"{self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo "
                f"{self.getAnosPracticando()} años en el deporte")