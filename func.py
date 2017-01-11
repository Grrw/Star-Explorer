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

def windResize():
    """
    Used for resizing the window
    Has issues when resizing on Windows CMD
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Please resize your window to fit the following box.")
    print("Press return when you are finished.")
    input()
    print(" R̲e̲s̲i̲z̲e̲________________________________________________________________________________________________")
    print("|  ,      \"                 .                             .                        .                   |")
    print("|      .          `                  @               `                `                      \"         |")
    print("|  ,          ~        *       ,          Created by Ben Yeffet   ,           *          `          @  |")
    print("|        @                            .       '            `                                           |")
    print("|  '              `                Inspired by towel.blinkenlights.nl                                  |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return

def mainScreen():
    """
    Main Menu Screen, returned to as a side-effect of switching from one to another
    Hard-coded and needs no web access
    """
    os.system('cls' if os.name == 'nt' else 'clear')
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Webpage timed out. Press 'q' to go back, 'j' to try again.")
    return

def charScreen(cURL, number):
    """
    Pass a URL and get info from each character and their homeworld
    Bring up tryFailed if server does not respond to either request
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    homeWorld = str(json.loads(cURL.text)['homeworld']) # make 'homeworld' into a string
    homeWorld = homeWorld.split("/")
    try:
        charWorld = requests.get('http://swapi.co/api/planets/' + homeWorld[5]) # get the planet info
    except:
        tryFailed()
        return
    print(" C̲h̲a̲r̲a̲c̲t̲e̲r̲_V̲i̲e̲w̲e̲r̲__________________________________________________________________________________")
    print("| Number: " + str(number))
    print("| Name: " + json.loads(cURL.text)['name'])
    print("| Hight: " + json.loads(cURL.text)['height'])
    print("| Mass: " + json.loads(cURL.text)['mass'])
    print("| Hair Color: " + json.loads(cURL.text)['hair_color'])
    print("| Skin Color: " + json.loads(cURL.text)['skin_color'])
    print("| Eye Color: " + json.loads(cURL.text)['eye_color'])
    print("| Birth Year: " + json.loads(cURL.text)['birth_year'])
    print("| Gender: " + json.loads(cURL.text)['gender'])
    print("| Homeworld: " + json.loads(charWorld.text)['name'] + '\n|\n| \'q\' to return')
    print("| 'k' to go to homeworld / 'i' to insert character number if you know it")
    print("| 'h' for previous character / 'l' for next / 'j' to reload page")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    return homeWorld[5] # take the number of the homeworld, and return it


def planetScreen(cURL, number):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" _P̲l̲a̲n̲e̲t̲_V̲i̲e̲w̲e̲r̲______________________________________________________________________________________")
    print("| Number: " + str(number))
    print("| Name: " + json.loads(cURL.text)['name'])
    print("| Rotational Period: " + json.loads(cURL.text)['rotation_period'])
    print("| Orbital Period: " + json.loads(cURL.text)['orbital_period'])
    print("| Diameter: " + json.loads(cURL.text)['diameter'])
    print("| Climate: " + json.loads(cURL.text)['climate'])
    print("| Gravity: " + json.loads(cURL.text)['gravity'])
    print("| Terrain: " + json.loads(cURL.text)['terrain'])
    print("| Surface Water: " + json.loads(cURL.text)['surface_water'])
    print("| Population: " + json.loads(cURL.text)['population'] + '\n|')
    print("| 'q' to return")
    print("| 'h' for previous planet, 'l' for next, 'j' to reload page")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def filmScreen(cURL, number):
    """
    Comparatively complicated because it functions as its own menu
    Pass a URL and the number of the movie to load information

    """
    filmScreenLoop = False # while loop for main filmScreen page
    while not filmScreenLoop:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" _F̲i̲l̲m̲_V̲i̲e̲w̲e̲r̲________________________________________________________________________________________")
        print("| Title: ")
        print("| Director: " + json.loads(cURL.text)['director'])
        print("| Producer: " + json.loads(cURL.text)['producer'])
        print("| Release Date: " + json.loads(cURL.text)['release_date'] + '\n|')
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
                os.system('cls' if os.name == 'nt' else 'clear')
                print(" _F̲i̲l̲m̲_V̲i̲e̲w̲e̲r̲_C̲r̲a̲w̲l̲__________________________________________________________________________________")
                print("| 'q' to quit")
                print("| 'h' to return to begnning, 'l' for next 5 lines")
                print("|----------------------------------------------------------------------------------------------------")
                print("| " + crawlString[linePrint])
                print("| " + crawlString[linePrint + 1])
                print("| " + crawlString[linePrint + 2])
                print("| " + crawlString[linePrint + 3])
                print("| " + crawlString[linePrint + 4])
                print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

                crawlStringLen = len(crawlString)
                crawlStringSelection = getch.getch() # the user's input
                if crawlStringSelection == 'q':
                    crawlStringLoop = True

                elif crawlStringSelection == 'l':
                    crawlStringDecider = False # used for decding how many lines will be printed
                    linePrint = linePrint + 5
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
                    linePrint = linePrint - 5
                    while not crawlStringDecider:
                        # prevent linePrint from going under 0
                        if linePrint - 5 <= crawlStringLen:
                            linePrint = 0
                            crawlStringDecider = True
                        else:
                            crawlStringDecider = True