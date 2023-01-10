# Polymorphism - Same function with different signatures

# print()
# print(3)
# print(4,5)
# print("This is number")
# print("This is number",45)
# print(len("python"))
# print(len([23,34,45,67,78,89]))

# Example of user-define polymorphism function

# def func(a=0,b=0,c=0):
#     print("addition is:",a+b+c)
# func()
# func(4)
# func(4,5)
# func(4,5,6)

# Polymorphism with class
# class developer:
#     def salary(self):
#         print("My salary is 45000")
    
#     def location(self):
#         print("My location is noida")
    
#     def leaves(self):
#         print("My pending leaves are 30")

# class programmer:
#     def salary(self):
#         print("My salary is 34000")
    
#     def location(self):
#         print("My location is pune")
    
#     def leaves(self):
#         print("My pending leaves are 20")

# dev = developer()
# pro = programmer()

# dev.salary()
# pro.salary()

# for employee in (dev, pro):
#     employee.salary()
#     employee.location()
#     employee.leaves()


# Polymorphism with Inheritance

# class Developer:
#     def salary(self):
#         print("My salary is 45000")
    
#     def location(self):
#         print("My location is noida")

# class Programmer(Developer):
#     def location(self):
#         print("My location is pune")

# class Marketing(Developer):
#     def location(self):
#         print("My location is ghaziabad")

# dev = Developer()
# pro = Programmer()
# mar = Marketing()

# dev.salary()
# dev.location()

# pro.salary()
# pro.location()

# mar.salary()
# mar.location()


# class Calculate:
#     def average(self, a=0, b=0, c=0):
#         print("Average is:",(a+b+c)/3)

# class Child1(Calculate):
#     pass

# class Child2(Calculate):
#     pass

# cal = Calculate()
# ch1 = Child1()
# ch2 = Child2()

# cal.average(24,34)
# ch1.average(24)
# ch2.average(24,24,24)

