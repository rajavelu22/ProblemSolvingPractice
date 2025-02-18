"""Question:27
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only."""

taskDict = {}

for i in range (1,20) :
    x= i*i
    taskDict.setdefault(i,str(x))
print(",".join(list(taskDict.values())))


##############################################################################################################################################################


"""Question:28
Define a function which can generate and print a list where the values are square of numbers"""

import math
TaskList = input("Enter the comma seperated values ").split(",")
Output = [x for x in TaskList if (math.isqrt(int(x))**2) == int(x) ]
print(Output)


##############################################################################################################################################################



"""Question:29
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
"""

import math
##Setting the Sqrt List here
TaskList = input("Enter the comma seperated values ").split(",")
Output = [x for x in TaskList if (math.isqrt(int(x))**2) == int(x) ]
print(Output)

##Getting the last Five
Length = len(Output)
LastFive = Output[-5:]
print("LasFive ",LastFive)


################################################################################################################################################


"""
Question:30
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.
"""
import math
##Setting the Sqrt List here
TaskList = input("Enter the comma seperated values ").split(",")
Output = [x for x in TaskList if (math.isqrt(int(x))**2) == int(x) ]
print(TaskList)
print(len(TaskList))
ListLength = len(Output)-5
print(ListLength)
#Getting the elements in the list execpt first five
print (Output[ListLength:])


#######################################################################################################################
