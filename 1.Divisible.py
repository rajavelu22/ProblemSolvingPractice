
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