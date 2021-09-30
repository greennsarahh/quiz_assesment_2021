# variables

# Ask user questions/ main routine
def ask(question, answer):
    error= "Please"
    i = int(input(question))
    if i == answer:
        print("Correct!")
        score += 1
    else:
        print("Sorry that is incorrect, the correct answer is {}.".format(answer))

#** Main Routine ***
score = 0

q1 = ask("How many legs does a spider have?",8)
q2 = ask("How many planets are in our solar system?", 8)
q3 = ask("How many wings do bees have?", 2)
q4 = ask("How many days are in a year", 365)
q5 = ask("How many colours are in a rainbow?", 7)
q6 = ask("How many continents are there in the world?", 7)

if score >= 6:
    print("You got {} out of 6. well done. ".format(score))
elif score <= 5:
    print("You got {} out of 6. better luck next time. ".format(score))



