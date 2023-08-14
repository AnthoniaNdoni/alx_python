#!/usr/bin/python3
"""
module documentation
"""
class Base:
    __nb_objects = 0

def __init__(self, id=None):
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects    
    
class Rectangle(Base): 
    """
     Rectangle class that inherits from the Base class.
     Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The unique identifier of the instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): The id for the instance. Defaults to None.
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
             raise ValueError("height must be > 0")
        else:    
            self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:    
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:    
            self.__y = y
        
        @property
        def width(self):
            """ 
            Get the width of the rectangle.
            """
            return self.__width
        
        @width.setter
        def width(self, value):
            """ 
            Set the width of the rectangle.
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

        @property
        def height(self):
            """
            Get the height of the rectangle.
            """
            return self.__height

        @height.setter
        def height(self,  value):
            """
            Set the height of the rectangle.
            """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

        @property
        def x(self):
            """
            Get the x-coordinate of the rectangle.
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            Set the x-coordinate of the rectangle.
            """
            if type(value) is not int:
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

        @property
        def y(self):
            """
            Get the y-coordinate of the rectangle.
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            Set the y-coordinate of the rectangle.
            """
            if type(value) is not int:
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            else: 
                self.__y = value

        def area(self):
            """
            calculate and return the area of the rectangle
            """ 
            return self.width * self.height 

        def display(self):
            """
            Display the rectangle using the '#' character.
            """
            for row in range(self.y):
                print()
            else:
                for row in range(self.height):
                    for column in range(self.width):
                        print(" ",end="")
                else:
                    for column in range(self.width):
                        print("#", end="")
                    else:    
                        print()  

        def __str__(self):
            """
            str update
            """
            return "[Rectangle]({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
        
        def update(self, *args, **kwargs):
            """
            update attributes
            """

            args_length = len(args)
            kwargs_length = len(kwargs)

            for key, value in kwargs.items():
                if key == "id":
                    self.id= value
                elif key == "width":
                 self.width = value
                elif key == "height": 
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value  

                     

            if args_length > 0:
                self.id = args[0]
            if args_length > 1:
                self.width = args[1]
            if args_length > 2:
                self.height = args[2]
            if args_length > 3:
                self.x = args[3]
            if args_length > 4:
                self.y  = args[4]                    