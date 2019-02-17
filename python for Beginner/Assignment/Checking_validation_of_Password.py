## Project 8: Checking the Validity of Password

# Validation Criteria :

# At least 1 letter between [a-z]
# At least 1 letter between [A-Z]
# At least 1 number between [0-9]
# At least 1 character from [@#$]
# Minimum length 8 characters
# Maximum length 256 characters

import re 

# == Global variables  ==

MIN_LEN = 8
MAX_LEN = 256

# ==        end        ==

if __name__ == "__main__":
    pass
    p = input("Enter your Password :  ")

    x = True

    while x:
        if (len(p) < MIN_LEN or len(p) > MAX_LEN):
            break
        elif not re.search("[a-z]", p):
            break
        elif not re.search("[A-Z]", p):
            break
        elif not re.search("[0-9]", p):
            break
        elif not re.search("[@#$]", p):
            break
        else:
            print("Valid Password !!!")
            x = False
            break
        
    if x:
        print("Not a Valid Password !!!")
        