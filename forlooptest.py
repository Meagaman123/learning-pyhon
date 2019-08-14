import time 

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
print('mission 1\n')
time.sleep(0.05)

st = 'Print only the words that start with s in this sentence'

# for loop that runs for every word in "st", each time the for loop runs it checks if the current words has an "s" in the first letter.
# if the word in fact has an "s" in the first letter it prints the word
for i in st.split(' '):
    if 's' in i[0].lower():
        print(i)
    else:
        pass

print('\n=====!complete!=====\n')
time.sleep(0.05)


# Use range() to print all the even numbers from 0 to 10.
print('mission 2\n')
time.sleep(0.05)

# A for loop that runs from a range() value which starts at 0 and goes to 10, skipping every other number.
# For each time the for loop runs it prints the number
for i in range(0,11,2):
    print(i)


print('\n=====!complete!=====\n')
time.sleep(0.05)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('mission 3\n')
time.sleep(0.05)

# Create an empty list called div_3_num
div_3_num = []

# For loop which runs from a range() value that starts at 1 and goes to 50.
# Each time the for loop runs it does the Mod of the number checks if it is divisible by 3
# If it is divisible by three it then appends it to the div_3_num list.
# Once all numbers (1-50) has been checked it prints out the list.
for i in range(1,51):
    if i%3 == 0:
        div_3_num.append(i)
    else:
        pass
print(div_3_num)

print('\n=====!complete!=====\n')
time.sleep(0.05)


# Go through the string below and if the length of a word is even print "even!"
print('mission 4\n')
time.sleep(0.05)

st = 'Print every word in this sentence that has an even number of letters'

# For loop which runs for each word in st
# It then takes the Mod of the length of the current word and sees if it is divisible by 2
# If result is 0 then we know it is an even number and we print " "X" has "Y" letters and is even! "
for i in st.split(' '):
    if len(i)%2 == 0:
        print('\"' + i + '\"' + ' has'+f' {len(i)}'+' letters and is even!')

print('\n=====!complete!=====\n')
time.sleep(0.05)


# Write a program that prints the integers from 1 to 100. But for multiples of
# three print "Fizz" instead of the number, and for the multiples of five print
# "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
print('mission 5\n')
time.sleep(0.05)


# For loop which runs from 1-100
for i in range(1,101):

    # First checks if number is divisble by 3 and 5, if true prints FizzBuzz+number
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz' + f' {i}')
    # checks if number is divisble by 3, if true prints Fizz+number
    elif i%3 == 0:
        print('Fizz' + f' {i}')
    # checks if number is divisble by 5, if true prints Buzz+number
    elif i%5 == 0:
        print('Buzz' + f' {i}')
    # If its neither divisible by 3 or 5, then p
    else:
        print(i)

print('\n=====!complete!=====\n')
time.sleep(0.05)


# Use List Comprehension to create a list of the first letters of every word in the string below:
print('mission 6\n')
time.sleep(0.05)

st = 'Create a list of the first letters of every word in this string'
the_list = []

# For loop that for every word in st
# Each loop we append the wirst letter or the current word to an empty list
# After the loop we print the list cointaining the first letter of every loop
for i in st.split(' '):
    the_list.append(i[0])
print(the_list)

print('\n=====!complete!=====\n')
time.sleep(0.05)


# The Challenge:
#
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!

print('NUMBER GUESSING GAME!\n')
time.sleep(0.05)

# Imports random commands
import random

# Sets what number you have to guess
the_num = random.randint(1,100)
# Sets state of winning game to False
correct = False
# Creates the last guess variable and sets it to none
last_guess = None
# Creates the guess number variable
guess_nr = 0

# While loop which runs as long as the correct number hasn't been guessed
while (correct == False):

    # Asks for input from player
    guess = input('enter a interger number: ')

    # Checks if the input is a number
    try:
        guess_int = int(guess)

        # Checks if guess is within 0 and 100 when this returns true we know the guess is valid
        if 0 < guess_int <= 100:

            # Adds 1 to the gues number which is displayed after the game
            guess_nr += 1

            # Checks if the guess is correct or not, If true ends the while loop and prints the guess number
            if guess_int == the_num:
                correct = True
                print(guess_nr)
            else:

                # If the guess isn't correct, check if guess is within 10 of correct number
                # If its witin 10 it returns "WARM!", if its more than 10 it returns "COLD!"
                if abs(the_num - guess_int) > 10:
                    print('COLD!')
                else:
                    print('WARM!')

                # Checks if there has been a last guess yet, will be None if its the first round
                if last_guess == None:
                    pass
                # If its past the first round it checks if the distance from the current guess to the correct number is greater or less
                # Than last guess and correct number. If its larger then return "COLDER!", If less return "WARMER!"
                else:
                    if abs(the_num - guess_int) > abs(the_num - last_guess):
                        print('COLDER!')
                    else:
                        print('WARMER!')

            # Sets last guess up for next guess
            last_guess = guess_int

        # If guess was not within 0-100 run this code
        else:
            print('Out of bounds!')

    # If input was not a number this code runs
    except ValueError:
        print('thats not an interger number!')

# YOU WIN!!! :)
print('\n=====!!!YOU WIN!!!=====\n')
time.sleep(0.05)
