# вычисление дискриминанта квадратного уравнения (ax^2 + bx + c = 0)
import math


def solve(a, b, c):
    D = b * b - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return {'x1': x1, 'x2': x2}
    if D == 0:
        x = -b / (2 * a)
        return {'x': x}
    if D < 0:
        return {}

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

print('Result: ', solve(a, b, c))
