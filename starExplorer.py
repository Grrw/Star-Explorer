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
            cResponse = requests.get('http://swapi.co/api/people/' + str(cAcc))
            if pSel == 1:
                func.charScreen(cResponse, cAcc)
            elif pSel == 2:
                func.charScreen2(cResponse, cAcc)
            # print(cAcc)
            cSelect = getch.getch()
            if cSelect == 'q':
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
        pass
    # Films
    elif mSelect == 'f':
        pass
    # Vehicles
    elif mSelect == 'v':
        pass
    # Starships
    elif mSelect == 's':
        pass



