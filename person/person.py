
class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
#
    def imc(self):
        return self.weight / (self.height**2)
#
    def sample(self, a, b):
        print(self,a,b)
