import random
import datetime
def Game(): 
 try:
    print("-------------------- ROCK,PAPPER,SCISSORS GAME -----------")
    Computer_choice = random.choice(["rock","papper","scissors"]).lower()
    while True:
        userchoice = input("Entire Your Choice or q to Quit ?:").lower().strip()
        contain = ["rock","papper","scissors"]
        if userchoice == "":
            print("Choose A choice ?!")
            continue
        elif userchoice == "q":
            if datetime.datetime.now().strftime("%p") == "AM":
                print("Have Nice Day ==>")
                break
            else:
                print("Have Nice Night ==>")
            break
        elif userchoice.isnumeric():
            print("Only String Is Allowed")
            continue
        if userchoice not in contain:
            print(f"{contain[0],contain[1],contain[2]} Only Is Allowed ",end="")
            print()
            continue
        if Computer_choice == contain[0]  and userchoice == contain[0]:
            print(F"Computer's Choice Is : 🪨  {Computer_choice} And Your Choice Is : 🪨   {userchoice}")
            print("It's Equal 🟰")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[1] and userchoice == contain[1]:
            print(F"Computer's Choice Is : 📄 {Computer_choice} And Your Choice Is : 📄 {userchoice}")
            print("It's Equal 🟰 ")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[2] and userchoice == contain[2]:
            print(F"Computer's Choice Is : ✂️  {Computer_choice} And Your Choice Is : ✂️  {userchoice}")
            print("It's Equal 🟰 ")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[0] and userchoice == contain[1]:
            print(F"Computer's Choice Is : 🪨   {Computer_choice} And Your Choice Is : 📄 {userchoice}")
            print("You Win 🏆")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[1]  and userchoice == contain[0]:
            print(F"Computer's Choice Is : 📄 {Computer_choice} And Your Choice Is : 🪨  {userchoice}")
            print("Computer Win 🖥️")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[1]  and userchoice == contain[2]:
            print(F"Computer's Choice Is : 📄  {Computer_choice} And Your Choice Is : ✂️  {userchoice}")
            print("You Win 🏆")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[2] and userchoice == contain[1]:
            print(F"Computer's Choice Is : ✂️  {Computer_choice} And Your Choice Is : 📄  {userchoice}")
            print("Computer Win 🖥️")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[2] and userchoice == contain[1]:
            print(F"Computer's Choice Is : ✂️  {Computer_choice} And Your Choice Is : 📄 {userchoice}")
            print("Computer Win 🖥️")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[0] and userchoice == contain[2]:
            print(F"Computer's Choice Is : 🪨  {Computer_choice} And Your Choice Is : ✂️  {userchoice}")
            print("Computer Win 🖥️")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
        if Computer_choice == contain[2] and userchoice == contain[0]:
            print(F"Computer's Choice Is : ✂️  {Computer_choice} And Your Choice Is : 🪨  {userchoice}")
            print("You Win 🏆")
            Computer_choice = random.choice(["rock","papper","scissors"]).lower()
            continue
 except KeyboardInterrupt as intrupts:
     print()
     print(f"Error : {intrupts} Don't push Ctrl + C If You Want To Quit Use \" Q \" Button.")
     Game()



if __name__ == "__main__":
    Game()

