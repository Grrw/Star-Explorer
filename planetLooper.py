import requests, json, time, os, getch, func

acc = 1
while True:
    response = requests.get('http://swapi.co/api/planets/' + str(acc))
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(str(acc))
    print('Name: ', json.loads(response.text)['name'])
    print('Population: ', json.loads(response.text)['population'])
    print('f for forward, d for backward, q for quit')
    forBack = getch.getch()
    if forBack == 'f':
        if acc == 61:
            print('Looping to Planet #1')
            time.sleep(1)
            func.loading()
            acc = 1
        else:
            func.loading()
            acc = acc + 1
    elif forBack == 'd':
        if acc == 1:
            print('Looping to Planet #61')
            time.sleep(1)
            func.loading()
            acc = 61
        else:
            func.loading()
            acc = acc - 1
    elif forBack == 'q':
        break