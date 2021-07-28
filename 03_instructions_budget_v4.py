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

        else:
            print("Please answer yes / no")
        # neither


# If [0] is $ then remove


def budget_que(question, low, high):
    error = "Your Budget should be a whole number between $10 and $1000\n"
    valid = False
    while not valid:
        try:
            # ask the question and remove the $ symbol if the user has entered it
            response = int(input(question).replace('$', ''))
            # if the amount is too low / too high give
            if low < response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)



# Main Routine
#
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
