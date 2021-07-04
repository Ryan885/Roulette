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

# Main Routine
#
# Below


show_instructions = yes_no("Have you played the game before? ")
if show_instructions == "no":
    print("instructions")

# If [0] is $ then remove

budget = input("How much is your budget for this session? (between $10 and $1000)")
print("Your Budget is ${}".format(budget))


