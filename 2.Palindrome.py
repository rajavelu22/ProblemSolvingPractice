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