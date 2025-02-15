# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between user defined ranges (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

while True:
    start = int(input("Enter your range from: "))
    end = int(input("Enter your range up to: "))
    
    output = []
    print("Printing numbers that are divisible by 7 but not by 5:")
    
    for i in range(start, end):
        if i % 7 == 0 and i % 5 != 0:
            output.append(str(i))  
    
    result = ','.join(output)  
    print(result)
    
    option = input("Do you want to continue? Press Y or N: ")
    if option.upper() != "Y":
        break
    
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

Number = int(input("Enter your number : "))
if(Number==0):
    print("The palindrome is 1")
else:
    for i in range (1,Number):
        Number=Number*(Number-i)
    print("The palindrome is ",Number)
    
"""Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

end=int(input("Enter Your Number : "))

output=dict()
for i in range (1,end+1):
    output[i]=i*i
print(output)

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