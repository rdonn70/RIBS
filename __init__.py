import sys
import random
import time
from msvcrt import getch
from os import system
from datetime import datetime
from team_league_generation import league_generator
from game import generate_game

current_year = datetime.now().year

def getkey():
    firstkey = getch()
    if(firstkey == b'\xe0'):
        return {b'P': "down", b'H': "up", b'M': "right", b'K': "left"}[getch()]
    elif(firstkey == b'\r'):
        return "enter"
    elif(firstkey == b'\x1b'):
        return "escape"
    elif(firstkey == b' '):
        return "space"
    else:
        return firstkey

def scrimmage(debug=0):
    if(debug == 1):
        print("DEBUG MODE ENABLED")
    print("Generating Leagues...")
    time.sleep(1)
    leagues = league_generator(current_year)
    home_team = leagues[0][1][0]
    away_team = leagues[0][1][1]
    system('cls') #Clears past print in cmd prompt
    print("League Generation Finished!")
    print("Starting Game - {} at {}".format(away_team[0][0], home_team[0][0]))
    print("")
    time.sleep(3)
    generate_game(home_team, away_team, debug)
    return

def season(): #WIP
    print("Generating Leagues...")
    time.sleep(1)
    leagues = league_generator(current_year)
    print("League Generation Finished!")
    time.sleep(0.5)
    system('cls') #Clears past print in cmd prompt
    print("Creating Regular Season Schedule...")
    return

df = random.randint(0, 9999)
selection_state = 0
system('cls')
if(df == 2006):
    screen_df = 1
    print("\u001b[31mSlaves to Armok: God of Blood\u001b[0m")
    print("Chapter III: Baseball")
    print("")
    print("Dwarf Fortress <<")
    print("Adventurer")
else:
    screen_df = 0
    print("\u001b[32mRyan's Insane Baseball Simulator\u001b[0m")
    print("Scrimmage Mode <<")
    print("Season Mode")

while True:
    keyboard_input = getkey()
    if(keyboard_input == 'escape'):
        sys.exit()
    elif(keyboard_input == b'`'):
        system('cls')
        scrimmage(1)
    elif(keyboard_input == 'down'):
        if(selection_state == 0 and screen_df == 1):
            system('cls')
            print("\u001b[31mSlaves to Armok: God of Blood\u001b[0m")
            print("Chapter III: Baseball")
            print("")
            print("Dwarf Fortress")
            print("Adventurer <<")
            selection_state = 1
        elif(selection_state == 0 and screen_df == 0):
            system('cls')
            print("\u001b[32mRyan's Insane Baseball Simulator\u001b[0m")
            print("Scrimmage Mode")
            print("Season Mode <<")
            selection_state = 1
    elif(keyboard_input == 'up'):
        if(selection_state == 1 and screen_df == 1):
            system('cls')
            print("\u001b[31mSlaves to Armok: God of Blood\u001b[0m")
            print("Chapter III: Baseball")
            print("")
            print("Dwarf Fortress <<")
            print("Adventurer")
            selection_state = 0
        elif(selection_state == 1 and screen_df == 0):
            system('cls')
            print("\u001b[32mRyan's Insane Baseball Simulator\u001b[0m")
            print("Scrimmage Mode <<")
            print("Season Mode")
            selection_state = 0
    elif(keyboard_input == 'enter' or 'space'):
        if(selection_state == 1):
            system('cls')
            print("INVALID SELECTION. Season Mode Coming Soon.")
            selection_state = 0
            time.sleep(3)
            system('cls')
            if(screen_df == 1):
                print("\u001b[31mSlaves to Armok: God of Blood\u001b[0m")
                print("Chapter III: Baseball")
                print("")
                print("Dwarf Fortress <<")
                print("Adventurer")
            else:
                print("\u001b[32mRyan's Insane Baseball Simulator\u001b[0m")
                print("Scrimmage Mode <<")
                print("Season Mode")
        else:
            system('cls')
            scrimmage(0)