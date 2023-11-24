# # Writing a program to add 2 numbers by taking number as a input?
# num01=input("Enter Number1  ")
# num02=input("Enter Number2  ")

# #since input is always a str converting str to int
# #Now:
# num01=int(num01)
# num02=int(num02)

# print("The Addition of Number1 & Number2 =" , num01+num02)



# #Q02)Write a program to compare 2 numbers by taking number as a input?
# num3=input('Enter Number 1: ')
# num4=input('Enter Number 2: ')

# #since input is always a str converting str to int
# #Now:
# num3=int(num3)
# num4=int(num4)
# print('The comparison of 2 numbers are', num3==num4)

# #Q03)Write a program to calculate avg of 2 numbers by taking number 
# # as a input?
# num5=input('Enter Number 1: ')
# num6=input('Enter Number 2: ')

# #since input is always a str converting str to int
# #Now:
# num5=int(num5)
# num6=int(num6)
# print('The avg of 2 numbers are', (num5+num6)/2)

# # #STRINGS PRACTICE QUESTIONS

# #Problem:1
# #Write a program to display a user entered name followed by good 
# #afternoon using input()function?
# Hi=input("Enter Your Name: ")
# print ("Good Afternoon "+ Hi+ "!")

# # Problem:2
# # Write a program to fill in a letter tempelate given below with 
# # name and date?
# letter='''Dear <|Name|>,
# Greetings from XYZ Coding House, I am happy to tell you that yo're 
# selected as a Developer in our renownable organization, hope you will 
# do your best in your role and position and make us proud.
# Have a good day ahead!
# Thanks and regards,
# Steve

# # Date: <|Date|>
# '''
# name = input("Enter Your Name\n")
# date = input("Enter Your Date\n")
# letter=letter.replace("<|Name|>",name)
# letter=letter.replace("<|Date|>",date)
# print(letter)

# #Problem:3
# #Write  progrm to detect double spaces in a string?
# str1="""This   is    my     String"""
# str1=str1.find("  ")
# print(str1)

# #Problem:4
# #Write  progrm to replace the double spaces in a string?
# str2=''''This    is    my    String'''
# doublespaces=str2.replace("    "," ")
# print(doublespaces)

# #Problem:4
# #write a program to format the following letter using escape 
# #squence characters.  
# #letter="Dear harry,this python coURse is NicE.thanKs!"
# letter2="Dear harry,this python coURse is NicE.thanKs!"
# formatted_letter2="Dear harry,\n\tthis python coURse is NicE.\nthanKs!"
# print(formatted_letter2.capitalize())

