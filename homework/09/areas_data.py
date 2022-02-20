from math import pi 

def square_area(a):
    area = a**2
    return ['Square', area]


def rectangle_area(a, b):
    area = a*b
    return ['rectangle', area]


def circle_area(radius):
    area = pi * radius**2
    return ['circle', area]


def triangle_area(base, height):
    area = 0.5 * base * height
    return ['triangle', area]


if __name__ == '__main__':
    print(square_area(5))
    print(rectangle_area(5, 7))
    print(circle_area(3))