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
        
#Pappegojan polly minigame
def polly():
    from encodings import utf_8
    import random
    chr = utf_8
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