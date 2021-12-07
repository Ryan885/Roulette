import random

#comment code uh anyway compile
from typing import Any, Union

parityvalue = 0
colourvalue = 0
parity = ""
colour = ""

ball_results = ["G0", "R1", "B2", "R3", "B4", "R5", "B6", "B7", "R8", "B9", "R10", "B11", "R12", "R13", "B14", "R15", "B16", "R17", "B18", "B19", "R20", "B21", "R22", "B23", "R24", "G25"]




# Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response
            # response to yes

        elif response == "no" or response == "n":
            response = "no"
            return response
            # response to no

        elif response == "exit":
            print("You end the game with ${}. You started with ${}".format(money, budget))
            exit()
        else:
            print("Please answer yes / no")
        # neither

def budget_que(question, low, high):
    error = "Your Budget should be a whole number between $10 and $1000\n"
    valid = False
    while not valid:
        try:
            # ask the question and remove the $ symbol if the user has entered it
            response = int(input(question).replace('$', ''))
            # if the amount is too low / too high give
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
def parityselection(question):
    global parity
    error = "Please select odd or even."
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "odd" or response == "o":
            response = "odd"
            parity = "odd"
            return response
        elif response == "even" or response == "e":
            response = "even"
            parity = "even"
            return response
        else:
            print(error)

def colourselection(question):
    global colour
    error = "Please select red or black."
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "red" or response == "r":
            response = "red"
            colour = "red"
            return response
        elif response == "black" or response == "b":
            response = "black"
            colour = "black"
            return response
        else:
            print(error)

def paritybetfunction(money):
    global newmoney
    global parityvalue
    global parity
    money = newmoney
    yes_no_parity = yes_no("Would you like to place a bet on parity?")
    if yes_no_parity == "yes":
        parityselection("Which would you like to place a bet on? (Odd/Even)")
        parityvalue = betting("How much would you like to bet on {}?".format(parity))
        print("You have placed a bet of ${}.".format(parityvalue))
        money -= parityvalue
        print("Your remaining balance is ${}.".format(money))
        newmoney = money
        return parityvalue and money
    elif yes_no_parity == "no":
        parityvalue = "0"
        parity = "none"
        return parityvalue and parity

def colourbetfunction(money):
    global newmoney
    global colourvalue
    global colour
    money = newmoney
    if newmoney > 0:
        yes_no_colour = yes_no("Would you like to place a bet on colour?")
        if yes_no_colour == "yes":
            colourselection("Which colour would you like to place a bet on? (Red/Black)")
            colourvalue = betting("How much would you like to bet on {}?".format(colour))
            print("You have placed a bet of ${}.".format(colourvalue))
            money -= colourvalue
            print("Your remaining balance is ${}.".format(money))
            newmoney = money
            return colourvalue and money
        if yes_no_colour == "no":
            colourvalue = "0"
            colour = "none"
            return colourvalue and colour

def betting(question):
    error = "You must have enough funds for your bet & type an integer.\n"
    valid = False
    while not valid:
        try:
            # ask the question and remove the $ symbol if the user has entered it
            response = int(input(question).replace('$', ''))
            # if the amount is too low / too high give
            if response <= newmoney and response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def compchoiceprocess():
    global comp_choice
    global colour
    global parity
    global parityvalue
    global money
    global newmoney
    if comp_choice[:1].lower() == colour[:1]:
        print("Your bet on {} was CORRECT! You won ${} back".format(colour, colourvalue*2))
        newmoney += colourvalue*2
    elif comp_choice[:1].lower() == "g":
        print("Green. Your bet (on colour) was incorrect.")
    elif colour == "none":
        print("")
    else:
        print("Your bet on {} was incorrect.".format(colour))

    if parity == "odd":
        if comp_choice[:1].lower() == "g":
            print("Green. Your bet (on parity) was incorrect.")

        elif int(comp_choice[1:]) % 2 != 0:
            print("Your bet on {} was CORRECT! You won ${} back".format(parity, parityvalue*2))
            newmoney += parityvalue*2
        else:
            print("Your bet on {} was incorrect.".format(parity))


    elif parity == "even":
        if comp_choice[:1].lower() == "g":
            print("Your bet (on parity) was incorrect.")


        elif int(comp_choice[1:]) % 2 == 0:
            print("Your bet on {} was CORRECT! You won ${} back".format(parity, parityvalue*2))
            newmoney += parityvalue*2
        else:
            print("Your bet on {} was incorrect.".format(parity))

def final():
    print("You now have: ${}".format(newmoney))
    if newmoney == 0:
        print("You end the game with $0.")
        exit()

# Main Routine
# Below





show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    print("******* INSTRUCTIONS *******\n"
          "Each round a random number (that has a colour) will be chosen.\n\n"
          "You choose if you want to bet on parity. If yes, you will choose\n"
          "which one, and choose how much to bet. (Options are odd or even)\n \n"
          "After parity, you choose if you want to bet on colour. (you can\n"
          "bet on both parity & colour). If yes, you will choose which one,\n"
          "and choose how much to bet. (Options are red or black)\n \n"
          "The computer will generate a random number. If your bet is correct\n"
          "then you will double the money you placed down to bet. If your bet\n"
          "is incorrect, you will lose the money you placed down to bet.\n"
          "If 0 is generated then you will lose the money you bet. 0 is not\n"
          "considered an even number.\n \n"
          "The game ends if you type 'EXIT' when asked if you want to place a \n"
          "bet. The game will also end if you have no money left to bet.\n\n")

budget = budget_que("How much money do you want to budget for this session?", 10, 1000)
print("Your Budget is ${}".format(budget))

money = budget
newmoney = money



 
print("round 1")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("Comp Choice:", comp_choice)
compchoiceprocess()
final()


print("\n round 2")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("Comp Choice:", comp_choice)
compchoiceprocess()

