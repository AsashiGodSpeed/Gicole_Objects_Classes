import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * self.radius ** 2
        print(f"Area of the circle is: {circle_area:.2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle is: {circle_perimeter:.2f}")


radius = float(input("Enter the radius of the circle: "))
my_shape = Circle(radius)

my_shape.area()
my_shape.perimeter()