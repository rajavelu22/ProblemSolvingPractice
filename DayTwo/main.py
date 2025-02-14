"""Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters"""

class Python(object) :
     def __init__(self):
         pass
     
     def setString(self):
         self.String = str(input("Enter Your String : "))
         
     def getString(self) :
         return self.String
     
     def testPrint(self) :
         print(f"This is test method to check the python class {self.String}")
        
ObjectOne = Python()
##this will call the setString and gets the input from the user
ObjectOne.setString()

#The user value will be passed to the X object here 
X = ObjectOne.getString()

#testing the class is working properly
ObjectOne.testPrint()

"""Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

import math
#Declaring and Initializing variable 

C = int(2*50) 
H = 30

ToDict = [int(x) for x in input().split(',')]
X=[]

for D in ToDict :
    X.append( str(round(math.sqrt(D*C/H))) )
    
print(X)