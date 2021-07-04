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

# Main Routine Below


show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))
having_fun = yes_no("Are you having fun")
print("You said {} to having fun.".format(having_fun))
