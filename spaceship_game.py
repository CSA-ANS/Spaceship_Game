#Ammaar Siddiqui
#Comp Prog
#10/12/17
PLANET=" " #define globals
NAME=" "
POINTS=0
def startup():
    print("Hello captain, welcome to the spaceship game. Your objective is simple. Fly from one planet to another without DYING! ")# introduction of game
    global NAME
    NAME=input("What is your name: ")#Asks them for their name.
    print("Hello "+NAME.title())
    menu()
def menu():
    print("1. Start Game")# Gives them option to start game or enter planet code
    print("2. Enter Planet Code")
    print("3. Quit Game")
    menuoption=input("Choose a number from the menu: ")
    if menuoption=="1":
        start_game()# starts game
    elif menuoption=="2":
        planetcode()# Gives them the option to enter planet code
    elif menuoption=="3":
        quit()#just in case they don't want to play
    elif menuoption=="4":#This number is not on the menu it is secretly hidden.
        cheatcode()
    else:
        print("What you have entered is invalid. Chose again")
        menu()
def cheatcode():
    print("You have found the secret option on the menu!")
    cheatcode=input("What is your cheat code: ")
    if cheatcode=="1860":#tells them all the escape velocities
        print("Mercury's escape velocity is 9,506.979 mph ")
        print("Venus's escape velocity is 23,174.66 mph")
        print("Earth's escape velocity is 25,022.3694 mph")
        print("Mars' escape velocity is 11,251.79 mph")
        print("Jupiter's escape velocity is 134,663.6 mph ")
        print("Saturn's escape velocity is 80,731.031 mph")
        print("Uranus' escape velocity is 47,825.698 mph")
        print("Neptune's escape velocity is 52,702.219 mph")
        print("Pluto's escape velocity is 2,751.432 mph")
        start_game()
    else:
        print("invalid cheat code")
        menu()
def planetcode():
    global PLANET
    entry=int(input("What is your planet code: "))#ask for planet code and checks what planet's code it is
    if entry==1:
        PLANET="earth"
    elif entry==2:
        PLANET="mercury"
    elif entry==3:
        PLANET="venus"
    elif entry==4:
        PLANET="mars"
    elif entry==5:
        PLANET="jupiter"
    elif entry==6:
        PLANET="saturn"
    elif entry==7:
        PLANET="uranus"
    elif entry==8:
        PLANET="neptune"
    elif entry==9:
        PLANET="pluto"
    else:
        print("invalid planet code")
        planetcode()
    pick_planet()#asks where do you want to go
def start_game():
    global PLANET#uses global
    PLANET=("earth")
    weight=input("How much does your ship weigh in pounds: ")#weight for future more realistic versions of the game where phiyscs matter
    print("Earth is where you will begin")
    pick_planet()
def pick_planet():
    print("Mercury")#tells you where you can go
    print("Venus")
    print("Earth")
    print("Mars")
    print("Jupiter")
    print("Saturn")
    print("Uranus")
    print("Neptune")
    print("Pluto")
    where=input("Where would you like to go: ").lower()
    if where != "earth" and where!= "mercury" and where!= "venus" and where!= "mars" and where!= "jupiter" and where!= "saturn" and where!= "uranus" and where!= "neptune" and where!= "pluto":
        print("invalid planet")
        pick_planet()#if they enter a planet that doesn't exist.
    if PLANET==where:
        print("You are already on "+PLANET.title()+" please pick another planet")
        pick_planet()#If they enter a planet they are already on
    else:
        escape_velocity(where)
def escape_velocity(where):
    global PLANET# global
    if PLANET=="earth":
        print("Welcome to Earth")
        escapevelocity=25022.3694#defines if planet = x escape velocity needed to escape is y
        planetcode=1
        print("your planet code is "+str(planetcode))#tells them the planet code
    elif PLANET=="mercury":
        print("Welcome to Mercury")
        escapevelocity=9506.979
        planetcode=2
        print("your planet code is "+str(planetcode))
    elif PLANET=="venus":
        print("Welcome to Venus")
        escapevelocity=23174.66
        planetcode=3
        print("your planet code is "+str(planetcode))
    elif PLANET=="mars":
        print("Welcome to Mars")
        escapevelocity=11251.79
        planetcode=4
        print("your planet code is "+str(planetcode))
    elif PLANET=="jupiter":
        print("Welcome to Jupiter")
        escapevelocity=134663.6
        planetcode=5
        print("your planet code is "+str(planetcode))
    elif PLANET=="saturn":
        print("Welcome to Saturn")
        escapevelocity=80731.031
        planetcode=6
        print("your planet code is "+str(planetcode))
    elif PLANET=="uranus":
        print("Welcome to Uranus")
        escapevelocity=47825.698
        planetcode=7
        print("your planet code is "+str(planetcode))
    elif PLANET=="neptune":
        print("Welcome to Neptune")
        escapevelocity=52702.219
        planetcode=8
        print("your planet code is "+str(planetcode))
    elif PLANET=="pluto":
        print("Welcome to Pluto")
        escapevelocity=2751.432
        planetcode=9
        print("your planet code is "+str(planetcode))
    takeoff(escapevelocity,where)#takeoff 
def takeoff(escapevelocity,where):
    global POINTS
    global PLANET# tells the program we will change the global
    speed=float(input("How fast would you like to go in mph: "))
    if speed==escapevelocity:
        print("You have escaped")#checks if they are able to escape
        PLANET=where
        print("You have successfully landed on "+ PLANET.title())
        POINTS=POINTS+100#more points if you are closer to the actual escape velocity
        print("You gained 100 points")
        leave()#continue or quit
    elif speed>escapevelocity and speed<escapevelocity*1.05:
        print("You have escaped")#checks if they are able to escape
        PLANET=where
        print("You have successfully landed on "+ PLANET.title())
        POINTS=POINTS+50
        print("You gained 50 points")
        leave()#continue or quit
    elif speed>escapevelocity and speed<escapevelocity*1.1:
        print("You have escaped")#checks if they are able to escape
        PLANET=where
        print("You have successfully landed on "+ PLANET.title())
        POINTS=POINTS+20
        print("You gained 20 points")
        leave()#continue or quit
    elif speed<escapevelocity:
        print("You went to slow. You die")#if they are not able to escape they die and restart or quit
        print("Your final score is "+str(POINTS)+" points")#tells them how many points they have
        print("Your points have been reset.")
        PLANET="earth"#resets planet to earth
        POINTS=0
        leave()
    elif speed>escapevelocity+escapevelocity*.10:
        print("you went too fast. You die")
        print("Your final score is "+str(POINTS)+" points")#tells them how many points they have
        print("Your points have been reset.")#lets them know that they have lost all points
        PLANET="earth"#resets planet to earth
        POINTS=0#They lose all points
        leave()
def leave():
    global POINTS
    print("1. Continue")
    print("2. Quit")
    leave=int(input("Would you like to continue or quit: "))#gives them the option of quitting
    if leave==1:
        pick_planet()#lets them continue
    elif leave==2:
        print("You have "+str(POINTS)+" points")
        quit()#quit function closes program
    else:
        print("Invalid Option. Please pick again")
        leave()
startup()#starts the game
