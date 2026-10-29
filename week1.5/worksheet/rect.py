# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if isinstance(width, int) == False or isinstance(height, int) == False:
            raise TypeError
        elif width <= 0 or height <= 0:
            raise ValueError
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(height, width):
        """Return whether the rectangle is a square"""
        if height == width:
            return True
        else:
            return False

    def area(height, width):
        """Return the area of the rectangle"""
        return height * width

    def perimeter(height, width):
        """Return the perimeter of the rectangle"""
        return (2 * height) + (2 * width)