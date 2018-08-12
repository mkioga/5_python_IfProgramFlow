
# ====================
# 5_IfProgramFlow.py:
# ====================

# We will get a recap of using input function
# If you enter age "twenty" instead of 20, it works here

name = input("Please enter your name: ")
age = input("How old are you {}? ".format(name))
print("{} is {} years old. Age in string format".format(name, age))
print(age)
print()

# Note that age 22 is in string format.
# So you cannot do calculations with it.

# However we can transform age to be in int format.
# We transform age to int form by enclosing input into int
# If you enter age "Twenty" instead of 20 here, it shows error.
# This is because it it expecting an int

name = input("Please enter your name: ")
age = int(input("How old are you {}? ".format(name)))
print("{} is {} years old. Age in int format".format(name, age))
print(age)
print()

# if and else
# Now we can use the int input above with some calculations or comparisons

if age >= 18:
    print("You are old enough to vote")
    print("Please take your voting materials")
else:
    print("You will be able to vote in {} years".format(18 - age))
    print()

# if, elif, else
# We are going to use this code to see if you can guess the correct
# Number which is 5

print("Please guess a number between 1 and 20: ")
guess = int(input())

if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done. You have guessed right")
    else:
        print("Sorry. Try again. Guess a higher number")
elif guess > 5:
    print("Please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done. You have guessed right")
    else:
        print("Sorry, You have not guessed correctly")
else:
    print("You got it the first time")

# Above if, elif, else code works, but it is not the best way of
# writing code because we have duplicated some code.
# Here is a better way of consolidating above code to avoid duplication

print()
print("Please print a number between 1 and 20: ")
guess = int(input())

if guess != 5: # if guess is not equal to 5, run this code
    if guess < 5:
        print("Please guess higher ")
    else:
        print("Please guess lower ")

    guess = int(input())
    if guess == 5:
        print("Well done. you got it")
    else:
        print("Sorry, you have not guessed right")
else:
    print("Contrats. You got it the first time")



