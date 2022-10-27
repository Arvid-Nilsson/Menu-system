import menuSystemFunctions as minigame

loopActive = True

def playAgain():
    global loopActive
    playAgain = input("\nDo you want to go back to menu or quit? (y/n) ")
    if "y" in playAgain:
        pass
    else:
        loopActive = False

#pick minigame
while loopActive:
    answer = int(input("""
Skriv 1 för att dela in i lag
Skriv 2 för att kolla vad pappegojan polly vill ha
Skriv 3 för att kolla vilket Harry Potter elevhem du hamnar i
Skriv 4 för att spela alien
Skriv 5 för att avsluta programmet
"""))
    print("")
    if answer == 1:
        minigame.laget()
        playAgain()
    elif answer == 2:
        minigame.polly()
        playAgain()
    elif answer == 3:
        minigame.harryPotter()
        playAgain()
    elif answer == 4:
        minigame.alien()
        playAgain()
    elif answer == 5:
        break

print("Tack för att du spelat!")


    
