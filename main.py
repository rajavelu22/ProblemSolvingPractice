"""Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""

Input = input("Enter your comma seperated values ").split(",")
Output = [str(int(x)**2) for x in Input if int(x)%2!=0]
for element in Input :
    X=int(element)
    if(X%2!=0):
        X=X*X
        Output.append(str(X))

print(",".join(Output))

"""Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""
Total = 0
while True :
    D = input("Enter D <amount> ==> For Deposit\nThen W <amnt> ==> For withdrawal ").split(" ")
    operation = D[0]
    if not D :
        break
    elif(operation == "D") : 
        netAmount = int(D[1])
        Total += netAmount
    elif operation == "W":
        netAmount = int(D[1])
        Total -= netAmount
    else :
        print(Total)
        exit()
"""Same thing using dictionary with additional terms and conditionx"""       
# account = {"Balance": 0}  

# Dictionary to store balance

# while True:
#     D = input("Enter D <amount> ==> For Deposit\nThen W <amount> ==> For Withdrawal: ").split()

#     if not D:  # If input is empty, exit
#         break

#     operation = D[0]

#     if operation in ["D", "W"]:  
#         if len(D) < 2 or not D[1].isdigit():
#             print("Invalid amount. Please enter a number.")
#             continue

#         amount = int(D[1])

#         if operation == "D":  # Deposit
#             account["Balance"] += amount
#         elif operation == "W":  # Withdrawal
#             if account["Balance"] >= amount:
#                 account["Balance"] -= amount
#             else:
#                 print("Insufficient balance.")

#     else:
#         print("Invalid operation. Use 'D' for deposit or 'W' for withdrawal.")
#         exit()

#     print("Current Balance:", account["Balance"])

"""Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1"""

Input = input("Enter your list of password to check the validity seperated with comma\'s ").split(",")

Output = []
for element in Input :
    flagOne = flagTwo = flagThree = flagFour = flagFive = 0
    if len(element)>=6 and len(element)<=12 :
        flagOne = 1
        for x in element :
            if x.isalpha() :
                if x.isupper() :
                    flagTwo=1
                else :
                    flagThree=1
            if x.isdigit() :
               flagFour=1
            if x in "@#$" :
                flagFive=1
    if flagOne == flagTwo == flagThree == flagFour == flagFive == 1 :
        Output.append(element)
print(Output)
########################################### Better method ##########################################
"""passwords = input("Enter passwords separated by commas: ").split(",")

valid_passwords = []

for password in passwords:
    if 6 <= len(password) <= 12:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "$#@" for c in password)

        if has_upper and has_lower and has_digit and has_special:
            valid_passwords.append(password)

print("Valid passwords:", valid_passwords)
"""



"""Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys."""               

from operator import itemgetter
      
List = []
while True :
    Input = input ("Enter your comma seperated value ").split(",")
    if Input == [""]:
        break
    List.append(tuple(Input))   
    
print (sorted(List, key=itemgetter(0,1,2)))
