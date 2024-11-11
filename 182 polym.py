# OOPS TASK
#
# 1-Simple Python program with POLYMORPHISM?
import math

from select import select

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of rectangle:",self.length * self.breadth)

    def perimeter(self):
        print("Perimeter of rectangle:",2*(self.length+self.breadth))

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of circle:",math.pi*self.radius*self.radius)

    def perimeter(self):
        print("Perimeter of circle:",2*math.pi*self.radius)

rect1 = Rectangle(5,10)
rect1.area()
rect1.perimeter()

c1 = Circle(5)
c1.area()
c1.perimeter()


