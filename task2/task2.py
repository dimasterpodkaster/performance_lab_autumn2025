from decimal import Decimal
import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1, 'r') as file_ellipse:
    lines = file_ellipse.readlines()
    x_center, y_center = map(Decimal, lines[0].split())
    x_radius, y_radius = map(Decimal, lines[1].split())


def ellipse_equation(x, x_center, x_radius, y, y_center, y_radius):
    return (x - x_center) ** 2 / x_radius ** 2 + (y - y_center) ** 2 / y_radius ** 2


eps = Decimal('1e-30')
with open(filename2, 'r') as file_points:
    lines = file_points.readlines()
    for line in lines:
        x1, y1 = map(Decimal, line.split())
        result = ellipse_equation(x1, x_center, x_radius, y1, x_center, y_radius)
        if 1 - eps <= result <= 1 + eps:
            print(0)
        elif result < 1 - eps:
            print(1)
        else:
            print(2)
