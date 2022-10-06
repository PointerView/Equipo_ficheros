from abc import ABC, abstractmethod



class Persona(ABC):
    
    
    __nombre = ""
    __apellido = ""
    __edad = 0
    
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        
    def viajar(self):
        return "Viajar"
    
    #   SETTERS / GETTERS
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido

    def getEdad(self):
        return self.__edad

    #   METODOS ABSTRACTOS EN CLASE ABSTRACTA


    @abstractmethod
    def partidoFutbol(self):
        pass
    
    @abstractmethod
    def entrenamiento(self):
        pass
    
    
    """ DESTRUCTOR """
    
    
    def __del__(self):
        pass
    
    
 
class Futbolista(Persona):

    __dorsal = 0
    __posicion = ""
    
    def __init__(self, nombre, apellido, edad, dorsal, posicion):
        super().__init__(nombre, apellido, edad)
        self.__dorsal = dorsal
        self.__posicion = posicion
       
    #   SETTERS / GETTERS
       
    def getDorsal(self):
        return self.__dorsal
    
    def getPosicion(self):
        return self.__posicion
    
    #   METODOS VARIOS
    
    def partidoFutbol(self):
        return "Juega el partido de futbol"
        
    def entrenamiento(self):
        return "Entrena"
    
    def entrevista(self):
        return "Recive una entrevista"
        
    def __del__(self):
        pass
    


class Medico(Persona):

    __titulacion = ""
    __excperiencia = 0


    def __init__(self, nombre, apellido, edad, titulacion, experiencia):
        super().__init__(nombre, apellido, edad)
        self.__titulacion = titulacion
        self.__experiencia = experiencia
        
    #   SETTERS / GETTERS  
        
    def getTitulacion(self):
        return self.__titulacion
    
    def getExperiencia(self):
        return self.__excperiencia
        
        
    #   METODOS VARIOS
        
    def partidoFutbol(self):
        return "Da asistencia en el partido de futbol"
        
    def entrenamiento(self):
        return "Da asistencia en el entrenamiento"
        
    def curarLesion(self):
        return "Cura las lesiones a los jugadores"
    
    def __del__(self):
        pass
    
    

class Entrenador(Persona):

    __estrategia = ""
    
    def __init__(self, nombre, apellido, edad, estrategia):
        super().__init__(nombre, apellido, edad)
        self.__estrategia = estrategia
     
        
    #   SETTERS / GETTERS 
    
    def getEstrategia(self):
        return self.__estrategia
        
    #   METODOS VARIOS
        
    def partidoFutbol(self):
        return "Dirige el partido de futbol"
        
    def entrenamiento(self):
        return "Dirige el entrenamiento"
        
    def planificarEntrenamiento(self):
        return "Planifica el entrenamiento"
        
    def __del__(self):
        pass
    
