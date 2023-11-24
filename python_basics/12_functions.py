# CALCULATING PERCENTAGE OF MARKS WITHOUT FUNCTIONS:
marks1 = [45, 56 ,67, 89, 51]
percentage_1= ((marks1[0] + marks1[1] + marks1[2] + marks1[3] + marks1[4])/400)*100

marks2 = [55, 56 ,17, 92, 61]
percentage_2= ((marks2[0] + marks2[1] + marks2[2] + marks2[3] + marks2[4])/400)*100
print(percentage_1,"\n",percentage_2)

# CALCULATING PERCENTAGE OF MARKS WITH FUNCTIONS:
def percentage(marks):
    p=((marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/400)*100
    return p

marks1 = [45, 56 ,67, 89, 51]
percentage_1=percentage(marks1)

marks2 = [55, 56 ,17, 92, 61]
percentage_1=percentage(marks2)
print(percentage_1,"\n",percentage_2)

def mysum(num1, num2):
    return num1+num2
def greet(name):
    print("Good Day: "+ name )
    
greet("HARRY")
s=mysum(9, 1)
print(s)

#DEFAULT ARGUMENTS IN FUNCTIONS:
def greet(name = "STRANGER"):
    print("Good Day: "+ name )

greet("IBAD")
greet()

#RECURSION IN FUNCTIONS:

    

