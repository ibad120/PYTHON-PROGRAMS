# #FOR LOOPS PRACTICE QUESTIONS:
# #PROBLEM 01)
# # Write a program of writng a table from for loop?
# number=int(input("ENTER THE NUMBER:  "))
# for i in range(11):
#     print(str(number) + "X" + str(i) + "=" + str(i*number))
#     #'F' STRING IN FOR LOOP:
#     # print(f"{number}X{i}={i*number}")

# #PROBLEM 02)
# #write a program to greet all the person names started in a list l1 and which starts with 'S'
# l1=['Ahmed' , 'Farhan' , 'Ali' , "Shayan" , 'Sami' , 'Hamza']
# for name in l1: 
#     if name.startswith('S'):
#         print('HELLO  ' + name)


# #PROBLEM 03)
# # ATTEMPT PROBLEM 01 USING WHILLE LOOP:
# number_1=int(input("ENTER THE NUMBER:  "))
# I1=0
# while I1<=10:
#     print(str(number_1) + "X" + str(i) + "=" + str(i*number_1))
#     I1=I1+1

# #PROBLEM 04)
# #write a program to find whether a given number is prime or not
# number2=int(input("ENTER THE NUMBER:  "))
# prime=True
# for i in range(2 , number2):
#     if number2%i== 0:
#         prime=False
#         break
# if prime:
#         print("THIS NUMBER IS PRIME")
# else:
#         print("THIS NUMBER IS NOT PRIME")




# #PROBLEM 05)
# #Write a program to find the sum of first n natural numbers
# def sum_of_naturals(n):
#     return n * (n + 1) // 2

# n = int(input("Enter the value of n: "))
# print("The sum of the first", n, "natural numbers is", sum_of_naturals(n))

# #USING FOR LOOP:

# def sum_of_natural_numbers(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# n = int(input("Enter a number: "))
# print("The sum of the first", n, "natural numbers is", sum_of_natural_numbers(n))

# #PROBLEM 06)
# #Write a program to calculate the factoraial of a given number?
# number3=int(input("ENTER THE NUMBER:  "))
# factorial = 1
# for i in range(1, number3+1):
#     factorial=factorial * i
# print ("THE FACTORIAL OF ", number3 ,"IS:", factorial )
# # print(f"The Factorial of {number3}is: {number3+i*number3}")


# #PROBLEM 07)
# #Write a program to print the following star pattern?
# # '   *'
# # '  ***'
# #'  *****'
# #' *******'
# n=3
# for i in range(3):
#         print(" " * (n-i-1), end="")
#         print("*" * (2*i+1), end="")
#         print(" " * (n-i-1))


# #PROBLEM 08)
# #Write a program to print the following star pattern?
# # '*'
# # '**'
# # '***'
# # '****'
# n=4
# for i in range(4):
#     print("*" * (i+1))