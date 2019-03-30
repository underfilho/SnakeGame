class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Iguala os valores de um vetor a um outro
    def set(self, vector):
        self.x = vector.x
        self.y = vector.y

    # Soma um vetor com outro
    def plus(self, vector):
        self.x += vector.x
        self.y += vector.y

    # Verifica se um vetor é igual ao outro
    def equal(self, vector):
        return self.x == vector.x and self.y == vector.y
