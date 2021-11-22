import random
parity = "odd"
colour = "red"
money = 50
newmoney = money
betting = 20
ball_results = ["G0", "R1", "B2", "R3", "B4", "R5", "B6", "B7", "R8", "B9", "R10", "B11", "R12", "R13", "B14", "R15", "B16", "R17", "B18", "B19", "R20", "B21", "R22", "B23", "R24", "G25"]


comp_choice = random.choice(ball_results)
print("Comp Choice:", comp_choice)

if comp_choice[:1].lower() == colour[:1]:
    print("Your bet on {} was CORRECT!".format(colour))
elif comp_choice[:1].lower() == "g":
    print("Green.")
else:
    print("Your bet on {} was incorrect.".format(colour))

if parity == "odd":
    if comp_choice[:1].lower() == "g":
        print("You lost all bets.")

    elif int(comp_choice[1:]) % 2 != 0:
        print("Your bet on {} was CORRECT!".format(parity))
    else:
        print("Your bet on {} was incorrect.".format(parity))
