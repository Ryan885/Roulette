# ask user if they have played before
show_instructions = input("Have you played before? ")

# if yes, output 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    show_instructions = "yes"
    print("program continues")

# if no, output 'display instructions'
elif show_instructions == "no" or show_instructions == "n":
    show_instructions = "no"
    print("Display Instructions")

else:
    print("Input Error. Answer Yes / No")

print("You chose {}".format(show_instructions))

