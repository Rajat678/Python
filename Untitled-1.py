class Area :
    def __init__(self,len,wid,height):
        self.len = len
        self.wid = wid
        self.height = height
        
    def __init__(self,L,B,H):
          self.side1 = L
          self.side2 = B  
          self.side3 = H
          
    def area_rectangle(self):
         a = self.side1*self.side2*self.side3
         print("Area of rectangle is :",a)  
    
    def area_square(self):
        b = self.side1*self.side1
        print("Area of square is: ",b)     
        
class Rectangle (Area):
    
        
            
    