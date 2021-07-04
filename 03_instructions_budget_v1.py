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
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response
                valid = True
            else:
                print(error)

        except ValueError:
            print(error)



# Main Routine
#
# Below

show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    print("instructions")

budget = budget_que("How much money do you want to budget for this session?", 10, 1000)
print("Your Budget is ${}".format(budget))




