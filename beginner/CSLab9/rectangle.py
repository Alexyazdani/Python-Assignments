class Rectangle:
    """
    One object of class Rectangle stores one
    rectangle's length and width.
    """

    def setData(self, newHeight, newWidth):
        """
        sets the data inside the Rectangle to newHeight by newWidth
        """
        self.height = newHeight
        self.width = newWidth

    def __str__(self):
        """
        returns a string containing the data in the Rectangle
        """
        return "height = %i, width = %i" % (self.height, self.width)
    
    def area(self):
        return (self.height*self.width)

"""
   Since the following code is not indented, it is not part of the
   class Rectangle. This code is used for testing objects of class
   Rectangle. This code creates two Rectangle objects and calls
   methods on them for testing purposes. We call this the test program.
"""
r1 = Rectangle()
r1.setData(3,4)
print('Rectangle r1: ',r1)   # automatically calls __str__(self) method and prints the returned value
r2 = Rectangle()
r2.setData(5,6)
print('Rectangle r2: ',r2)   # automatically calls __str__(self)
area1=r1.area()
area2=r2.area()
print(area1, area2)