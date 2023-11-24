#PROBLEM NO 01):
#Write a Program to find the greatest of four numbers entered by the user?
# num1 =int(input("Enter The Number1:  "))
# num2 =int(input("Enter The Number2:  "))
# num3 =int(input("Enter The Number3:  "))
# num4 =int(input("Enter The Number4:  "))

# if(num1>num4):
#    f1 = num1
# else:
#    f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#    f2 = num3

# if(f1>f2):
#    print(str(f1) + "  Is Greatest")
# else:
#    print(str(f2) + "  Is Greatest")
    

#PROBLEM NO 02):
#Write a Program to find out whether a student pass or fail, if it requires
#total 40% and at atleast 33% in each subject to pass.Assume 3 subjects | 
#note: take the marks as an input from the user.

# sub_1=int(input("Enter Marks of Computer \n"))
# sub_2=int(input("Enter Marks of Physics \n"))
# sub_3=int(input("Enter Marks of Mathematics \n"))

# if(sub_1<33 or sub_2<33 or sub_3<33):
#    print("\nYou Are Fail Because You Have Less Than 33% In One Of The Subject\n")

# elif(sub_1+sub_2+sub_3)/3 <40:
#    print("\nYou Are Fail Due To Total Percentage Less Than 40%\n")

# else:
#    print("\nCongratulations! You Are Passed The Exam")


#PROBLEM NO 03):
# write a program to detect the following words in the text take text as a input:
# "make alot of money","buy now","click this","subscribe this" 

# text=input("Enter The Text:\n  ")

# if("make alot of money" in text):
#     print("****SPAM****")

# elif("buy now" in text):
#     print("****SPAM****")

# elif("click this" in text):
#     print("****SPAM****")

# elif("subscribe this" in text):
#     print("****SPAM****")

# else:
#     print("****NO SPAM****")


#PROBLEM NO)4)
#Write a program to find whether a given usernamecontains less than 10 
# characters or not?

# username = input("Enter Your Username:  ")
# if(len(username))>10:
#     print("Username contains more than 10 chracters.")

# else:
#       print("Username cannot contains more than 10 chracters.")


#write a program which finds out whether a given name is present in a list or not.

# list_001=['Ibad', 'Ahmed', 'Ammar', 'Ali' ]

# myname=input("Enter Your Name:  ")
# if(myname in list_001):
#     print("The Given Name Is Present In The List")
# else:
#     print("The Given Name Is Not Present In The List")


# PROBLEM NO:06)
# Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 50-60 = Fail
# 60-70 = D
# 70-80 = c
# 80-90 = B
# 90-100 = Excellent

#Marks of the student:
# marks1=int(input("Enter The Marks Of Physics:   "))
# marks2=int(input("Enter The Marks Of Maths:   "))
# marks3=int(input("Enter The Marks Of English:   "))
# marks4=int(input("Enter The Marks Of Urdu:   "))

# total_marks=marks1+marks2+marks3+marks4
# percentage_stud=(total_marks/400)*100

# if(percentage_stud>90):
#     print("EXCELLENT")

# elif(percentage_stud>=80 ):
#     print("A GRADE")

# elif(percentage_stud>=70 ):
#     print("B GRADE")

# elif(percentage_stud>=60 ):
#     print("C GRADE")

# elif(percentage_stud>=50 ):
#     print("D GRADE")

# else:
#     print("FAIL")

