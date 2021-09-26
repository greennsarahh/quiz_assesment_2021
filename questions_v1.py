# variables
score = 0

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low/ high give
            if low < response <= high:
                return response


        # output an error
            else:
                print(error)

        except ValueError:
            print(error)

def yes_no(questions):
    valid = False
    while not valid:
        response = input(questions).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

def instruction():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

played_before = yes_no("Have you played the game before?")
print("You chose {}" .format(played_before))
print()
if played_before == "no":
    instruction()
print("Program continues")

how_much = num_check("How much would you like to play with? ", 0, 10)
print("You will be spending ${}" .format(how_much))
balance = how_much

play_again = input("Press <enter> to play...").lower()
while play_again == "":


# Ask user questions/ main routine

answer = int(input("How many legs does a spider have?"))
if answer == 8:
    print("Correct!")
    score += 1
else:
    print("Sorry that is incorrect, the correct answer is 8.")

answer = int(input("How many planets are in our solar system?"))
if answer == 8:
    print("Correct!")
    score += 1
else:
    print("Sorry that is incorrect, the correct answer is 8.")

answer = int(input("How many wings do bees have?"))
if answer == 2:
    print("Correct!")
    score += 1
else:
    print("Sorry that is incorrect, the correct answer is 2.")

answer = int(input("How many days are in a year"))
if answer == 365:
    print("Correct!")
    score += 1
else:
    print("Sorry that is incorrect, the correct answer is 365.")

answer = int(input("How many colours are in a rainbow?"))
if answer == 7:
    print("Correct!")
    score += 1
else:
    print("Sorry that is incorrect, the correct answer is 7.")

answer = int(input("How many continents are there in the world?"))
if answer == 7:
    print("Correct!")
    score += 1
else:
    print("Sorry that is incorrect, the correct answer is 7.")

print("Your final score is {} out of 6".format(score))
print()

if answer >= 6:
    print("Well done thank you for playing!")
elif answer <= 5:
    print("Better luck next time, thank you for playing")






