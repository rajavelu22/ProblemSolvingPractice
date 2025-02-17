"""Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield"""

# class Generator :
#     def Start(self) :
#         Start = int(input("Enter the from range for finding number which are divisible by 7 "))   
#         End = int(input())+1
        
#         num = [x for x in range ( Start , End) if(x%7==0)]
#         return num

# Obj = Generator()
# Output = Obj.Start()
# print(",".join(map(str,Output)))


##################################################################################################################################################################################################################################################


"""Question 21
Level 3

Question :
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

# import math
# Input = input("Enter your travel details on graph ").split(" ")

# Up = int(Input[1])
# Down = int(Input[3])
# Left = int(Input[5])
# Right = int(Input[7])

# XTwo = (Up-Down)
# YTwo = (Right-Left)

# #Calculating distance travelled using the below formulae
# Dist = math.sqrt((XTwo**2)+(YTwo)**2)
# print(round(Dist))

# Optimized method

"""import math

# Initialize movement dictionary
movement = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}

# Take multiple lines of input until the user presses Enter (empty input)
while True:
    try:
        line = input().strip()  # Read a line and remove extra spaces
        if not line:  # Stop if the user just presses Enter
            break
        direction, steps = line.split()  # Split into direction and step count
        movement[direction] += int(steps)  # Update the movement dictionary
    except ValueError:
        print("Invalid input format. Please enter direction and steps correctly.")
        continue

# Calculate final coordinates
x_final = movement["RIGHT"] - movement["LEFT"]
y_final = movement["UP"] - movement["DOWN"]

# Compute Euclidean distance from (0,0)
distance = math.sqrt(x_final**2 + y_final**2)

# Print rounded result
print(round(distance))"""



##################################################################################################################################################################################################################################################



"""Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input."""


# Input = input("Enter your Statement ").split(" ")
# SetInput = set(Input)
# Store = {}
# for element in SetInput :
#     Store.setdefault(element,Input.count(element))
# print({ Key : Value for Key , Value in sorted(Store.items()) })


##################################################################################################################################################################################################################################################


"""Question 23
level 1

Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator"""
# Input = int(input("Enter the number to square : "))
# print(Input**2)
