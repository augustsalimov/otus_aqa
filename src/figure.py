class Figure:
    def __init__(self, name, sides):
        self.__name = name
        self.__sides = sides

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Transmitted wrong class")

    def area(self):
        pass

    def sides(self):
        return self.__sides
