"""Question:31
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
"""
# List = []

# for i in range (1,21):
#     x = int (i**2)
#     List.append(x)

# print(tuple(List))

##################################################################################################################################################

"""Question:32
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

"""
# values = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# print(values[:5],end="")
# print(values[-5:],end="")

##################################################################################################################################################

"""
Question:33
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)."""

values = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# output = tuple(x for x in values if x % 2 == 0)
print(tuple(x for x in values if x % 2 == 0))

##################################################################################################################################################

"""Question:34
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10]."""

List = [1,2,3,4,5,6,7,8,9,10]

Output = filter(lambda x:x%2==0,List)

##################################################################################################################################################

"""Question:35
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]."""

List = [1,2,3,4,5,6,7,8,9,10]

Output = map(lambda x:x**2 , filter(lambda x:x%2==0,List))
print(list(Output))

##################################################################################################################################################

"""Question:36
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)."""

FilterOutput = list(filter(lambda x:x%2==0 , range(1,21)))
print(FilterOutput)

##################################################################################################################################################

"""Question:37
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)."""

ListOutput = list(map(lambda x:x**2 , range(1,21)))
print(ListOutput)

##################################################################################################################################################


