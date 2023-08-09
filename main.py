
from classes.Triangle import Triangle
from classes.Rectangle import Rectangle
from classes.Figura import Figura

def count_p(some_object):
    return some_object.tcount_p()

figura = Figura()
triangle = Triangle(1, 2, 3)
rectangle = Rectangle(2, 3)

print(figura.count_p())
print(triangle.count_p())
print(rectangle.count_p())

