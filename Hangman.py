# Importing external functions

import random
import string
import time
import os

# Pre-assigning values to variables used throughout the code

letters = list(string.ascii_letters)
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
file = open('hangman_words sample.txt', 'r')
text = file.read()
words = text.split("\n")
word = ""
fruits = []
fruits_h = []
fruits_m = []
fruits_e = []
vegetables = []
vegetables_h = []
vegetables_m = []
vegetables_e = []
dessert = []
dessert_h = []
dessert_m = []
dessert_e = []
country_names = []
country_names_e = []
country_names_m = []
country_names_h = []
already_guessed = []
correctly_guessed = []
i_fruits = words.index('Fruit:')
i_vegetables = words.index('Vegetables:')
i_dessert = words.index('Dessert:')
i_country_name = words.index('Country Name:')
while '' in words:
    words.remove("")


# Counting the number of times a vowel is repeated in the word

def vowel_frequency(word):
    global vowels
    vowel_frequency = 0
    freq = []
    for v in vowels:
        word = word.lower()
        vowel_frequency = word.count(v)
        freq.append(vowel_frequency)
    return max(freq)


# Counting the number of times a non-vowel letter is repeated in the word

def letter_frequency(word):
    global vowels
    global letters
    freq = []
    for v in vowels:
        while v in letters:
            letters.remove(v)
    for l in letters:
        word = word.lower()
        letter_frequency = word.count(l)
        freq.append(letter_frequency)
    return max(freq)


# Creating lists based on category and level which is decided based on the following criteria:
# level 1 words are the easiest words, have vowels repeated more than twice, and different letters
# level 2 words are medium difficulty words, have vowels repeated only twice, and letter repeated twice or more
# level 3 words are the hardest words, have vowels repeated only once, and letters repeated twice or more

def lvl_list():
    global fruits
    global fruits_h
    global fruits_m
    global fruits_e
    global vegetables
    global vegetables_h
    global vegetables_m
    global vegetables_e
    global dessert
    global dessert_h
    global dessert_m
    global dessert_e
    global country_names
    global country_names_e
    global country_names_m
    global country_names_h
    i_fruits = words.index('Fruit:')
    i_vegetables = words.index('Vegetables:')
    i_dessert = words.index('Dessert:')
    i_country_name = words.index('Country Name:')
    for word in words:
        i_word = words.index(word)

        if i_fruits < i_word < i_vegetables:
            fruits.append(word)
        elif i_vegetables < i_word < i_dessert:
            vegetables.append(word)
        elif i_dessert < i_word < i_country_name:
            dessert.append(word)
        elif i_word > i_country_name:
            country_names.append(word)

    for f in fruits:
        if vowel_frequency(f) == 1 and letter_frequency(f) >= 2:
            fruits_h.append(f)
        elif vowel_frequency(f) == 2 and letter_frequency(f) >= 2:
            fruits_m.append(f)
        else:
            fruits_e.append(f)

    for v in vegetables:
        if vowel_frequency(v) == 1 and letter_frequency(v) >= 2:
            vegetables_h.append(v)
        elif vowel_frequency(v) == 2 and letter_frequency(v) >= 2:
            vegetables_m.append(v)
        else:
            vegetables_e.append(v)

    for d in dessert:
        if vowel_frequency(d) == 1 and letter_frequency(d) >= 2:
            dessert_h.append(d)
        elif vowel_frequency(d) == 2 and letter_frequency(d) >= 2:
            dessert_m.append(d)
        else:
            dessert_e.append(d)

    for c in country_names:
        if vowel_frequency(c) == 1 and letter_frequency(c) >= 2:
            country_names_h.append(c)
        elif vowel_frequency(c) == 2 and letter_frequency(c) >= 2:
            country_names_m.append(c)
        else:
            country_names_e.append(c)


# Returns the initial word the player gets - a level 1 word - if they're playing a new game

def word_generator():
    lvl_list()
    global word
    category = input(f"Which of the following categories would you like to guess from?\
        \nFruits\nVegetables\nDessert\nCountry names\nRandom\nChoice:")

    while category != 'Fruits' and category != 'Vegetables' and category != 'Dessert' and category != 'Country names' \
            and category != 'Random':
        print('Invalid entry')
        category = input(f"Which of the following categories would you like to guess from?\
            \nFruits\nVegetables\nDessert\nCountry names\nRandom\nChoice:")
    if category == 'Fruits':
        word = random.choice(fruits_e)

    elif category == 'Vegetables':
        word = random.choice(vegetables_e)

    elif category == 'Dessert':
        word = random.choice(dessert_e)

    elif category == 'Country names':
        word = random.choice(country_names_e)

    else:
        category_lst = [fruits_e, vegetables_e, dessert_e, country_names_e]
        random_category = random.choice(category_lst)
        word = random.choice(random_category)

    return word, category


# Checks if the player's level should be incremented

def lvl_checker(category, lvl, count):
    lvl_list()
    global fruits
    global fruits_h
    global fruits_m
    global fruits_e
    global vegetables
    global vegetables_h
    global vegetables_m
    global vegetables_e
    global dessert
    global dessert_h
    global dessert_m
    global dessert_e
    global country_names
    global country_names_e
    global country_names_m
    global country_names_h
    word = ""

    # If count of strikes is 0 the player goes up a level otherwise they remain in the same level

    if count == 0:
        if lvl == 1:
            lvl += 1
            if category == 'Fruits':
                word = random.choice(fruits_m)

            elif category == 'Vegetables':
                word = random.choice(vegetables_m)

            elif category == 'Dessert':
                word = random.choice(dessert_m)

            elif category == 'Country names':
                word = random.choice(country_names_m)

            else:
                category_lst = [fruits_m, vegetables_m, dessert_m, country_names_m]
                random_category = random.choice(category_lst)
                word = random.choice(random_category)


        elif lvl == 2:
            lvl += 1
            if category == 'Fruits':
                word = random.choice(fruits_h)

            elif category == 'Vegetables':
                word = random.choice(vegetables_h)

            elif category == 'Dessert':
                word = random.choice(dessert_h)

            elif category == 'Country names':
                word = random.choice(country_names_h)

            else:
                category_lst = [fruits_h, vegetables_h, dessert_h, country_names_h]
                random_category = random.choice(category_lst)
                word = random.choice(random_category)

        elif lvl == 3:
            if category == 'Fruits':
                word = random.choice(fruits_h)

            elif category == 'Vegetables':
                word = random.choice(vegetables_h)

            elif category == 'Dessert':
                word = random.choice(dessert_h)

            elif category == 'Country names':
                word = random.choice(country_names_h)

            else:
                category_lst = [fruits_h, vegetables_h, dessert_h, country_names_h]
                random_category = random.choice(category_lst)
                word = random.choice(random_category)
    else:
        count = 0
        if lvl == 1:
            if category == 'Fruits':
                word = random.choice(fruits_e)

            elif category == 'Vegetables':
                word = random.choice(vegetables_e)

            elif category == 'Dessert':
                word = random.choice(dessert_e)

            elif category == 'Country names':
                word = random.choice(country_names_e)

            else:
                category_lst = [fruits_e, vegetables_e, dessert_e, country_names_e]
                random_category = random.choice(category_lst)
                word = random.choice(random_category)

        if lvl == 2:
            if category == "Fruits":
                word = random.choice(fruits_m)


            elif category == "Vegetables":
                word = random.choice(vegetables_m)

            elif category == 'Dessert':
                word = random.choice(dessert_m)

            elif category == 'Country names':
                word = random.choice(country_names_m)

            else:
                category_lst = [fruits_m, vegetables_m, dessert_m, country_names_m]
                random_category = random.choice(category_lst)
                word = random.choice(random_category)

        if lvl == 3:
            if category == 'Fruits':
                word = random.choice(fruits_h)

            elif category == 'Vegetables':
                word = random.choice(vegetables_h)

            elif category == 'Dessert':
                word = random.choice(dessert_h)

            elif category == 'Country names':
                word = random.choice(country_names_h)

            else:
                category_lst = [fruits_h, vegetables_h, dessert_h, country_names_h]
                random_category = random.choice(category_lst)
                word = random.choice(random_category)

    # Returns the next word the player, category, level, and count is going to get
    return category, word, lvl, count


# If the player is playing a previous game
# Program uses fetched data
# otherwise program uses initiative values

def draw(real_word, word, display, already_guessed, correctly_guessed, count, lvl, category):
    global name
    print('Enter "-1" for menu')
    print("level ", lvl)
    if count == 0:
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
    if real_word == "" and display == '':
        real_word = word
        for w in word:
            if w != " ":
                display += "_"
            else:
                display += " "
    limit = 5

    # Loops until strike count meets the limit or player guesses the real word
    while count != limit and real_word.strip() != display.strip():
        guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
        guess = guess.strip()

        # Loops until entry is valid
        while (len(guess) == 0 or len(guess) >= 2 or guess not in list(string.ascii_letters)) and (guess != "-1"):
            print("Invalid Input, Try a letter\n")
            guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")

        # Checks if guess was previously entered
        if guess in already_guessed or guess in correctly_guessed:
            print("You already guessed this letter.Try another letter.\n")

        # Checks if guess or capital guess is in the word and changes display accordingly
        elif str(guess) in real_word.replace(" ", '') or str(guess.upper()) in real_word.replace(" ", ''):
            for l in word:
                if l == guess.upper():
                    correctly_guessed.append(guess.upper())
                    index = word.index(l)
                    word = word[:index] + "_" + word[index + 1:]
                    display = display[:index] + guess.upper() + display[index + 1:]
                    print(display + "\n")
                elif l == guess:
                    correctly_guessed.append(guess)
                    index = word.index(l)
                    word = word[:index] + "_" + word[index + 1:]
                    display = display[:index] + guess + display[index + 1:]
                    print(display + "\n")
        else:
            if guess != "-1":
                already_guessed.append(guess)
                count += 1
                if count == 1:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

                elif count == 2:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

                elif count == 3:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

                elif count == 4:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |    /|\ \n"
                          "  |       \n"
                          "__|__\n")
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

                elif count == 5:
                    time.sleep(1)
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     O \n"
                          "  |    /|\ \n"
                          "  |    / \ \n"
                          "__|__\n")
        # Menu displays when "-1" is entered
        if guess == "-1":
            print(f"(i)Pause and save the game\n(ii) exit game\n(iii) continue game ")
            menu = input("Enter (i/ii/iii)")

            # Validating entry
            while menu != "i" and menu != "ii" and menu != "iii":
                print("Invalid entry,please enter one of the given choices")
                menu = input("Enter (i/ii/iii)")
            if menu == "i":
                print("One second, saving progress...")
                file = open(name + ".txt", 'w')
                # Saving progress to player's file
                file.write(
                    f'{real_word}\n{word}\n{display}\n{already_guessed}\n{correctly_guessed}\n{count}\n{lvl}\n{category}')
                exit()
            elif menu == "ii":
                print("Exiting game")
                exit()
        if real_word.strip() == display.strip():
            print("Congrats! You have guessed the word correctly!")
            # Asks the user if they'd like to continue playing if they guessed the word
            print("Would you like to continue playing?")
            CorE = input("Enter (C/c) to continue or (E/e) to exit")
            # Validating entry
            while CorE != "C" and CorE != "c" and CorE != "E" and CorE != "e":
                print("Invalid entry,please enter one of the given choices")
                CorE = input("Enter (C/c) to continue or (E/e) to exit")

            if CorE == "C" or CorE == "c":
                hangman(category, lvl, count)
            else:
                exit()
        if count == limit:
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", real_word)
            hangman(category, lvl, count)


def play_loop():
    global play
    global name
    # Asks player for their name and looks for a text file of the same name
    try:
        name = input("Please enter your name:")
        file = open((name + '.txt'), 'r')
        # Makes sure it's a non-empty file
        if os.path.getsize(name + '.txt') != 0:
            print(f"Welcome back {name}!\n")
            play = input(f"Enter (P/p) if you would like to continue a previous game\nEnter (N/n) if you would like to "
                         f"play a new game\n")

            # Validating entry
            while play != "P" and play != "p" and play != "N" and play != "n":
                print("Invalid entery! Please enter one of the given choices.")
                play = input(
                    f"Enter (P/p) if you would like to continue a previous game\nEnter (N/n) if you would like to "
                    f"play a new game\n")
        else:
            # When file is empty, asks user if they want to play
            print("Your file is empty")
            play = input(f"Enter (Y/y) if you would like to play\nEnter (N/n) if you want to exit\n")
            while play != "Y" and play != "y" and play != "N" and play != "n":
                print("Invalid entery! Please enter one of the given choices.")
                play = input(f"Enter (Y/y) if you would like to play\nEnter (N/n) if you want to exit\n")
            if play == "N" or play == "n":
                exit()

    # Creates file if it doesn't exist
    except FileNotFoundError:
        print(f"You're new here! Welcome {name}")
        play = input(f"Enter (Y/y) if you would like to play\nEnter (N/n) if you want to exit\n")
        while play != "Y" and play != "y" and play != "N" and play != "n":
            print("Invalid entery! Please enter one of the given choices.")
            play = input(f"Enter (Y/y) if you would like to play\nEnter (N/n) if you want to exit\n")
        if play == "N" or play == "n":
            exit()


def main():
    global count
    global display
    global word
    global already_guessed
    global correctly_guessed
    global lvl

    global letters
    play_loop()
    if play == "p" or play == "P":

        # Assigning data from file as values to variables and sends as parameter to the draw function
        file = open(name + '.txt', 'r')
        data_list = file.read().split("\n")
        real_word = str(data_list[0])
        display = str(data_list[1])
        word = str(data_list[2])
        for i in data_list[3]:
            if i in letters:
                already_guessed.append(i)
        for i in data_list[4]:
            if i in letters:
                correctly_guessed.append(i)
        count = int(data_list[5])
        lvl = int(data_list[6])
        category = str(data_list[7])
        previous_play(real_word, word, display, already_guessed, correctly_guessed, count, lvl, category)

    elif play == "N" or play == "n" or play == "Y" or play == "y":
        intial_hangman()


def hangman(category, lvl, count):
    # The function most used throughout the game
    already_guessed = []
    correctly_guessed = []

    # Assigning values to variables using the function lvl_checker
    category, word, lvl, count = lvl_checker(category, lvl, count)
    real_word = ""
    display = ""
    draw(real_word, word, display, already_guessed, correctly_guessed, count, lvl, category)


# This function is called when player chooses to continue a previous play
def previous_play(real_word, display, word, already_guessed, correctly_guessed, count, lvl, category):
    draw(real_word, word, display, already_guessed, correctly_guessed, count, lvl, category)


# This function is called when player chooses to play a new game
def intial_hangman():
    already_guessed = []
    correctly_guessed = []
    lvl = 1
    count = 0
    word, category = word_generator()
    real_word = ""
    display = ""
    draw(real_word, word, display, already_guessed, correctly_guessed, count, lvl, category)


main()
