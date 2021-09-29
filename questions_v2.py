# variables
score = 0
# Ask user questions/ main routine
def ask(question, answer):
    i = int(input(question))
    if i == answer:
        print("Correct!")
        score += 1
    else:
        print("Sorry that is incorrect, the correct answer is {}.".format(answer))

#** Main Routine ***
score = 0
question = ask("How many legs does a spider have?",8)
question = ask("How many planets are in our solar system?", 8)
question = ask("How many wings do bees have?", 2)
question = ask("How many days are in a year", 365)
question = ask("How many colours are in a rainbow?", 7)
question = ask("How many continents are there in the world?", 7)


