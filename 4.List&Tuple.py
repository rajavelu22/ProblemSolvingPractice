"""Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""

x=input("Enter Your comma seperated value : ")
#Converting into list 
#List are mutable 
l=x.split(',')
#While tuple in python is immutable 
t=tuple(l)
print(f"Your String is {x}")
print(f"Your List is {l}")
print(f"Your Tuple is {t}")