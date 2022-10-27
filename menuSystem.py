from ast import While
import menuSystemFunctions as ms

while True:
    answer = int(input("""
    Skriv 1 för att dela in i lag
    Skriv 2 för att kolla vad pappegojan polly vill
    Skriv 3 för att kolla vilket Harry Potter elevhem du hamnar i
    Skriv 4 för att spela alien
    skriv 5 för att avsluta programmet
    """))
    if answer == 1:
        ms.laget()
    elif answer == 2:
        ms.polly
    elif answer == 3:
        ms.harryPotter
    elif answer == 4:
        ms.alien
    elif answer == 5:
        break


    
