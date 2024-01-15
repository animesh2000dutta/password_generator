import random
import string

def generate_password(min_length,numbers=True, special_characters=True):
    letter=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters = letter
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special

    
    password=""
    meet_criteria=False
    has_number=False
    has_special=False

    while not meet_criteria or len(password) < min_length:
        new_char=random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number=True
        if new_char in digits:
            has_special=True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_number

    return password

min_length= int(input("enter length of the password: "))
has_number= input("Do you wnat to add numbers (y/n)").lower() == "y"
has_special= input("Do you want to add special numbers (y/n)").lower() == "y"
password = generate_password(min_length,has_number,has_special)
print("The genrated passowrd is : ",password) 


