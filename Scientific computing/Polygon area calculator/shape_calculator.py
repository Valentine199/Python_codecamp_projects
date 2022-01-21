#from _typeshed import Self


class Rectangle:
    width = 0
    height = 0

    def __init__(self, Width, Height):
        self.width  = Width
        self.height = Height
    
    def __str__(self) :
        return "Rectangle(width={}, height={})".format(self.width, self.height) 
    
    def set_width(self, newWidth):
        self.width = newWidth
    
    def set_height(self, newHeight):
        self.height = newHeight

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if(self.width > 50 or self.height>50):
            return "Too big for picture."
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print("*", end="")
                print()
    
    def get_amount_inside(self, shape):
        return self.get_area() // shape.getarea()
    

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side={})".format(self.width)
    
    def set_height(self, newHeight):
        self.height = newHeight
        self.width = newHeight
    
    def set_width(self, newWidth):
        self.height = newWidth
        self.width = newWidth
    
    def set_side(self, side):
        self.width = side
        self.height = side
    

