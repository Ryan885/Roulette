import random

#comment code uh anyway compile
from typing import Any, Union

parityvalue = 0
colourvalue = 0
parity = ""
colour = ""

# list of possible places the ball could land or computer could generate
ball_results = ["G0", "R1", "B2", "R3", "B4", "R5", "B6", "B7", "R8", "B9", "R10", "B11", "R12", "R13", "B14", "R15", "B16", "R17", "B18", "B19", "R20", "B21", "R22", "B23", "R24", "G25"]




# Functions

# Basic function for yes/no questions
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
            print("You end the game with ${}. You started with ${}".format(newmoney, budget))
            exit()
            # Users can exit/leave the game when they want when asked a yes/no question e.g.
            # at the start of round 4 after made $20, when asked if they want to make a bet on parity
            # they can also choose to quit.
        else:
            print("Please answer yes / no")
        # no correct answers given (yes/no/quit)

# Budget Question. Asks the user how much they want to budget for the game
def budget_que(question, low, high):
    error = "Your Budget should be a whole number/integer between $10 and $1000\n"
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
            # if the amount is lower than $10 or higher than $1000
        except ValueError:
            print(error)
            # error printed when the user enters e.g. "Twenty Dollars" instead of 20/$20.

# selection of the bet being on either odd or even (parity)
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
            # response to odd
        elif response == "even" or response == "e":
            response = "even"
            parity = "even"
            return response
            # response to even
        else:
            print(error)
            # no correct response given (odd/o or even/e)

# selection of the bet being on either red or black (colour)
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
            # response to red
        elif response == "black" or response == "b":
            response = "black"
            colour = "black"
            return response
            # response to black
        else:
            print(error)
            # no correct response given (red/r or black/b)

# parity bet function asks the user if they would like to bet on parity, and goes through the process
# of betting on parity. if the user says no, parity is given the value "none"
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
        print("Your remaining balance is ${}. \n".format(money))
        newmoney = money
        return parityvalue and money
        # if the user does make a bet on parity
    elif yes_no_parity == "no":
        parityvalue = "0"
        parity = "none"
        return parityvalue and parity
        # if the user does not make a bet on parity

def colourbetfunction(money):
    global newmoney
    global colourvalue
    global colour
    money = newmoney
    # if/else statement only asks the user if they want to place a bet on colour if 'newmoney' > 0
    # so they cannot say yes and get stuck in a loop unable to answer a 'correct' variable.
    if newmoney > 0:
        yes_no_colour = yes_no("Would you like to place a bet on colour?")
        if yes_no_colour == "yes":
            colourselection("Which colour would you like to place a bet on? (Red/Black)")
            colourvalue = betting("How much would you like to bet on {}?".format(colour))
            print("You have placed a bet of ${}.".format(colourvalue))
            money -= colourvalue
            print("Your remaining balance is ${}. \n".format(money))
            newmoney = money
            return colourvalue and money
            # if the user does make a bet on colour
        if yes_no_colour == "no":
            colourvalue = "0"
            colour = "none"
            return colourvalue and colour
            # if the user does make a bet on colour
    else:
        colour = "none"
        # else occurs when newmoney = $0 (all money has been bet on parity)

# basic betting function for when a user is asked how much money the want to bet.
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
                # error message when the bet exceeds funds, the bet is $0 or the bet is a negative number.

        except ValueError:
            print(error)
            # error printed when the user enters e.g. "Twenty Dollars" instead of 20/$20.

# process of working out whether the computer choice is the same as the user choice
# and what happens when it is / is not.
def compchoiceprocess():
    global comp_choice
    global colour
    global parity
    global parityvalue
    global money
    global newmoney

    # computer choice process for finding if the computer generated colour is the same as the user bet on (or did not bet on)
    if comp_choice[:1].lower() == colour[:1]:
        print("\x1b[1;39;42m Your bet on {} was CORRECT! You won ${} back \033[0;0m".format(colour, colourvalue*2))
        newmoney += colourvalue*2
        # response to computer colour being the same as user colour. They receive double what they bet.
    elif comp_choice[:1].lower() == "g":
        print("\033[1;30;41m Green. Your bet (on colour) was incorrect. \033[0;0m")
        # response to colour being green
    elif colour == "none":
        print("")
        # response to no colour being bet on
    else:
        print("\033[1;30;41m Your bet on {} was incorrect. \033[0;0m".format(colour))
        # response to else (e.g. the computer generated colour being red when user choice is black)

    # computer choice process for finding if the computer generated colour is the same as the user bet on (or did not bet on)
    if parity == "odd":
        # if parity is odd then
        if comp_choice[:1].lower() == "g":
            print("\033[1;30;41m Green. Your bet (on parity) was incorrect. \033[0;0m")
            # response to colour being green
        elif int(comp_choice[1:]) % 2 != 0:
            print("\x1b[1;39;42m Your bet on {} was CORRECT! You won ${} back \033[0;0m".format(parity, parityvalue*2))
            newmoney += parityvalue*2
            # response to computer choice parity being odd. User receives double their bet back
        else:
            print("\033[1;30;41m Your bet on {} was incorrect. \033[0;0m".format(parity))
            # response to else (when the comp choice number % 2 = 0, showing it is even)


    elif parity == "even":
        # else if parity is even then
        if comp_choice[:1].lower() == "g":
            print("\033[1;30;41m Your bet (on parity) was incorrect. \033[0;0m")
            # response to colour being green
        elif int(comp_choice[1:]) % 2 == 0:
            print("\x1b[1;39;42m Your bet on {} was CORRECT! You won ${} back \033[0;0m".format(parity, parityvalue*2))
            newmoney += parityvalue*2
            # response to parity being even. User receives double their bet back
        else:
            print("\033[1;30;41m Your bet on {} was incorrect. \033[0;0m".format(parity))
            # response to else (when the comp choice number % 2 does not = to 0)

    # final balance for the turn printed.
    print("\033[1;30;47m You now have: ${} \033[0;0m".format(newmoney))

    # checks to see if the balance is 0, if so the game ends.
    if newmoney == 0:
        print("\033[1;30;47m You end the game with $0. \033[0;0m")
        exit()



# Main Routine Below

# Asks the User if they have played the game.
show_instructions = yes_no("Have you played the game before?")
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
    # instructions if the user has not played the game before

# Asks the user how much money they would like to budget for the session & prints the budget.
budget = budget_que("How much money do you want to budget for this session?", 10, 1000)
print("Your Budget is ${} \n".format(budget))

# variables relating to money
money = budget
newmoney = money

# Round 1
print("\033[1;30;47m round 1 \033[0;0m")
# process for a parity bet
paritybetfunction(newmoney)
# process for a colour bet
colourbetfunction(newmoney)
# a random computer choice from the list is generated
comp_choice: Union[str, Any] = random.choice(ball_results)
# the computer choice is printed
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
# the process for what the program does with the computer choice (e.g. wins back money, ends game with $0, etc).
compchoiceprocess()



print("\n \033[1;30;47m round 2 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 3 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 4 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 5 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 6 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 7 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 8 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 9 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()


print("\n \033[1;30;47m round 10 \033[0;0m")
paritybetfunction(newmoney)
colourbetfunction(newmoney)
comp_choice: Union[str, Any] = random.choice(ball_results)
print("\x1b[1;31;40m Comp Choice:", comp_choice, "\033[0;0m")
compchoiceprocess()
# after 10 round the game ends
print("You end the game with ${}. You started with ${}".format(newmoney, budget))
exit()
