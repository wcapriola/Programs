print("Welcome to BET IT ALL! A two player game where you need to take risks to get more money. There are three stages to BET IT ALL! In each the risk and reward goes up. Get ready to take chances. Get ready to loose some. And get ready to WIN!")
pOne = 20
pTwo = 20
import random

#player ONE first turn:
while pOne > 0:
    pOne = str(pOne)
    print("Player One, you have " + pOne + " dollars. Will you gamble? (yes/no)")
    if input() == 'yes':
        number = random.randint(1, 2)
        print("Pick a number, 1 or 2 to put your money on. You have a 50/50 chance of doubling your money!")
        guess = input()
        guess = int(guess)
        
        print("Now, you have " + pOne + " dollars. How much will you gamble?")
        gamble = input()
        gamble = int(gamble)
        pOne = int(pOne)
        if gamble > pOne:
            pOne = str(pOne)
            print("You don't have that much money. Try again.")
            print("Now, you have " + pOne + " dollars. How much will you gamble?")
            gamble = input()
            pOne = int(pOne)
            gamble = int(gamble)
            if gamble > pOne:
                print("You don't have that much. Onto player two.")
                break
            else:
                gamble = int(gamble)
                pOne = pOne - gamble
        else:
            gamble = int(gamble)
            pOne = pOne - gamble

        if guess == number:
            pOne = pOne + (gamble* 2)
            print("Yea! That was right. The money you gambled just doubled!")
        if guess != number:
            print("Nope. Sorry, you just lost the money that you gambled.")

    else:
        print("Okay. Onto player two.")
        break

pOne = int(pOne)
if pOne <= 0:
    print("PLAYER TWO WINS! Player one is out of money.")


#player TWO first turn:
while pTwo > 0:
    pTwo = str(pTwo)
    print("Player Two, you have " + pTwo + " dollars. Will you gamble? (yes/no)")
    if input() == 'yes':
        number = random.randint(1, 2)
        print("Pick a number, 1 or 2 to put your money on. You have a 50/50 chance of doubling your money!")
        guess = input()
        guess = int(guess)
        
        print("Now, you have " + pTwo + " dollars. How much will you gamble?")
        gamble = input()
        gamble = int(gamble)
        pTwo = int(pTwo)
        if gamble > pTwo:
            pTwo = str(pTwo)
            print("You don't have that much money. Try again.")
            print("Now, you have " + pTwo + " dollars. How much will you gamble?")
            gamble = input()
            pTwo = int(Two)
            gamble = int(gamble)
            if gamble > pTwo:
                print("You don't have that much. Onto round two.")
                break
            else:
                gamble = int(gamble)
                pTwo = pTwo - gamble
        else:
            gamble = int(gamble)
            pTwo = pTwo - gamble

        if guess == number:
            pTwo = pTwo + (gamble* 2)
            print("Yea! That was right. The money you gambled just doubled!")
        if guess != number:
            print("Nope. Sorry, you just lost the money that you gambled.")

    else:
        print("Okay. Onto round two.")
        break
pTwo = int(pTwo)
if pTwo <= 0:
    print("PLAYER ONE WINS! Player two is out of money.")

#End of round one
print("Round one is over. Let's see who is in the lead!")
pOne = str(pOne)
pTwo = str(pTwo)
print("Player one has " + pOne + " dollars! Player two has " + pTwo + " dollars! Get ready for round two! The risk is higher, but you can triple your money!")
pOne = int(pOne)
pTwo = int(pTwo)




#Player ONE round two

while pOne > 0:
    pOne = str(pOne)
    print("Player One, you have " + pOne + " dollars. Will you gamble? (yes/no)")
    if input() == 'yes':
        number = random.randint(1, 3)
        print("Pick a number, 1 - 3 to put your money on. You have a 1/3 chance of tripling your money!")
        guess = input()
        guess = int(guess)
        
        print("Now, you have " + pOne + " dollars. How much will you gamble?")
        gamble = input()
        gamble = int(gamble)
        pOne = int(pOne)
        if gamble > pOne:
            pOne = str(pOne)
            print("You don't have that much money. Try again.")
            print("Now, you have " + pOne + " dollars. How much will you gamble?")
            gamble = input()
            pOne = int(pOne)
            gamble = int(gamble)
            if gamble > pOne:
                print("You don't have that much. Onto player two.")
                break
            else:
                gamble = int(gamble)
                pOne = pOne - gamble
        else:
            gamble = int(gamble)
            pOne = pOne - gamble

        if guess == number:
            pOne = pOne + (gamble* 3)
            print("Yea! That was right. The money you gambled just tripled!")
        if guess != number:
            print("Nope. Sorry, you just lost the money that you gambled.")

    else:
        print("Okay. Onto player two.")
        break

pOne = int(pOne)
if pOne <= 0:
    print("PLAYER TWO WINS! Player one is out of money.")



#Player TWO round two
while pTwo > 0:
    pTwo = str(pTwo)
    print("Player Two, you have " + pTwo + " dollars. Will you gamble? (yes/no)")
    if input() == 'yes':
        number = random.randint(1, 3)
        print("Pick a number, 1-3 to put your money on. You have a 1/3 chance of tripling your money!")
        guess = input()
        guess = int(guess)
        
        print("Now, you have " + pTwo + " dollars. How much will you gamble?")
        gamble = input()
        gamble = int(gamble)
        pTwo = int(pTwo)
        if gamble > pTwo:
            pTwo = str(pTwo)
            print("You don't have that much money. Try again.")
            print("Now, you have " + pTwo + " dollars. How much will you gamble?")
            gamble = input()
            pTwo = int(Two)
            gamble = int(gamble)
            if gamble > pTwo:
                print("You don't have that much. Onto round three.")
                break
            else:
                gamble = int(gamble)
                pTwo = pTwo - gamble
        else:
            gamble = int(gamble)
            pTwo = pTwo - gamble

        if guess == number:
            pTwo = pTwo + (gamble* 3)
            print("Yea! That was right. The money you gambled just tripled!")
        if guess != number:
            print("Nope. Sorry, you just lost the money that you gambled.")

    else:
        print("Okay. Onto round three.")
        break
pTwo = int(pTwo)
if pTwo <= 0:
    print("PLAYER ONE WINS! Player two is out of money.")

#end of round two
print("Round two is over. Let's see who is in the lead!")
pOne = str(pOne)
pTwo = str(pTwo)
print("Player one has " + pOne + " dollars! Player two has " + pTwo + " dollars! Get ready for final round three! The risk is higher, but you can QUADRUPLE your money!")
pOne = int(pOne)
pTwo = int(pTwo)



#player ONE round three:
while pOne > 0:
    pOne = str(pOne)
    print("Player One, you have " + pOne + " dollars. Will you gamble? (yes/no)")
    if input() == 'yes':
        number = random.randint(1, 4)
        print("Pick a number, 1 - 4 to put your money on. You have a 1/4 chance of QUADRUPLING your money!")
        guess = input()
        guess = int(guess)
        
        print("Now, you have " + pOne + " dollars. How much will you gamble?")
        gamble = input()
        gamble = int(gamble)
        pOne = int(pOne)
        if gamble > pOne:
            pOne = str(pOne)
            print("You don't have that much money. Try again.")
            print("Now, you have " + pOne + " dollars. How much will you gamble?")
            gamble = input()
            pOne = int(pOne)
            gamble = int(gamble)
            if gamble > pOne:
                print("You don't have that much. Onto player two.")
                break
            else:
                gamble = int(gamble)
                pOne = pOne - gamble
        else:
            gamble = int(gamble)
            pOne = pOne - gamble

        if guess == number:
            pOne = pOne + (gamble* 4)
            print("Yea! That was right. The money you gambled just QUADRUPLED!")
        if guess != number:
            print("Nope. Sorry, you just lost the money that you gambled.")

    else:
        print("Okay. Onto player two.")
        break

pOne = int(pOne)
if pOne <= 0:
    print("PLAYER TWO WINS! Player one is out of money.")




#player TWO round three:
while pTwo > 0:
    pTwo = str(pTwo)
    print("Player Two, you have " + pTwo + " dollars. Will you gamble? (yes/no)")
    if input() == 'yes':
        number = random.randint(1, 4)
        print("Pick a number, 1-4 to put your money on. You have a 1/4 chance of QUADRUPLING your money!")
        guess = input()
        guess = int(guess)
        
        print("Now, you have " + pTwo + " dollars. How much will you gamble?")
        gamble = input()
        gamble = int(gamble)
        pTwo = int(pTwo)
        if gamble > pTwo:
            pTwo = str(pTwo)
            print("You don't have that much money. Try again.")
            print("Now, you have " + pTwo + " dollars. How much will you gamble?")
            gamble = input()
            pTwo = int(Two)
            gamble = int(gamble)
            if gamble > pTwo:
                print("You don't have that much. Onto the score check.")
                break
            else:
                gamble = int(gamble)
                pTwo = pTwo - gamble
        else:
            gamble = int(gamble)
            pTwo = pTwo - gamble

        if guess == number:
            pTwo = pTwo + (gamble* 4)
            print("Yea! That was right. The money you gambled just QUADRUPLED!")
        if guess != number:
            print("Nope. Sorry, you just lost the money that you gambled.")

    else:
        print("Okay. Onto the score check!.")
        break



#score check:
pOne = str(pOne)
print("OKAY! It's time to see the scores! Who will win?")
pOne = str(pOne)
pTwo = str(pTwo)
print("Player one has " + pOne + "! Player two has " + pTwo + "!")
pOne = int(pOne)
pTwo = int(pTwo)
if pOne > pTwo:
    print("Player one WINS BET IT ALL!")
    print("Okay, player one. Let's see what medal you made.")
    print("10- BRONZE, 27- SILVER, 52- GOLD, 111- PLATINUM, 502- ULTRAPLATINUMDIMONDTHING!")
if pTwo > pOne:
    print("Player two WINS BET IT ALL!")
    print("Okay, player two. Let's see what medal you made.")
    print("10- BRONZE, 27- SILVER, 52- GOLD, 111- PLATINUM, 502- ULTRAPLATINUMDIMONDTHING!")
if pTwo == pOne:
    print("Players one and two TIE BET IT ALL!")
    print("Okay, players. Let's see what medal you made.")
    print("10- BRONZE, 27- SILVER, 52- GOLD, 111- PLATINUM, 502- ULTRAPLATINUMDIMONDTHING!")
print("Thanks for playing")










        
    
