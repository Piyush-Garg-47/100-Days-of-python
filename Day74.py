class Shape:
  def __init__(self , x , y):
     self.x = x 
     self.y = y 
  def area(self):
     return self.x * self.y 
  
class circle(Shape):
   def __init__(self , radius):
      super().__init__(radius,radius) 
      self.radius = radius
      def area(self):
         return 3.14 * super().area() 
  
rec = Shape(3,4)
print(rec.area())

c = circle(5)
print(c.area())