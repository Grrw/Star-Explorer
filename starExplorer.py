import requests, os, json, time, getch, func

func.windResize()


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
                try:
                    if int(charJump) <= 0 or int(charJump) >= 89:
                        wrongCharNum = True
                    else:
                        cAcc = int(charJump)
                except:
                    wrongCharNum = True

# PLANET SELECT
    elif mSelect == 'p':
        pExit = False
        pAcc = 1
        wrongPlanetNumber = False
        while not pExit:
            if tryWorld == True: # if user pressed 'k' on charScreen, take them to the planet
                pAcc = int(homeChoice)
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
                planetJump = input("Type a number from 1-61: ") # jump to character
                try:
                    if int(planetJump) <= 0 or int(planetJump) >= 62:
                        wrongPlanetNumber = True
                    else:
                        pAcc = int(planetJump)
                except:
                    wrongPlanetNumber = True

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
        vExit = False
        vehiclePage = 1
        vehicleIndex = 0 # going to 8 on p4
        pageFour = False
        one_error = False
        two_error = False
        while not vExit:
            wrongJump = False
            func.clearS()
            try:
                vResponse = requests.get('http://swapi.co/api/vehicles/?page=' + str(vehiclePage))
                vehicleData = func.transportScreen(vResponse, vehicleIndex, True)
                print("| Vehicle Identification (section / number) = " + str(vehiclePage) + ' / ' + str(vehicleIndex))
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                if pageFour == True:
                    print("Section 4 only goes up to 8.")
                    pageFour = False
                if one_error == True:
                    print("Invalid number, try 1-4.")
                    one_error = False
                if two_error == True:
                    print("Invalid number, try 0 - 9")
                    two_error = False
            except:
                func.tryFailed()

            vSelect = getch.getch()
            if vSelect == 'q':
                vExit = True

            # the following loops pages and indexes
            elif vSelect == 'l':
                if vehiclePage == 4 and vehicleIndex == 8:
                    vehiclePage = 1
                    vehicleIndex = -1
                vehicleIndex = vehicleIndex + 1
                if vehicleIndex > 9:
                    vehiclePage = vehiclePage + 1
                    vehicleIndex = 0
            elif vSelect == 'h':
                vehicleIndex = vehicleIndex - 1
                if vehicleIndex < 0:
                    vehiclePage = vehiclePage - 1
                    if vehiclePage < 1:
                        vehiclePage = 4
                    vehicleIndex = 9
                    if vehiclePage == 4:
                        vehicleIndex = 8

            elif vSelect == 'i':
                jumpVehicle = input("Type the first vehicle identification number: ")
                try:
                    jumpVehicle = int(jumpVehicle) # make the user's input into int
                except:
                    wrongJump = True
                if wrongJump == False:
                    if jumpVehicle > 4 or jumpVehicle < 1:
                        one_error = True
                        wrongJump = True
                        # only if put in a proper first number:
                    else:
                        jumpVehicle2 = input('Type the second ship identification number : ' + str(jumpVehicle) + ' / ')
                        try:
                            jumpVehicle2 = int(jumpVehicle2) # make the user's input into int
                        except:
                            wrongJump = True
                        if wrongJump == False:
                            if jumpVehicle2 == 4 and jumpVehicle2 > 8 and jumpVehicle2 <= 9:
                                jumpVehicle2 = 8
                                pageFour = True
                            elif jumpVehicle2 > 8 or jumpVehicle2 < 0:
                                two_error = True
                                wrongJump = True

                if wrongJump != True:
                    jumpVehicle = str(jumpVehicle) + str(jumpVehicle2)
                    jumpVehicle = list(jumpVehicle)
                    vehiclePage = int(jumpVehicle[0])
                    vehicleIndex = int(jumpVehicle[1])


# STARSHIP SELECT
    elif mSelect == 's':
        sExit = False
        shipPage = 1
        shipIndex = 0
        pageFour = False
        one_error = False
        two_error = False
        while not sExit:
            wrongJump = False # used if 'i' is pressed
            func.clearS()
            try:
                sResponse = requests.get('http://swapi.co/api/starships/?page=' + str(shipPage))
                shipData = func.transportScreen(sResponse, shipIndex, False)
                print("| Ship Identification (section / number) = ", str(shipPage), '/', str(shipIndex))
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
                if pageFour == True:
                    print("Section 4 only goes up to 6.")
                    pageFour = False
                if one_error == True:
                    print("Invalid number, try 1-4.")
                    one_error = False
                if two_error == True:
                    print("Invalid number, try 0 - 9")
                    two_error = False
                    
            except:
                func.tryFailed()

            sSelect = getch.getch()
            if sSelect == 'q':
                sExit = True

            # the following loops pages and indexes
            elif sSelect == 'l':
                if shipPage == 4 and shipIndex == 6:
                    shipPage = 1 
                    shipIndex = -1
                    print('loop to shipPage 1 and shipIndex 0')
                shipIndex = shipIndex + 1
                print('added 1 to shipIndex')
                if shipIndex > 9:
                    shipPage = shipPage + 1 # ships are on pages, referenced by indexes of 'results'
                    print('added 1 to shipPage')
                    shipIndex = 0
                    print('reset shipIndex')
            elif sSelect == 'h':
                shipIndex = shipIndex - 1
                print('remove 1 from shipIndex')
                if shipIndex < 0:
                    shipPage = shipPage - 1
                    print('remove 1 from shipPage')
                    if shipPage < 1:
                        shipPage = 4
                        print('backwards reset of shipPage')
                    shipIndex = 9
                    print('reset of shipIndex (p1-3)')
                    if shipPage == 4:
                        shipIndex = 6
                        print('backwards reset (p4) of shipIndex')

            elif sSelect == 'i':
                jumpShip = input("Type the first ship identification number: ")
                try:
                    jumpShip = int(jumpShip) # make the user's input into int
                except:
                    wrongJump = True
                if wrongJump == False:
                    if jumpShip > 4 or jumpShip < 1:
                        one_error = True
                        wrongJump = True
                        # only if put in a proper first number:
                    else:
                        jumpShip2 = input('Type the second ship identification number : ' + str(jumpShip) + ' / ')
                        try:
                            jumpShip2 = int(jumpShip2) # make the user's input into int
                        except:
                            wrongJump = True
                        if wrongJump == False:
                            if jumpShip == 4 and jumpShip2 > 6 and jumpShip2 <= 9:
                                jumpShip2 = 6
                                pageFour = True
                            elif jumpShip2 > 9 or jumpShip2 < 0:
                                two_error = True
                                wrongJump = True

                if wrongJump != True:
                    jumpShip = str(jumpShip) + str(jumpShip2)
                    jumpShip = list(jumpShip)
                    shipPage = int(jumpShip[0])
                    shipIndex = int(jumpShip[1])