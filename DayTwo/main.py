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

"""Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form."""

# Getting the input from the user 
X = int(input("Enter the number of rows "))
Y = int(input("Enter the number of columns "))

List = []

for i in range (0,X) :
    New_List=[]
    for j in range (0,Y) :
        value = input(f" Enter the value for the index {i} {j} ")
        New_List.append(value)
        List.append(New_List)
        
print(List)


"""Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

List = [x for x in input().split(',')]
List.sort()
print (",".join(List))