# Types of Polymorphism
# 1 - Method Overloading -   Compile Time Polymorphism
# 2 - Method Overriding -   Runtime Polymorphism

# Method Overloading - Same function with differenct signatures
# Method Overriding - Same function with similar signature 

# Method Overloading - Don't need inheritance
# Method Overriding - Inheritance is required

# Method Overloading - User don't need more than one class
# Method Overriding - User need more than one class

# Example of Method Overloading

# class Calculation:
#     def calc(self, x=None, y=None):
#         if (x==None and y==None):
#             print("I am Method Overloading")
#         elif x!=None and y==None:
#             fact = 1
#             for i in range(1, x+1):
#                 fact = fact * i
#             print("Factorial is:",fact)
#         else:
#             print("Addition is",x+y)

# calc_obj = Calculation()
# calc_obj.calc()
# calc_obj.calc(5)
# calc_obj.calc(5,6)

# Example of Method Overriding
class A:
    def wish(self):
        print("Hello! Good Morning")

class B(A):
    def wish(self):
        print("Hello! Good Evening")

objB = B()
objB.wish()