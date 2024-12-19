class ClienteOB:
    def __init__(self, nombre, apellido, cedula, edad, imgDocumento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__edad = edad
        self.__imgDocumento = imgDocumento

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, value):
        self.__cedula = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        if value >= 0:
            self.__edad = value
        else:
            raise ValueError("La edad no puede ser negativa")

    @property
    def imgDocumento(self):
        return self.__imgDocumento

    @imgDocumento.setter
    def imgDocumento(self, value):
        self.__imgDocumento = value
