""" Question : 38
Please raise a RuntimeError exception.
"""
#The raise keyword in Python is used to trigger an exception.
raise RuntimeError('something wrong')

##################################################################################################################################################

"""Question : 39
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
try :
    div = 5/0
except ZeroDivisionError:
    print("You Can't Divide any number by 0")


##################################################################################################################################################

"""Question : 40
Define a custom exception class which takes a string message as attribute."""

class ExceptionClass(Exception):
    """
    This is User Defined Exception Class 
    attr = msg
    """
    def __init__(self,args):
        self.args = args
        
    def __str__(self):
        # return f"self.args"
        return "".join(map(str,self.args))

Obj = ExceptionClass("This is my error message") 
print(Obj)   

##################################################################################################################################################


"""Question: 41

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john
"""


Email = input("Enter Your Email Address : ").split("@")

for elements in Email :
    print(elements)
    exit()