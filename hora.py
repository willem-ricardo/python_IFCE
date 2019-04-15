class Hora:
    ### Construtor
    def __init__(self, h = 0, m = 0, s = 0):
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            self.__hora = h
            self.__minuto = m
            self.__segundo = s
        else:
            self.__hora = 0
            self.__minuto = 0
            self.__segundo = 0
        
    def set_hora(self, hora):
        if 0 <= hora <= 24:
            self.__hora = hora
            
    def set_minuto(self, minuto):
        if 0 <= minuto <= 59:
            self.__minuto = minuto
            
    def set_segundo(self, segundo):
        if 0 <= segundo <= 59:
            self.__segundo = segundo
        
    def mostre_hora(self):
        return "{:02d}:{:02d}:{:02d}".format(self.__hora, self.__minuto, self.__segundo)
        