from ast import While
import menuSystemFunctions as ms
loopActive = True

def playAgain():
    global loopActive
    playAgain = input("Do you want to go back to menu? (y/n) ")
    if "y" in playAgain:
        pass
    else:
        loopActive = False
        

while loopActive:
    answer = int(input("""
Skriv 1 för att dela in i lag
Skriv 2 för att kolla vad pappegojan polly vill
Skriv 3 för att kolla vilket Harry Potter elevhem du hamnar i
Skriv 4 för att spela alien
skriv 5 för att avsluta programmet
"""))
    if answer == 1:
        ms.laget()
        playAgain()
    elif answer == 2:
        ms.polly
        playAgain()
    elif answer == 3:
        ms.harryPotter
        playAgain()
    elif answer == 4:
        ms.alien
        playAgain()
    elif answer == 5:
        break


    
