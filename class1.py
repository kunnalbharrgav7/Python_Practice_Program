class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 *self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

a=int(input("Enter the radius"))
a1=circle(a)
print(a1.area())
print(a1.circumference())


