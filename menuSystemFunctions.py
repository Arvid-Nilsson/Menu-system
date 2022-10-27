#laget! minigame
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
        
#Pappegojan polly minigamegit
def polly():
    import random
    seads = ""
    preference = ""
    
    while True:
        try:
            temperature = float(input("Hur varmt är det idag? "))
        except:
            print("Skriv endast tal tack")
        else:
            break

    weather = input("Vad är det för väder idag ").lower()
    while "inte" in weather:
        weather = input("Skriv inte \u0022inte\u0022 \nVad är det för väder idag ").lower()

    if temperature < 0 or "snö" in weather:
        seads = str(random.randint(1, 25)) + " frön"
    elif temperature > 20 and "sol" in weather:
        seads = "5 frön"
        preference = "en rolig historia"
    elif temperature < 20 and not("regn" in weather):
        seads = "10 frön"
        preference = "och en sång om livet på havet"
    elif temperature == 20 or "blås" in weather:
        seads = "\b\b\binte äta"
        preference = "men hen vill att du skal sätta på radion"
    else:
        seads = "\b\b\binte uppleva detta vädret"

    print(f"polly vill ha {seads} {preference} \u2665")

#Harry potter house mini game
def harryPotter():
    import random
    sum = 0
    house = ""
    randomHouse = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    #Check so that the sum of the traits is greater than 10
    while sum <= 10:
        brave = int(input("Hur modig är du på en skala av 1 till 10? "))
        astute = int(input("Hur slug är du på en skala av 1 till 10? "))
        patience = int(input("Hur tålmodig är du på en skala av 1 till 10? "))
        sensible = int(input("Hr förnuftig är du på en skala av 1 till 10? "))
        houseList = [brave, astute, patience, sensible]
        sum = brave + astute + patience + sensible

    #finds largest number in list
    indexLargestNumber = houseList.index(max(houseList))

    if brave >= 8 and astute <= 3:
        house += "Gryffindor"
        print(f"Ditt elevhem är {house} \nGrattis!")
    elif astute >= 8 and brave <= 3:
        house += "Slytherin"
        print(f"Ditt elevhem är {house} \nGrattis!")
    elif patience >= 8 and sensible <= 3:
        house += "Hufflepuff"
        print(f"Ditt elevhem är {house} \nGrattis!")
    elif sensible >= 8 and patience <= 3:
        house += "Ravenclaw"
        print(f"Ditt elevhem är {house} \nGrattis!")
    elif houseList[indexLargestNumber] <= 7 and houseList[indexLargestNumber] >= 4:
        #find string from list by index
        print(f"Ditt elevhem är {randomHouse[indexLargestNumber]} \nGrattis")
    else: 
        house += random.choice(randomHouse)
        print(f"Ditt elevhem är {house} \nGrattis!")

#Alien minigame
def alien():
    Alien = str(input("Vilken färg är din Alien ")).lower()
    poäng = 0
    if (Alien == "rosa"):
        poäng += 15
    elif (Alien == "blå"):
        poäng += 10
    elif (Alien == "gul"):
        poäng += 5
    print("Du har ",poäng," poäng") 





        