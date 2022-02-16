from turtle import circle


class Figure:
    name = ''
    S = float()

    


class Square(Figure):

    def __init__(self, name, side):
        self.name = name
        self.side = int(side)
    
    def find_S_sq(self):
        self.S = self.side**2
        return f'S = {self.S}'


    def info_sq(self):
        return f'Figure name is {self.name}, its S is {self.S}'


class Circle(Figure):

    def __init__(self, name, r):
        self.name = name
        self.r = r

    def find_S_crcl(self):
        π = 3.14
        self.S = π*(self.r**2)
        return f'S = {self.S}'

    def info_crcl(self):
        return f'Figure name is {self.name}, its S is {self.S}'




sq1 = Square('Square', 2)
sq1.find_S_sq()
print(sq1.info_sq())

crcl1 = Circle('Circle', 3)

print(crcl1.find_S_crcl())

figures = [sq1, crcl1]
suma = 0
for i in figures:
    suma += i.S

print(suma)