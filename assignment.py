# Student Marks :

# a = int(input("Enter the marks:"))
# b = int(input("Enter the maximum marks:"))
# c = (a/b)*100
# if(c>=60):
    # print("First Division")
# elif(c>=45):
    # print("Second Division")    
# elif(c>=33):
    # print("Third Division")
# else:
    # print("Failed")        
    
# Leap year or not :

# a = int(input("Enter the year:"))
# if(a%4==0 and a%400==0 and a!=1700 and a!=1900):
#     print("",a,"is leap year")
# else:
#     print("",a,"is not a leap year")    

# Electricity Bill :

# a = int(input("Enter Electricity Unit:"))
# if(a<=100):
#    print("No bill")
# elif(a<=200):
#    b=a%100
#    c=b*5
#    print("Bill is",c)
# else:
#    b=a%100
#    c=b*10
#    print("Bill is",c)

# Check a number divisible by 4 & 6 :

# a = int(input("Enter a no:"))
# if(a%4==0 and a%6==0):
#     print("",a,"Number is divisible by 4 and 6")
# else:
#     print("Number is not divisible by 4 and 6")

# Multiplication of table:

# num = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(i*num, end=" ")

# Sum of n natural numbers:

# a = int(input("Enter a natural number:"))
# num=a
# b=0
# while(num>0):
#     b=b+num
#     num=num-1
# print("Sum of first",a,"natural number is",b) 

# Print all even no b/w given range:

# a = int(input("Enter start of range: "))
# b = int(input("Enter end of range: "))
# print("Even number is: ", end=" ")
# for i in range(a, b+1):
#     if(i%2==0):
#         print(i, end=" ")


# Print all odd no b/w given range:
 
# a = int(input("Enter start of range: "))
# b = int(input("Enter end of range: "))
# print("Odd number is: ", end=" ")
# for i in range(a, b+1):
#     if(i%2!=0):
#         print(i, end=" ")

# Print Factorial of a number:

# a = int(input("Enter a number: "))
# fact = 1
# for i in range(1,a+1):
#     fact = fact * i
# print(fact)

# Print reverse of a number :

# a = int(input("Enter Number: "))
# rev=0
# while(a>0):
#     b=a%10
#     rev=rev*10+b
#     a=a//10
# print("Reverse of number is:",rev)    
    
# Count digits in a Number :

# a = int(input("Enter a Number: "))
# count = 0
# while(a>0):
#     count = count+1
#     a=a//10
# print("The number of digits in the number are:",count)    
  
# Print Sum of all digits in a number :

# a = int(input("Enter a Number: "))
# b = 0
# while(a>0):
#     c=a%10
#     b=b+c
#     a=a//10
# print("Total sum of digits is:",b)    

# Check a number is Armstrong or not :

# a = int(input("Enter a Number: "))
# d = 0
# temp = a
# while(a>0):
#     c =a%10
#     b =c*c*c
#     d = b+d
#     a =a//10
# if(temp==d):
#     print("The number is Armstrong:",d)    
# else:
#     print("Number is not Armstrong")    

# Check a number is Strong no :

# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while(num>0):
#     rem = num%10
#     fact = 1
#     for i in range(1,rem+1):
#         fact = fact * i
#     sum = sum + fact
#     num = num//10
# if(sum == temp):
#     print("Strong Number")
# else:
#     print("Not a Strong Number")

# Check a Number is Palindrome or not :

# a = int(input("Enter Number: "))
# temp = a
# rev=0
# while(a>0):
#      b=a%10
#      rev=rev*10+b
#      a=a//10
# if(temp==rev):
#     print(" ",temp,"Number is palindrome")
# else:
#     print(" ",temp,"Number is not Palindrome")    


#  Check a number is Perfect Number :

# a = int(input("Enter a number: "))
# b = 0
# temp = a
# for i in range(1,a):
#     if(a%i==0):
#         b = b + i
# if(b==temp):
#     print("",temp,"is a perfect number")
# else:
#     print("",temp,"is not a perfect number")     
    
    
    
    
    
    
    
    
    
    