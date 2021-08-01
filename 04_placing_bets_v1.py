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


def colourselection(question):
    error = "Please select red or black."
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "red" or response == "r":
            response == "red"
            return response
        elif response == "black" or response == "b":
            response = "black"
            return response
        else:
            print(error)


def betting(question):
    error = "You must have enough funds for your bet & type an integer.\n"
    valid = False
    while not valid:
        try:
            # ask the question and remove the $ symbol if the user has entered it
            response = int(input(question).replace('$', ''))
            # if the amount is too low / too high give
            if response < budgetcash:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


budgetcash = 50
money = 50
yes_no_parity = yes_no("Would you like to place a bet on parity?")
if yes_no_parity == "yes":
    parity = betting("How much would you like to bet on parity?")
    print(parity)
    money -= parity
print(money)

# round two
yes_no_parity = yes_no("Would you like to place a bet on parity?")
if yes_no_parity == "yes":
    parity = betting("How much would you like to bet on parity?")
    print(parity)
    money -= parity
print(money)

