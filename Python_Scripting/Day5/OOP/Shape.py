import math


class Point:

    def __init__(self, x=0, y=0): #constructor method
        self.x = x
        self.y = y


    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


    def __str__(self):
        return f'({self.x!r}, {self.y!r})'
        


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius


    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)


    def area(self):
        return math.pi * (self.radius ** 2)


    def circumference(self):
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        #return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)
        return f'Circle({self.radius!r}, {self.x!r}, {self.y!r})'


    def __str__(self):
        return repr(self)
        

if __name__ == "__main__":
    a = Point()
    print(a)
    b = Point(3,4)
    print(b)
    print(f'Representation form of a: {repr(a)}')
    print(f'Print form of b: {str(b)}')
    print(f'Distance from origin : {b.distance_from_origin()}')
    b.x = -19
    print(f'Print form of b: {str(b)}')
    print(a == b, a != b)



