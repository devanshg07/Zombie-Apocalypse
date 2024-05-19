import random

class useYourCaps:

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

            zombCount = age + random.randint(0, 10)

            print("Oh No " + name + " your life is in danger!")
            print(str(zombCount) + " zombies are after you!!!")

            print("Okay " + name + ", are you going to cook these " + str(zombCount) + " zombies, or let these " + str(zombCount) + " zombies cook you?")
            print(name + ", you have " + str(capCount) + " bottlecaps, each killing one zombie. Will you play to live, or submit defeat?")

            try:
                inputNum = input("Enter 1 to play on, Enter 2 to give up: ")

                if int(inputNum) == 1:
                    print("Long time no talk, " + name + " proud of you for having the will to live.")
                    print()

                    while zombCount > 0 and capCount > 0:
                        capCount, zombCount = useYourCaps.chooseOption(capCount, name, zombCount)

                        if zombCount <= 0:
                            print("Congrats on surviving.")
                            break

                        if capCount <= 0:
                            print("Well played, but you have died.")
                            break

                elif int(inputNum) == 2:
                    print("Rest in Peace, " + name)
                    break

                else:
                    print("Invalid choice! Please enter 1 or 2.")

            except Exception as e:
                print("An exception occurred:", e)

            if not useYourCaps.playAgain():
                break

    @staticmethod
    def chooseOption(capCount, name, zombCount):
        gameinputNum = input("1. Spend Bottle Caps. 2. Gamble: ")

        try:
            if int(gameinputNum) == 1:
                zombCount = useYourCaps.spendCaps(capCount, zombCount)

            elif int(gameinputNum) == 2:
                capCount = useYourCaps.gamble(capCount)

            else:
                print("Invalid choice! Please enter 1 or 2.")

        except ValueError:
            print("Invalid input! Please enter a number.")
        
        return capCount, zombCount

    @staticmethod
    def spendCaps(capCount, zombCount):
        try:
            usedCaps = int(input("How many bottle caps would you like to use? "))
            leftCaps = capCount - usedCaps
            zombKilled = usedCaps
            zombCount -= zombKilled

            if zombCount <= 0:
                zombCount = 0

            if leftCaps <= 0:
                leftCaps = 0

            print("You used " + str(usedCaps) + " bottle caps.")
            print("You now have " + str(leftCaps) + " bottle caps left.")
            print("You have killed " + str(zombKilled) + " zombies, " + str(zombCount) + " are still alive.")

            return zombCount

        except ValueError:
            print("Invalid input! Please enter a number.")
            return zombCount

    @staticmethod
    def gamble(capCount):
        print("You've chosen to gamble friend, rules are you must enter a whole number, and if it's odd or even similar to the computer you win, or else you lose.")
        try:
            betCaps = int(input("How much are you willing to bet? "))
            betNum = int(input("Enter a whole number: "))

            randNum = random.randint(0, 100)

            if (randNum % 2 == 0 and betNum % 2 == 0) or (randNum % 2 == 1 and betNum % 2 == 1):
                capCount += betCaps
                print("You now have " + str(capCount) + " bottle caps")

            else:
                capCount -= betCaps
                print("You now have " + str(capCount) + " bottle caps")

                if capCount <= 0:
                    capCount = 0

        except ValueError:
            print("Invalid input! Please enter a number.")

        return capCount

    @staticmethod
    def playAgain():
        playAgainInput = input("Would you like to play again? Y for Yes, N for No: ")

        if str(playAgainInput).upper() == "Y":
            return True
        
        elif str(playAgainInput).upper() == "N":
            return False
        
        else:
            print("Invalid input! Please enter Y or N.")
            return useYourCaps.playAgain()

# Run the game
useYourCaps.playGame()
