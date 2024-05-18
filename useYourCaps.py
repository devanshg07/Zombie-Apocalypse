import random

class useYourCaps:

    inputNum = 0
    gameinputNum = 0
    name = ""
    age = 0
    usedCaps = 0
    betCaps = 0
    betNum = 0
    randNum = 0

    @staticmethod
    def playGame():
        while True:
            print("Greetings Humans, it has come to our concern that zombies are taking over mankind!")  # oh no
            print()
            name = input("Enter your name: ")
            nameLen = len(str(name))
            age = int(input("Enter your age: "))

            capCount = 0

            if nameLen > age:
                capCount = random.randint(age, nameLen)

            elif age > nameLen:
                capCount = random.randint(nameLen, age)

            else:
                capCount = age

            leftCaps = capCount

            zombCount = age + random.randint(0, 10)

            print("Oh No " + name + " your life is in danger!")
            print(str(zombCount) + " zombies are after you!!!")

            print("Okay " + name + ", are you going to cook these " + str(zombCount) + " zombies, or let these " + str(zombCount) + " zombies cook you?")
            print(name + ", you have " + str(capCount) + " bottlecaps, each killing one zombie. Will you play to live, or submit defeat?")

            try:
                inputNum = input("Enter 1 to play on, Enter 2 to give up. ")

                if int(inputNum) == 1:
                    print("Long time no talk, " + name + " proud of you for having the will to live.")
                    print()
                    print("What would you like to do?")
                    gameinputNum = input("1. Spend Bottle Caps. 2. Gamble: ")

                    try:
                        if int(gameinputNum) == 1:
                            useYourCaps.spendCaps(capCount)

                        elif int(gameinputNum) == 2:
                            useYourCaps.gamble(capCount)
                        else:
                            print("Invalid choice! Please enter 1 or 2.")

                    except ValueError:
                        print("Invalid input! Please enter a number.")

                elif int(inputNum) == 2:
                    print("Rest in Peace, " + name)
                    break

                else:
                    break

            except Exception as e:
                print("An exception occurred:", e)

    @staticmethod
    def spendCaps(capCount):
        try:
            usedCaps = int(input("How many bottle caps would you like to use? "))
            leftCaps = capCount - usedCaps
            capCount = leftCaps

            if leftCaps <= 0:
                print("Well played, but you have died.")
            else:
                print("You used " + str(usedCaps) + " bottle caps.")
                print("You now have " + str(leftCaps) + " bottle caps left.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    @staticmethod
    def gamble(capCount):
        print("You've chosen to gamble friend, rules are you must enter a whole number, and if it's odd or even similar to the computer you win, or else you lose. ")
        betCaps = int(input("How much are you willing to bet? "))
        betNum = int(input("Enter a whole number: "))

        randNum = random.randint(0, 100)

        if (randNum % 2 == 0 and betNum % 2 == 0) or (randNum % 2 == 1 and betNum % 2 == 1):
            capCount += betCaps
            print("You now have " + str(capCount) + " bottle caps")

        else:
            capCount -= betCaps
            print("You now have " + str(capCount) + " bottle caps")
            if betCaps <= 0:
                print("Well played, but you have died.")

# Run the game
useYourCaps.playGame()
