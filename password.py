"""
This program will print a random string of characters of a random length between six and twelve characters long. The
password will be created out of a mixture of capital letters (A-Z), lower case letters (a-z), numerals (0-9) and the
symbols: ! ? @ # & ; :
"""

from random import randrange, choice  # import extra module (choice and randrange functions from random module)
import string  # import extra module to obtain the ascii letters


character_choice = []  # create a list for password characters choice
special_char = ["!", "?", "@", "#", "&", ";", ":"]  # create a list of special characters
# characters being used in the password
character_choice.extend(list(string.digits))  # add numerals (0-9)
character_choice.extend(list(string.ascii_letters))  # add capital, normal characters (a-z & A-Z)
character_choice.extend(special_char)  # add special characters


# password generate function
def password_generator():
    pass_word = []  # create a list for the password output
    pass_len = randrange(6, 13)  # add password length (6-12)
    # create a password with the length randomly between 6 and 12
    for time in range(pass_len):  # create a loop to make the password
        pass_word.append(choice(character_choice))  # append random character to the list
    # convert the list to the string form
    pass_word = "".join(pass_word)
    return pass_word  # return the output of the function (password in the string form)


password = password_generator()  # run the function to create the password
print(password)  # print the password
