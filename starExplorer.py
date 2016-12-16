import requests, os, json, time, getch, func

func.windResize()
input()

mExit = False
while not mExit:
    os.system('cls' if os.name == 'nt' else 'clear')
    func.mainScreen()
    mSelect = getch.getch()
    if mSelect == 'q':
        mExit = True
        os.system('cls' if os.name == 'nt' else 'clear')





