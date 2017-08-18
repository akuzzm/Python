class Circle:
    def __init__(self, x, y, r):
      self.x = x
      self.y = y
      self.r = r
      
    def area(self):
       if self.x > 0 and self.y > 0:
            return "area =", self.r * self.r * 3.14
       else:
            return "Enter correct data!"

    def length(self):
        if self.x > 0 and self.y > 0:
            return "length =", 2 * self.r * 3.14
        else:
            return "Enter correct data!"

    def __str__(self):
        if self.x > 0 and self.y > 0:
            return "x = {}, y = {}, r = {}, area = {}, length = {}" \
               .format(self.x, self.y, self.r, self.r * self.r * 3.14,
                       2 * self.r * 3.14)
        else:
            return "Enter correct data!"
