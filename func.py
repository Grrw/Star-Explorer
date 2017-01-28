import json, os, time, requests, getch

    # print(" ____________________________________________________________________________________________________")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print("|                                                                                                    |")
    # print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def clearS():
    os.system('cls' if os.name == 'nt' else 'clear')

def windResize():
    """
    Previously used for resizing the window, which is no longer necessary
    Currently serves as a credits page
    """
    clearS()
    print(" ______________________________________________________________________________________________________")
    print("|  ,      \"                 .                             .                        .                   |")
    print("|  ,          ~        *       ,          Created by Ben Yeffet   ,           *          `          @  |")
    print("|        @                            .       '            `                             ,             |")
    print("|  '              `                Inspired by towel.blinkenlights.nl       `                          |")
    print("|          .               `             .                                         .                   |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    time.sleep(3)
    return

def mainScreen():
    """
    Main Menu Screen, returned to as a side-effect of switching from one to another
    Hard-coded and needs no web access
    """
    clearS()
    print(" M̲a̲i̲n̲_P̲a̲ge̲___________________________________________________________________________________________")
    print("|   `       .         ,       *         '   .          `         `       .      `      '         ,   |")
    print("|     @         `         ,        Star Wars Informational Navigator       .        `             .  |")
    print("|          `           .          .      'c' for characters          .            ,         *        |")
    print("|   .          __                          'p' for planets       `          '            ,           |")
    print("|            / *  \           .             'f' for films       .            ,                       |")
    print("|       `    \    /                        'v' for vehicles             `          `           @     |")
    print("|              ‾‾       `         '       's' for starships       ,                      `           |")
    print("|   \"                      '               .             .                    *               '      |")
    print("|                .                                                      .                            |")
    print("|   `    ,                               '        \"           `                           |_/‾‾\_|   |")
    print("|                       @          `         'q' to quit           \"       `     '        |‾\__/‾|   |")
    print("|    `         *               ,                  ,             `       ,                            |")
    print("|       .               '             \"                  *                       `         ,         |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def tryFailed():
    """
    Call when a try/except is used to prevent app from crashing
    """
    clearS()
    print("Webpage timed out. Press 'q' to go back, 'j' to try again.")
    return

def charScreen(cURL, number):
    """
    Pass a URL and get info from each character and their homeworld
    Bring up tryFailed if server does not respond to either request
    """
    clearS()
    homeWorld = str(json.loads(cURL.text)['homeworld']) # make 'homeworld' into a string
    homeWorld = homeWorld.split("/")
    try:
        charWorld = requests.get('http://swapi.co/api/planets/' + homeWorld[5]) # get the planet info
    except:
        tryFailed()
        return
    personData = json.loads(cURL.text)
    print(" C̲h̲a̲r̲a̲c̲t̲e̲r̲_V̲i̲e̲w̲e̲r̲__________________________________________________________________________________")
    print("| Number: " + str(number))
    print("| Name: " + personData['name'])
    print("| Height: " + personData['height'])
    print("| Mass: " + personData['mass'])
    print("| Hair Color: " + personData['hair_color'])
    print("| Skin Color: " + personData['skin_color'])
    print("| Eye Color: " + personData['eye_color'])
    print("| Birth Year: " + personData['birth_year'])
    print("| Gender: " + personData['gender'])
    print("| Homeworld: " + json.loads(charWorld.text)['name'] + '\n|\n| \'q\' to return')
    print("| 'k' to go to homeworld / 'i' to insert character number if you know it")
    print("| 'h' for previous character / 'l' for next / 'j' to reload page")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return homeWorld[5] # take the number of the homeworld, and return it


def planetScreen(cURL, number):
    """
    Pass a URL and get info from each planetScreen
    tryFailed is brought up outside the function, this is used only to pring the information
    """
    clearS()
    planetData = json.loads(cURL.text)
    print(" _P̲l̲a̲n̲e̲t̲_V̲i̲e̲w̲e̲r̲______________________________________________________________________________________")
    print("| Number: " + str(number))
    print("| Name: " + planetData['name'])
    print("| Rotational Period: " + planetData['rotation_period'])
    print("| Orbital Period: " + planetData['orbital_period'])
    print("| Diameter: " + planetData['diameter'])
    print("| Climate: " + planetData['climate'])
    print("| Gravity: " + planetData['gravity'])
    print("| Terrain: " + planetData['terrain'])
    print("| Surface Water: " + planetData['surface_water'])
    print("| Population: " + planetData['population'] + '\n|\n| \'q\' to return')
    print("| 'i' to insert planet number if you know it")
    print("| 'h' for previous planet / 'l' for next")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def filmScreen(cURL, number):
    """
    Comparatively complicated because it functions as its own menu
    Pass a URL and the number of the movie to load information
    """
    filmScreenLoop = False # while loop for main filmScreen page
    filmData = json.loads(cURL.text)
    while not filmScreenLoop:
        clearS()
        print(" _F̲i̲l̲m̲_V̲i̲e̲w̲e̲r̲________________________________________________________________________________________")
        print("| Title: " + filmData['title'])
        print("| Director: " + filmData['director'])
        print("| Producer: " + filmData['producer'])
        print("| Release Date: " + filmData['release_date'] + '\n|')
        print("| 'q' to return")
        print("| 'k' to view opening crawl")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        film_selection = getch.getch() # select an option
        if film_selection == 'q':
            filmScreenLoop = True
        elif film_selection == 'k':
            # The information is pulled and made into a list
            crawlString = str(json.loads(cURL.text)['opening_crawl'])
            crawlString = crawlString.split("\n")

            crawlStringLoop = False # while loop for secondary filmScreen page
            crawlString.append(" ")
            crawlString.append("END OF CRAWL")
            linePrint = 0 # starts on crawlString[0]

            while not crawlStringLoop:
                clearS()
                print(" _F̲i̲l̲m̲_V̲i̲e̲w̲e̲r̲_C̲r̲a̲w̲l̲__________________________________________________________________________________")
                print("| 'q' to quit")
                print("| 'h' to return to begnning, 'l' to scroll down.")
                print("|----------------------------------------------------------------------------------------------------\n|")
                print("| " + crawlString[linePrint])
                print("| " + crawlString[linePrint + 1])
                print("| " + crawlString[linePrint + 2])
                print("| " + crawlString[linePrint + 3])
                print("| " + crawlString[linePrint + 4] + '\n|')
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                crawlStringLen = len(crawlString)
                crawlStringSelection = getch.getch() # the user's input
                if crawlStringSelection == 'q':
                    crawlStringLoop = True

                elif crawlStringSelection == 'l':
                    crawlStringDecider = False # used for decding how many lines will be printed
                    linePrint = linePrint + 1
                    while not crawlStringDecider:
                        # prevent linePrint from going over crawlStringLen
                        if linePrint + 5 >= crawlStringLen:
                            linePrint = crawlStringLen
                            linePrint = linePrint - 5
                            crawlStringDecider = True
                        else:
                            crawlStringDecider = True

                elif crawlStringSelection == 'h':
                    crawlStringDecider = False # used for decding how many lines will be printed
                    linePrint = linePrint - 1
                    while not crawlStringDecider:
                        # prevent linePrint from going under 0
                        if linePrint - 5 <= crawlStringLen:
                            linePrint = 0
                            crawlStringDecider = True
                        else:
                            crawlStringDecider = True

def transportScreen(cURL, index, vehicle): # vehicle must be True or False
    """
    Because Vehicles and Starships are very similiar, takes either
    Only attempts to print either Starship or Vehicle info

    """
    clearS()
    transportData = json.loads(cURL.text)
    if vehicle == False:
        print(" _S̲t̲a̲r̲s̲h̲i̲p̲_V̲i̲e̲w̲e̲r̲____________________________________________________________________________________")
    elif vehicle == True:
        print(" _V̲e̲h̲i̲c̲l̲e̲_V̲i̲e̲w̲e̲r̲_____________________________________________________________________________________")
    print("| Name: " + transportData['results'][index]['name'])
    print("| Model: " + transportData['results'][index]['model'])
    print("| Manufacturer: " + transportData['results'][index]['manufacturer'])
    print("| Length: " + transportData['results'][index]['length'])
    print("| Max Atmosphering Speed: " + transportData['results'][index]['max_atmosphering_speed'])
    print("| Crew: " + transportData['results'][index]['crew'])
    print("| Passengers: " + transportData['results'][index]['passengers'])
    print("| Cargo Capacity: " + transportData['results'][index]['cargo_capacity'])
    if vehicle == False:
        print("| Hyperdrive Rating: " + transportData['results'][index]['hyperdrive_rating'])
        print("| MGLT: " + transportData['results'][index]['MGLT'])
        print("| Starship Class: " + transportData['results'][index]['starship_class'])
    elif vehicle == True:
        print("| Vehicle Class: " + transportData['results'][index]['vehicle_class'])
    print("| 'i' to insert ship identification numbers if you know them")
    print("| 'k' to view films with this ship / 'h' for previous ship, 'l' for next")
    return transportData