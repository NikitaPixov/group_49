class unit:
    def __init__(self,sm,mm):
        self.sm = sm
        self.mm = mm


class Figure(unit):
    def calculate_area(self,):
        raise NotImplementedError("This method should be overridden in subclasses")

    def info(self):
        raise NotImplementedError("This method should be overridden in subclasses")


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}cm, area: {area}cm²")


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.length}cm, width: {self.width}cm, area: {area}cm²")

shapes = [
    Square(4),
    Square(5),
    Rectangle(3, 6),
    Rectangle(2, 8),
    Rectangle(5, 5)
]
for shape in shapes:
    print(shape.info())