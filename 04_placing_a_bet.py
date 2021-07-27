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

def betting(question):
    error = "You must have enough funds for your bet.\n"
    valid = False
    while not valid:
        try:
            # ask the question and remove the $ symbol if the user has entered it
            response = int(input(question).replace('$', ''))
            # if the amount is too low / too high give
            if response < money:
                return response
            else:
                print(error)

        except ValueError:
            print(error)




# Main Routine Below

money = 50
show_instructions = yes_no("Would you like to place a bet on parity?")
if show_instructions == "yes":
    parity = betting("How much would you like to bet on parity?")
    print(parity)
