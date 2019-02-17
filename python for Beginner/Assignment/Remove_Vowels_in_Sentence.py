## Project: 2

# Removing Vowels in text

vowels = ("a","e","i","o","u")

message = input("Enter the message text: ")

new_message = ""

for letter in message:
    if letter not in vowels:
        new_message = new_message + letter
        
print("Message without vowels is : {} ".format(new_message))