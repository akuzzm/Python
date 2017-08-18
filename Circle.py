class Circle:
    def __init__(self, x, y, r):
      self.x = x
      self.y = y
      self.r = r
      
    def area(self):
       if self.x > 0 and self.y > 0:
         area = self.r * self.r * 3.14
         return area
       else:
            return "Enter correct data!"

    def length(self):
        if self.x > 0 and self.y > 0:
            length = 2 * self.r * 3.14
            return length
        else:
            return "Enter correct data!"

    def __str__(self):
        if self.x > 0 and self.y > 0:
            return "x = {}, y = {}, r = {}, area = {}, length = {}" \
               .format(self.x, self.y, self.r, self.area(),
                       self.length())
        else:
            return "Enter correct data!"
        
if __name__=="__main__":
    
    circle_a=Circle(x=2, y=3, r=5)
    print circle_a
