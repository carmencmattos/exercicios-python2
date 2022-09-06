""" Escreva uma classe “Quadrado”, crie dois métodos que retornem a área do quadrado e o perímetro, não crie a instância nesse exercício. """
# Área do quadrado = lado ** 2  /  Perímetro do quadrado = lado * 4

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def area_quadrado(self):
        return (f"A área do quadrado é igual a {self.lado**2}")
    
    def perimetro_quadrado(self):    
        return (f"O perímetro do quadrado é igual a {self.lado*4} ")
    

        