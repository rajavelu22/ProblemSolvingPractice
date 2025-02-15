"""Question 9
Level 2

Question :
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""
while True :
    print(input("Enter your sentence : ").upper())
    
"""Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data."""

WS_Input = input("Enter your sentence seperated by white space : ").split(" ")


print( " ".join((list(sorted(set(WS_Input))))))

"""Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

BinaryInput = input("Enter your comma seperated input : ").split(",")
R = 0
Divisible = []
for element in BinaryInput :
    X = int(element,2)
    if ( X%5 == 0) :
        Divisible.append(element)

print(" ".join(Divisible))

"""Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

CSV=[]
for i in range (1000,3001):
    s = str(i)
    if(int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0): 
        CSV.append(s)
print (",".join(CSV))


"""Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""

UserInput = input("Enter your sentence ")
digit = 0
alpha = 0
for element in UserInput : 
    if (element.isdigit()) : 
        digit+=1
    elif (element.isalpha()) : 
        alpha+=1
        
print(f"Digits : {digit}\nLetters : {alpha}")

"""Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

"""Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

UserInput = input("Enter your sentence : ")
Count = { "Upper" : 0 , "Lower" : 0 }
for element in UserInput :
    if(element.isupper()) : 
        Count["Upper"]+=1
    else :
        Count["Lower"]+=1
print(Count)

"""Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

UserInput = int(input("Enter your number "))
loop = 4
Count=0
while(loop):
    loop-=1
    Count += UserInput
    UserInput = (UserInput*10)+9   
print(Count)