import requests, os, json, time, getch, func

func.windResize()
input()

reloadFilms = False # used when user chose invalid film
tryWorld = False # used when user goes from Character to Planets
mExit = False

while not mExit:
    func.mainScreen()
    if tryWorld == True: # if user pressed 'k' on charScreen, autoselect 'p' on mainScreen
        mSelect = 'p'
        func.clearS()
    else:
        mSelect = getch.getch()

# QUIT MAIN LOOP
    if mSelect == 'q':
        mExit = True
        func.clearS()

# CHARACTER SELECT
    elif mSelect == 'c':
        cExit = False
        cAcc = 1
        wrongCharNum = False
        while not cExit:
            print("Loading...")
            # try/except tries to get the date from swapi
            try:
                cResponse = requests.get('http://swapi.co/api/people/' + str(cAcc), timeout = 9)
                homeChoice = func.charScreen(cResponse, cAcc) # store what the function returns
            except:
                func.tryFailed()

            # if user previously selected an invalid number
            if wrongCharNum == True:
                print("Invalid number. Please try 1-88")
                wrongCharNum = False

            cSelect = getch.getch()
            if cSelect == 'q': # quit
                cExit = True
            elif cSelect == 'h': # prev
                cAcc = cAcc - 1
                if cAcc <= 0:
                    cAcc = 88
            elif cSelect == 'l': # next 
                cAcc = cAcc + 1
                if cAcc >= 89:
                    cAcc = 1
            elif cSelect == 'j':
                print("Reloading")
            elif cSelect == 'k':
                cExit = True
                tryWorld = True
            elif cSelect == 'i':
                charJump = input("Type a number from 1-88: ") # jump to character
                if int(charJump) <= 0 or int(charJump) >= 89:
                    wrongCharNum = True
                    cAcc = cAcc
                else:
                    cAcc = charJump

# PLANET SELECT
    elif mSelect == 'p':
        pExit = False
        pAcc = 1
        wrongPlanetNumber = False
        while not pExit:
            if tryWorld == True: # if user pressed 'k' on charScreen, take them to the planet
                pAcc = homeChoice
                tryWorld = False
            print("Loading...")
            # try/except tries to get the date from swapi
            try:
                pResponse = requests.get('http://swapi.co/api/planets/' + str(pAcc), timeout = 9)
                func.planetScreen(pResponse, pAcc)
            except:
                func.tryFailed()

            # if user previously selected an invalid number
            if wrongPlanetNumber == True:
                print("Invalid number. Please try 1-61")
                wrongPlanetNumber = False

            pSelect = getch.getch()
            if pSelect == 'q': # quit 
                pExit = True
            elif pSelect == 'h': # prev
                pAcc = pAcc - 1
                if pAcc <= 0:
                    pAcc = 61
            elif pSelect == 'l': # next
                pAcc = pAcc +1
                if pAcc >= 62:
                    pAcc = 1
            elif pSelect == 'j':
                print('Reloading')
            elif pSelect == 'i':
                planetJump = input("Type a number from 1-88: ") # jump to character
                if int(planetJump) <= 0 or int(planetJump) >= 62:
                    wrongPlanetNumber = True
                    pAcc = pAcc
                else:
                    pAcc = planetJump
                # keep pAcc the same

# FILM SELECT
    elif mSelect == 'f':
        fExit = False
        fAcc = 1
        invalid_message = False
        filmTimeout = False
        while not fExit:
            print("Loading...")
            func.clearS()
            print(" _P̲l̲a̲n̲e̲t̲_V̲i̲e̲w̲e̲r̲______________________________________________________________________________________")
            print("| Select a film (1-7) or press 'q' to quit: \n|")
            print("| 1: The Phantom Menace\n| 2: Attack of The Clones\n| 3: Revenge of the Sith")
            print("| 4: A New Hope\n| 5: The Empire Strikes Back\n| 6: Return of The Jedi")
            print("| 7: The Force Awakens")
            print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾") 
            if invalid_message == True:
                print("Invalid choice. Try 1-7.")
                invalid_message = False
            elif filmTimeout == True:
                print("Webpage timed out. Check internet connection and try again.")
                filmTimeout = False
            fSelect = getch.getch()
            # Change user selection to API designation
            if fSelect == 'q':
                fExit = True
            elif fSelect == '1':
                movieChoice = '4'
            elif fSelect == '2':
                movieChoice = '5'
            elif fSelect == '3':
                movieChoice = '6'
            elif fSelect == '4':
                movieChoice = '1'
            elif fSelect == '5':
                movieChoice = '2'
            elif fSelect == '6':
                movieChoice = '3'
            elif fSelect == '7':
                movieChoice = '7'
            else:
                movieChoice = '0'
            if fExit != True:
                if int(movieChoice) == 0:
                    invalid_message = True
                else:
                    print("Loading...")
                    try:
                        fResponse = requests.get('http://swapi.co/api/films/' + str(movieChoice), timeout = 9)
                        func.filmScreen(fResponse, int(movieChoice))
                    except:
                        filmTimeout = True





# VEHICLE SELECT
    elif mSelect == 'v':
        pass

# STARSHIP SELECT
    elif mSelect == 's':
        sExit = False
        shipPage = 1
        shipIndex = 1
        while not sExit:
            func.clearS()
            try:
                sResponse = requests.get('http://swapi.co/api/starships/?page=' + str(shipPage))
                shipData = func.shipScreen(sResponse, shipIndex)
            except:
                func.tryFailed()
            
            print('shipPage = ' + str(shipPage))
            print('shipIndex = ' + str(shipIndex))

            sSelect = getch.getch()
            if sSelect == 'q':
                sExit = True

            # the following loops pages and indexes
            elif sSelect == 'l':
                if shipPage == 4 and shipIndex == 7:
                    shipPage = 1 
                    shipIndex = 0
                    print('loop to shipPage 1 and shipIndex 0')
                shipIndex = shipIndex + 1
                print('added 1 to shipIndex')
                if shipIndex > 10:
                    shipPage = shipPage + 1 # ships are on pages, referenced by indexes of 'results'
                    print('added 1 to shipPage')
                    shipIndex = 1
                    print('reset shipIndex')
            elif sSelect == 'h':
                shipIndex = shipIndex - 1
                print('remove 1 from shipIndex')
                if shipIndex < 1:
                    shipPage = shipPage - 1
                    print('remove 1 from shipPage')
                    if shipPage < 1:
                        shipPage = 4
                        print('backwards reset of shipPage')
                    shipIndex = 10
                    print('reset of shipIndex (p1-3)')
                    if shipPage == 4:
                        shipIndex = 7
                        print('backwards reset (p4) of shipIndex')
            input()
            