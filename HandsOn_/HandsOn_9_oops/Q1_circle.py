import math

class Circle:
    # Default constructor
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    # Getter for radius   
    def get_radius(self):
        return self.radius

    # Setter for radius
    def set_radius(self, radius):
        self.radius = radius

    # Getter for color
    def get_color(self):
        return self.color

    # Setter for color
    def set_color(self, color):
        self.color = color

    # Method to calculate area
    def get_area(self):
        return math.pi * self.radius ** 2

    # toString equivalent
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"


# Driver code to test
if __name__ == "__main__":
    # Using default constructor
    c1 = Circle()
    print(c1)  # Circle[radius=1.0, color=red]
    print("Area:", c1.get_area())

    # Using constructor with radius
    c2 = Circle(2.5)
    print(c2)  # Circle[radius=2.5, color=red]
    print("Area:", c2.get_area())

    # Using constructor with radius and color
    c3 = Circle(3.0, "blue")
    print(c3)  # Circle[radius=3.0, color=blue]
    print("Area:", c3.get_area())

    # Testing setters
    c3.set_radius(4.0)
    c3.set_color("green")
    print(c3)  # Circle[radius=4.0, color=green]
    print("Area:", c3.get_area())
