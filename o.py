from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(width):
        pass

class Circle(Shape):
    def get_area(width):
        print (3.14 * width**2)

class Square(Shape):
    def get_area(width, height):
        print(height * width)

class Triangle(Shape):
    def get_area(width, height):
        print((height*width)/2)

def main():
    square = Square
    square.get_area(5, 10)
    triangle = Triangle
    triangle.get_area(6, 20)
    circle = Circle
    circle.get_area(3)

if __name__ == "__main__":
    main()