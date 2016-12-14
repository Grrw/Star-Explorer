import time, os

def loading():
    l='Loading... '
    a=0
    while True:
        time.sleep(.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        a=a+1
        if a%11==0: print(l+'[ █       ██ ]')
        elif a%11==1: print(l+'[ ██        █]')
        elif a%11==2: print(l+'[  ███       ]')
        elif a%11==3: print(l+'[   ███      ]')
        elif a%11==4: print(l+'[    ███     ]')
        elif a%11==5: print(l+'[     ███    ]')
        elif a%11==6: print(l+'[      ███   ]')
        elif a%11==7: print(l+'[       ███  ]')
        elif a%11==8: print(l+'[        ███ ]')
        elif a%11==9: print(l+'[ █       ██ ]')
        elif a%11==10:
            return
