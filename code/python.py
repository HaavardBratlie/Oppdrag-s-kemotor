import msvcrt  #trenger denne for at get keypress skal fungere
import os  #trenger denne for at console clear skal fungere
 
def console_clear():                     #console clear fjerner alt som er i konsollen/terminalen helt frem til der den står i koden.
    os.system('cls' if os.name == 'nt' else 'clear')
 
def get_keypress():         #get keypress gjør at man bare trenger å taste en tast en gang i steden for å måtte trykke enter etter du trykker den
    return msvcrt.getch().decode('utf-8')            #jeg har ikke brukt get keypress siden det gjør det vanskelig for meg å bruke "exit" komandoen jeg har i denne koden
                                                                                 #jeg kunne ha endret den til f.eks. trykk 0 for å gå tilbake, men valgte heller å beholde den.
def lesInnTekst(filnavn):               #denne funksjonen henter og lagrer all teksten fra tekstfil1.txt hvis den ikke finner filen returnerer den "filen ble ikke funnet"
    try:
        with open(filnavn, 'r', encoding='utf-8') as fil:
            return fil.readlines()
    except FileNotFoundError:
        print("Filen ble ikke funnet.")
        return []

def printMeny():       #hovedmeny. dette er stedet du kommer når programmet starter.
    console_clear()   #brukt console clear. gjør så bare menyen viser i konsollen
    print("--------- Søkemotor ---------")
    print("| 1. Print ord              |")
    print("| 2. Finn ord               |")
    print("| 3. Finn linje med ord     |")
    print("| 4. Tell antall ord        |")
    print("| 5. Avslutt                |")
    print("-----------------------------")

def menyOrd():          #dette er den andre menyen. menyen som ligger etter "1. print ord" i hoved menyen.
    console_clear()     #i denne kan man velge om man vil printe første gang ordet står eller alle gangene.
    print("------------- Print Ord -------------")
    print("| 1. Print første gangen ordet står |")
    print("| 2. Print alle gangene ordet står  |")
    print("| 3. Tilbake til menyen             |")
    print("-------------------------------------")
    valg = input("Velg et alternativ: ")
    gjoermenyvalg(valg)

def menyLinje():      #denne menyen er lignene som den over. den er bare for "3. finn linje med ord" istedenfor.
    console_clear()   # du kan velge om du vil printe den første linja ordet står på eller alle linjene ordet står på.
    print("------------ Antall Linjer ------------")
    print("| 1. Print første linjen ordet står   |")
    print("| 2. Print alle linjene ordet står    |")
    print("| 3. Tilbake til menyen               |")
    print("---------------------------------------")
    valg2 = input("Velg et alternativ: ")
    linjemenyvalg(valg2)

def utfoerMenyvalg(valgtTall, tekstliste):      #denne funksjonen er for første menyen. 
    if valgtTall == "1":
        menyOrd()   #når man velger 1 kommer man til menyOrd() slik at man kan velge videre
        valg = input("Velg et alternativ: ") 
        gjoermenyvalg(valg)
    elif valgtTall == "2":
        test = True          #hvis man velger 2 får man denne inputten.
        while test == True:  #alle valgene har denne biten med kode. 1 og 3 har den i selve funksjonen og ikke her siden de går via en annen meny
            ord = input("Skriv inn et ord for å finne ut om det står i teksten: ")
            if ord == "exit":  #denne biten med kode stiller spørsmålet og kjører funksjonen hvis man ikke skriver exit. hvis man skriver exit går man til menyen.
                return
            finnOrd(ord, tekstliste)
    elif valgtTall == "3":
        menyLinje()  #kjører menyLinje. viderefører bruker
        valg2 = input("Velg et alternativ: ")
        linjemenyvalg(valg2)
    elif valgtTall == "4":
        test = True
        while test == True:
            ord = input("Skriv inn et ord for å finne ut hvor mange ganger det står: ")
            if ord == "exit":
                return
            tellOrd(ord, tekstliste)
    elif valgtTall == "5":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N: ")
        if bekreftelse.lower() == "j":
            exit()
        else:
            printMeny()
            menyvalg = input("Velg et alternativ: ")
            utfoerMenyvalg(menyvalg, tekstliste)
    else:
        print("Ugyldig valg. Velg et tall mellom 1-5.")
        printMeny()
        menyvalg = input("Velg et alternativ: ")
        utfoerMenyvalg(menyvalg, tekstliste)



def gjoermenyvalg(tall):   #denne koden er for menyOrd altså 1 i den originale menyen. den fungerer på samme måte som "utfoerMenyvalg" men for en annen meny.
    if tall == "1":
        test = True          #her er den kodesnutten som var på 2 og 4 i "utfoerMenyvalg".
        while test == True:
            ord = input("Skriv inn et ord for å finne det første stedet det står: ")
            if ord == "exit":  
                test = False
                menyOrd()
                valg = input("Velg et alternativ: ")   # hvis man velger 1 kjører man printOrd. 
                gjoermenyvalg(valg)
            printOrd(ord, tekstliste)
    elif tall == "2":
        test = True                 #velger man 2 kjører den printOrdene. finner alle gangene ordet står i teksten
        while test == True:
            ord = input("Skriv inn et ord for å finne alle gangene det står: ")
            if ord == "exit":
                test = False
                printMeny()
                valg = input("Velg et alternativ: ")
                gjoermenyvalg(valg)
            printOrdene(ord, tekstliste)
    elif tall == "3":
        bekreftelse = input("Er du sikker på at du vil tilbake til menyen? J/N: ")
        if bekreftelse.lower() == "j":
            printMeny()
            menyvalg = input("Velg et alternativ: ")
            utfoerMenyvalg(menyvalg, tekstliste)
        else:
            menyOrd()
            valg = input("Velg et alternativ: ")
            gjoermenyvalg(valg)
    else:
        print("Ugyldig valg. Velg et tall mellom 1-3.")
        menyOrd()
        valg = input("Velg et alternativ: ")
        gjoermenyvalg(valg)      

def linjemenyvalg(tall):              #menyvalg for linjemeny. altså valg 3 i hovedmenyen.
    if tall == "1":
        test = True
        while test == True:
            ord = input("Skriv inn et ord for å finne den første linja det står på: ")
            if ord == "exit":
                test = False
                menyLinje()
                valg2 = input("Velg et alternativ: ")
                linjemenyvalg(valg2)
            finnLinje(ord, tekstliste)
    elif tall == "2":
        test = True
        while test == True:
            ord = input("Skriv inn et ord for å finne alle linjene det står på: ")
            if ord == "exit":
                test = False
                menyLinje()
                valg2 = input("Velg et alternativ: ")
                linjemenyvalg(valg2)
            finnLinjene(ord, tekstliste)
    elif tall == "3":
        bekreftelse = input("Er du sikker på at du vil tilbake til menyen? J/N: ")
        if bekreftelse.lower() == "j":
            printMeny()
            menyvalg = input("Velg et alternativ: ")
            utfoerMenyvalg(menyvalg, tekstliste)
        else:
            menyOrd()
            valg = input("Velg et alternativ: ")
            gjoermenyvalg(valg)
    else:
        print("Ugyldig valg. Velg et tall mellom 1-3.")
        menyOrd()
        valg = input("Velg et alternativ: ")
        gjoermenyvalg(valg)      


def printOrd(ord, tekstliste):          #her ligger funksjonene
    for linje in tekstliste:
        if ord in linje.split():  
            console_clear()
            print(f"Fant ordet '{ord}'")     
            return
    console_clear()
    print(f"Ordet '{ord}' ble ikke funnet.")


def printOrdene(ord, tekstliste):
    console_clear()
    for linjenummer, linje in enumerate(tekstliste, start=1):  #denne linja teller alle linjene.
        if ord in linje.split():  
            print(f"Fant ordet '{ord}' på linje {linjenummer}")
            funnet = True
    print(f"Ordet '{ord}' ble ikke funnet i teksten.")


def finnOrd(ord, tekstliste):
    for indeks, linje in enumerate(tekstliste, start=1):
        if ord in linje.split():
            console_clear()
            print("True")
            return
    console_clear()
    print("False")

def finnLinje(ord, tekstliste):
    for indeks, linje in enumerate(tekstliste, start=1):
        if ord in linje.split():
            console_clear()
            print(f"'{ord}' står på linje {indeks}: {linje.strip()}")
            return
    console_clear()
    print(f"Ordet '{ord}' ble ikke funnet i teksten.")

def finnLinjene(ord, tekstliste):
    console_clear()
    for indeks, linje in enumerate(tekstliste, start=1):
        if ord in linje.split():  
            print(f"'{ord}' står på linje {indeks}: {linje.strip()}")
            funnet = True
    print(f"Ordet '{ord}' ble ikke funnet i teksten.")


def tellOrd(ord, tekstliste):
    antall = 0
    for linje in tekstliste:
        if ord in linje.split():
            antall += 1
    if antall == 1:
        console_clear()
        print(f"Ordet '{ord}' står {antall} gang i teksten.")
    else:
        console_clear()
        print(f"Ordet '{ord}' står {antall} ganger i teksten.")

#denne delen her starter hele programmet.

tekstliste = lesInnTekst("tekstfil1.txt")  #leser av tekstfil1.txt

if tekstliste:
    while True:      #hvis tekstfil1.txt finnes starter den programmet med printmeny.
        printMeny()
        menyvalg = input("Velg et alternativ: ")
        utfoerMenyvalg(menyvalg, tekstliste)