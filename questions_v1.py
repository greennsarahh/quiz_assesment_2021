# variables

# Ask user questions/ main routine
def question(score = 0):
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
question()






