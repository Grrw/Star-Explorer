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
        while not cExit:
            print("Loading...")
            # try/except tries to get the date from swapi
            try:
                cResponse = requests.get('http://swapi.co/api/people/' + str(cAcc), timeout = 9)
                homeChoice = func.charScreen(cResponse, cAcc) # store what the function returns
            except:
                func.tryFailed()
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
                    print("Invalid number. Please ")
                    cAcc = cAcc
                else:
                    cAcc = charJump

# PLANET SELECT
    elif mSelect == 'p':
        pExit = False
        pAcc = 1
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
                    except ConnectionError:
                        filmTimeout = True





# VEHICLE SELECT
    elif mSelect == 'v':
        pass

# STARSHIP SELECT
    elif mSelect == 's':
        pass