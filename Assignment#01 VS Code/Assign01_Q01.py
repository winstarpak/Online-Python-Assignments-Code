print("This is Assignment#01")
print("Output for Question#01: 'Write a PYTHON program to print the following string in given sequence' is:")
print(" ")
print("Twinkle, twinkle, little Star,")
print("         How I wonder what you are!")
print("                 Up above the world so high,")
print("                 Like a diamond in the sky.")
print("Twinkle, twinkle, little Star,")
print("         How I wonder what you are!")
print("----------------------------------------------------------------------------------------")
print("Output for Question#02: 'Write a PYTHON program to get the PYTHON version you are using' is: ")
print(" ")
import sys
print("I am using the Python with version")
print (sys.version)
print("Version info.")
print (sys.version_info)
print("----------------------------------------------------------------------------------------")
print("Output for Question#03: 'Write a PYTHON program to display current date&time' is: ")
print(" ")
from datetime import datetime
now = datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("----------------------------------------------------------------------------------------")
print("Output for Question#04: 'Write a PYTHON program which accepts radius of a circle & calculates area of the circle' is: ")
print(" ")
import math
rad = int (input("Enter radius of the Circle: "))
area = math.pi * rad * rad
print("The area of the circle is: ")
print(area)
print("----------------------------------------------------------------------------------------")
print("Output for Question#05: 'Write a PYTHON program which accepts user's first & last name and display it in reverse order with a space b/w them' is: ")
print(" ")
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print (lname +" "+ fname)
print("----------------------------------------------------------------------------------------")
print("Output for Question#06: 'Write a PYTHON program which accepts two inputs from user & print their sum' is: ")
print(" ")
print("Please provide only integers..!")
input1  = int(input("Enter first number: "))
input2  = int(input("Enter second number: "))
sum  = input1 + input2
print("The sum of both the numbers is: ")
print(sum)
print("The assignment Completed Successfully...")
print("----------------------------------------------------------------------------------------")