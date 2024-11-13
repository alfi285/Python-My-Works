# 3. Module with a Class
# --Create a module named shapes.py that defines a class Rectangle
# with methods to calculate the area and perimeter.
# The class should take length and width as parameters.
# In another file main.py, create an instance of Rectangle
# and print the area and perimeter.

class Rectangle:
    def area(self,length,breath):
        return length*breath

    def perimeter(self,length,breadth):
        return 2*(length+breadth)