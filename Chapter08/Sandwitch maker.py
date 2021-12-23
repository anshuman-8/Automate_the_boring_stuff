import pyinputplus as inp

print("We are going to make a Sandwitch !!!")

bread=inp.inputMenu(["wheat","white","sourdough"])

protein=inp.inputMenu(["chicken","ham","turkey","tofu"])

cheese=inp.inputYesNo("Do you want cheese?")

if cheese=="Yes":
    ctype=inp.inputMenu(["mozzarella","Swiss","cheddar"])

sause=inp.inputYesNo("Do you want mayo, mustard, lettuce, or tomato.")

numb=inp.inputInt("How many sandwitch do you want?", min=1)
