import requests, os, json, time, getch, func

func.windResize()
input()

mExit = False
while not mExit:
    func.mainScreen()
    mSelect = getch.getch()
    # Quitting
    if mSelect == 'q':
        mExit = True
        os.system('cls' if os.name == 'nt' else 'clear')
    # Characters
    elif mSelect == 'c':
        cExit = False
        cAcc = 1
        pSel = 1
        while not cExit:
            print("Loading...")
            try:
                cResponse = requests.get('http://swapi.co/api/people/' + str(cAcc), timeout = 10)
                func.charScreen(cResponse, cAcc)
            except:
                func.tryFailed()
            # print(cAcc)
            cSelect = getch.getch()
            if cSelect == 'q': # Quit
                cExit = True
            elif cSelect == 'h':
                cAcc = cAcc - 1
                if cAcc <= 0:
                    cAcc = 88
                # print(cAcc)
            elif cSelect == 'l':
                cAcc = cAcc + 1
                if cAcc >= 89:
                    cAcc = 1
                # print(cAcc)
    # Planets
    elif mSelect == 'p':
        pExit = False
        pAcc = 1
        while not pExit:
            print("Loading...")
            try:
                pResponse = requests.get('http://swapi.co/api/planets/' + str(pAcc), timeout = 10)
                func.planetScreen(pResponse, pAcc)
            except:
                func.tryFailed()
            pSelect = getch.getch()
            if pSelect == 'q': # Quit 
                pExit = True
            elif pSelect == 'h':
                pAcc = pAcc - 1
                if pAcc <= 0:
                    pAcc = 61
            elif pSelect == 'l':
                pAcc = pAcc +1
                if pAcc >= 62:
                    pAcc = 1

    # Films
    elif mSelect == 'f':
        pass
    # Vehicles
    elif mSelect == 'v':
        pass
    # Starships
    elif mSelect == 's':
        pass



