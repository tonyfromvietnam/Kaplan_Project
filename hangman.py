"""
This program will play a game of Hangman with the user. This program will first choose a secret word at random out of a
list of words. This program will then display a dash for each letter of the secret word. The user will guess letters,
one at a time, to try to guess the secret word. If the user guesses a letter in the secret word that letter will replace
the dash in the correct position.
If the user guesses a letter that does not appear in the secret word the program will reduce the number of incorrect
guesses available by one. If the user correctly guesses all the letters in the word, the user wins the game. Otherwise
when the user runs out of incorrect guesses the program wins.
After each game the user will have the option to play again.
"""

from random import choice  # import extra module (choice from random module)

count = 10  # number of attempts
list_of_words = ["python", "string", "mathematics", "kaplan", "london", "it", "hangman", "chairs", "backpack",
                 "clothes", "computer", "program", "glasses", "shirt", "pants", "friends", "food",
                 "apple", "banana", "straws", "study"]
random_word = choice(list_of_words)


# create a function that display dash (-) instead of the characters
def display_dash():
    word = []
    for _ in random_word:  # create a loop to convert the word to dash
        word.append("-")  # add dash to the list word
    dash = "".join(word)  # convert list to string
    return dash  # return the word the in dash form


# create a function that replace letter in case of dash (-) in the word
def update_word():
    new_word = None  # create a new variable to store the word after player's guesses
    word = list(user)  # create a variable to store the word in list form
    for number, value in enumerate(random_word):  # find the positions of the chosen character
        if person_choice == value:
            word[number] = person_choice  # change the dash to the chosen character
        new_word = "".join(word)  # convert the type of variable new_word from list to string
    return new_word  # return the output of the function


user = display_dash()  # create a variable to store the output of display_dash function (The word in dash form)

# the program start
while True:
    print(user)  # print the word in the latest form
    person_choice = str(input("Your guess (1 word): ")).lower()  # ask the user to input a character
    if not person_choice.isalpha():  # check the input is a letter. Also checks the input has been made.
        print("That is not a letter. Please try again.")
        continue
    elif len(person_choice) > 1:  # check the input is only one letter
        print("That is more than one letter. Please try again.")
        continue

    # if the player's input is match
    if person_choice in random_word:
        user = update_word()  # run the function update_word

    # if the choice is not match
    if person_choice not in random_word:
        count -= 1  # reduce the chances by 1
        if count == 0:  # chance = 0 (lose the game)
            print("You lose, 0 remaining guess.")
            print("The word is:", random_word)
            # decision to play again
            decision = str(input("\nPress \"Yes\" to play again\n."))
            # if the player wants to play again
            if decision.lower() == "yes":
                count = 10  # recreate the number of attempts
                random_word = choice(list_of_words)  # choose the new word
                user = display_dash()  # convert the word to dash
                continue
            # if the player doesn't want to play again
            else:
                break

        else:  # other possibilities
            print("Try again")
            print("You have", count, "remaining guess(es).")

    # when the dash is filled (win the game)
    if user == random_word:
        print("Congratulations\nYou won!")
        print("The word is:", random_word)
        # decision to play again
        decision = str(input("\nPress \"Yes\" to play again.\n"))
        # if the player wants to play again
        if decision.lower() == "yes":
            count = 10  # recreate number of attempts
            random_word = choice(list_of_words)  # choose the new word
            user = display_dash()  # convert the word to dash
            continue
        # if the player doesn't want to play again
        else:
            break
