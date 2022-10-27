def laget():
    names = []
    def teamsPicker(i):
        teamTemp = []
        for x in range (i, len(names), n):
            teamTemp.append(names[x])
        return teamTemp

    #Kolla hur många lag dem vill ha indelade i
    while True:
        try:
            n = int(input("Hur många lag vill du dela in i? "))
        except:
            print("Skriv endast tal tack")
        else:
            break

    #Kolla vem som skall delas in 
    while True:
        name = input("Skriv in n för att dela in i lag eller skriv in namn ")
        if name == "n" and len(names) >= n:
            break
        elif(name == "n"):
            print(f"\nDu måste ha minst {n} namn att dela in och du har {len(names)} namn")
        else:
            names.append(name)

    #Skriv ut lagen
    for p in range(n):
        print(f"Lag {p + 1} består av", end='')
        for x in teamsPicker(p):
            print(" ", x, end='')
        print(" ")
        
