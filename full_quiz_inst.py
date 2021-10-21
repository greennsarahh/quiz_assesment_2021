# variables

# Ask user questions/ main routine
def ask(question):
    error= "Please enter a whole number"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)

# Functions go here
def yes_no(questions):
    valid = False
    while not valid:
        response = input(questions).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
             response = "no"
             print("""in this game the questions will be short and you will have to answer with a integer, 
             there will be six questions. You will be able to earn 6 points! Good luck!""")
             return response

        else:
            print("please answer yes / no")

# main routine goes here
show_instructions = yes_no("Have you played this game before?")
print("You chose {}" .format(show_instructions))
print()



#** Main Routine ***
# ask a question
score = 0
q1 = ask("How many legs does a spider have?")
if q1 == 8:
    print("Correct!")
    score +=1
    print("your current score is {}".format(score))
else:
    print("sorry that is incorrect, the correct answer is 8")
q2 = ask("How many planets are in our solar system?")
if q2 == 8:
    print("Correct!")
    score +=1
    print("your current score is {}".format(score))
else:
    print("sorry that is incorrect, the correct answer is 8")
q3 = ask("How many wings do bees have?")
if q3 == 2:
    print("Correct!")
    score +=1
    print("your current score is {}".format(score))
else:
    print("sorry that is incorrect, the correct answer is 2")
q4 = ask("How many days are in a year")
if q4 == 365:
    print("Correct!")
    score +=1
    print("your current score is {}".format(score))
else:
    print("sorry that is incorrect, the correct answer is 365")
q5 = ask("How many colours are in a rainbow?")
if q5 == 7:
    print("Correct!")
    score +=1
    print("your current score is {}".format(score))
else:
    print("sorry that is incorrect, the correct answer is 7")
q6 = ask("How many continents are there in the world?")
if q6 == 7:
    print("Correct!")
    score +=1
    print("your current score is {}".format(score))
else:
    print("sorry that is incorrect, the correct answer is 7")


if score >= 6:
    print("You got {} out of 6. well done. ".format(score))
elif score <= 5:
    print("You got {} out of 6. better luck next time. ".format(score))

print("Thank you for playing")


