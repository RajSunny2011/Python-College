import math

class Shape:
    def __init__(self):
        self.details = {}

    def print_details(self):
        for key, value in self.details.items():
            print(f"{key}: {value}")

class Triangle(Shape):
    def __init__(self, A, B, C):
        super().__init__()
        self.details = {"Side A": A, "Side B": B, "Side C": C}

    def area(self):
        S = (self.details["Side A"] + self.details["Side B"] + self.details["Side C"]) / 2
        return math.sqrt(S * (S - self.details["Side A"]) * (S - self.details["Side B"]) * (S - self.details["Side C"]))

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.details = {"Length": length, "Width": width}

    def area(self):
        return self.details["Length"] * self.details["Width"]

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.details = {"Side": side}

    def area(self):
        return self.details["Side"] ** 2

class Cuboid(Shape):
    def __init__(self, length, width, height):
        super().__init__()
        self.details = {"Length": length, "Width": width, "Height": height}

    def area(self):
        return self.details["Length"] * self.details["Width"] * self.details["Height"]

class Cube(Shape):
    def __init__(self, side):
        super().__init__()
        self.details = {"Side": side}
    
    def area(self):
        return self.details["Side"] ** 3

class Cone(Shape):
    def __init__(self, radius, height):
        super().__init__()
        self.details = {"Radius": radius, "Height": height}

    def area(self):
        return (1/3) * math.pi * (self.details["Radius"] ** 2) * self.details["Height"]

class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__()
        self.details = {"Radius": radius, "Height": height}

    def area(self):
        return math.pi * (self.details["Radius"] ** 2) * self.details["Height"]

class Sphere(Shape):
    def __init__(self, radius):
        super().__init__()
        self.details = {"Radius": radius}

    def area(self):
        return (4/3) * math.pi * self.details["Radius"] ** 3

def create_shape():
    shape_type = input("Enter shape type:\n1. Triangle\n2. Rectangle\n3. Square\n4. Cuboid\n5. Cube\n6. Cone\n7. Cylinder\n8. Sphere\nEnter: ")
    if shape_type == "1":
        A = float(input("Enter side A: "))
        B = float(input("Enter side B: "))
        C = float(input("Enter side C: "))
        return Triangle(A, B, C)
    elif shape_type == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        return Rectangle(length, width)
    elif shape_type == "3":
        side = float(input("Enter side length: "))
        return Square(side)
    elif shape_type == "4":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        return Cuboid(length, width, height)
    elif shape_type == "5":
        side = float(input("Enter side length: "))
        return Cube(side)
    elif shape_type == "6":
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        return Cone(radius, height)
    elif shape_type == "7":
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        return Cylinder(radius, height)
    elif shape_type == "8":
        radius = float(input("Enter radius: "))
        return Sphere(radius)
    else:
        return None

while True:
    shape = create_shape()
    shape.print_details()
    print("Area/Volume:", shape.area())
    if input("Do you want to continue? (y/n): ").lower() != "y":
        break
    