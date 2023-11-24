# # AIRTHEMATIC OPERATORS: 
# a = 5
# b = 9
# print(a+b)
# a -= 9
# print(a)

# num1 = 90
# num2 = 9

# num1%=28
# print(num1)

# #LOGICAL OPERATORS:
# x = 7
# y = 90
# print("The value of x is:",x,"\nThe value of y is:",y)
# print(x!=y or x>y)
# print(x!=y and x>y)


# # STRINGS METHODS:
# name = "Muhammad Ibad"
# print("Hello,  ", name)
# print("Hello, ", name.capitalize())
# print("Hello, ", name.upper())
# print("Hello, ", name.lower())
# print("Hello, ", name[0:3])
# print("Hello, ", name[3:6])
# print("Hello, ", name[6])
# print("Hello, ", name.count('a'))
# print("Hello, ", name.isalnum())
# print("Hello, ", name.isnumeric())
# print(name)

# LISTS METHODS:
# l1 = [12, 45,  85, 46,  41 , 66 ]
# print(l1)
# print(type(l1))
# print(l1.count(45))
# l1.remove(45)
# l1.extend([77, 98, 76])
# l1.pop()
# l1.append(78)
# l1.sort()
# print(l1)



# a = int(input("Enter The Number: "))

# if(a==1):
#     print("The value Of a = 1")
# elif(a==2):
#     print("The value Of a = 2")
# elif(a==3):
#     print("The value Of a = 3")
# elif(a==4):
#     print("The value Of a = 4")
# elif(a==5):
#     print("The value Of a = 5")
# elif(a==6):
#     print("The value Of a = 6")
# else:
#     print("Invalid Value Entered!")
    

# l2= [1, 2, 34, 56, 88, 99]
# for item in l2:
#     print(item)


# i= 0
# while(i<10):
#     print(i)
#     i+=1

# while(True):
#         number = int(input("Enter the Number: "))
#         print(number)
#         if(number==0):
#             break
# print("Program Has Finished Executing.....")


# try:    
#     number2 = int(input('Enter the Number: '))
#     print(number2 + 5)
# except Exception as e:
#      print("Some Error Occured\n", e)


# WRITE IN FILE HANDLING:
s = "Harry is a Good Boy"
with open("Test.txt", "w") as f:
     f.write(s)

# READ IN FILE HANDLING:
with open('Test_2.txt', "r") as f:
     s1 = f.read()
     print(s1)

# APPEND IN FILE HANDLING:
with open('Test_2.txt', "a") as f:
     f.write('''
This is a Python tutorial in Hindi with a focus on learning through
project-based examples.
The instructor highlights the importance of hands-on experience and mentions that they have earned money through freelancing Python projects.''')