import sys
import random
import time
import winsound
from msvcrt import getch
from os import system
from datetime import datetime
from team_league_generation import league_generator
from physics import hitting

current_year = datetime.now().year

def getkey():
    firstkey = getch()
    if(firstkey == b'\xe0'):
        return {b'P': "down", b'H': "up", b'M': "right", b'K': "left"}[getch()]
    elif(firstkey == b'\r'):
        return "enter"
    elif(firstkey == b'\x1b'):
        return "escape"
    else:
        return firstkey

def generate_game(home_team, away_team):
    #generates the field in ascii art
    grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' '], [' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' '], [' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '▢', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' '], ['|', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '/', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '|'], ['|', '#', '#', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '#', '#', '|'], ['|', '\\', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '/', '|'], ['|', '#', '\\', '#', '#', '#', '#', '#', '/', '#', '#', '#', '#', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '/', '#', '|'], ['|', '#', '#', '\\', '#', '#', '#', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', '#', '#', '#', '/', '#', '#', '|'], ['|', '#', '#', '#', '\\', '#', '/', '#', '#', '#', '#', '/', '-', '\\', '#', '#', '#', '#', '\\', '#', '/', '#', '#', '#', '|'], [' ', '\\', '#', '#', '#', '▢', '#', '#', '#', '#', '#', '|', '▢', '|', '#', '#', '#', '#', '#', '▢', '#', '#', '#', '/', ' '], [' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '\\', '-', '/', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' '], [' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '▢', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '/', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '_', '_', '_', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    #bunch of definitions for variables used later on, in the score comparison for the starting lineup and more
    home_pitches_thrown = away_pitches_thrown = cp_replace_home = cp_replace_away = 0
    current_SP_score = current_CP_score = current_C_score = current_1B_score = current_2B_score = current_3B_score = current_SS_score = current_LF_score = current_CF_score = current_RF_score = current_DH_score = 0
    home_SP = home_CP = home_C = home_1B = home_2B = home_3B = home_SS = home_LF = home_CF = home_RF = home_DH = 0
    home_RP = [] #relief pitcher list for the home team
    home_leftover_pitchers = [] #leftover pitcher list for the home team
    
    for x in range(len(home_team[1])): #determines the active roster for the home team
        if(home_team[1][x][2] == "SP" and home_team[1][x][4] > current_SP_score):
            current_SP_score = home_team[1][x][4]
            home_SP = x
        elif(home_team[1][x][2] == "C" and home_team[1][x][4] > current_C_score):
            current_C_score = home_team[1][x][4]
            home_C = x
        elif(home_team[1][x][2] == "1B" and home_team[1][x][4] > current_1B_score):
            current_1B_score = home_team[1][x][4]
            home_1B = x
        elif(home_team[1][x][2] == "2B" and home_team[1][x][4] > current_2B_score):
            current_2B_score = home_team[1][x][4]
            home_2B = x
        elif(home_team[1][x][2] == "3B" and home_team[1][x][4] > current_3B_score):
            current_3B_score = home_team[1][x][4]
            home_3B = x
        elif(home_team[1][x][2] == "SS" and home_team[1][x][4] > current_SS_score):
            current_SS_score = home_team[1][x][4]
            home_SS = x
        elif(home_team[1][x][2] == "LF" and home_team[1][x][4] > current_LF_score):
            current_LF_score = home_team[1][x][4]
            home_LF = x
        elif(home_team[1][x][2] == "CF" and home_team[1][x][4] > current_CF_score):
            current_CF_score = home_team[1][x][4]
            home_CF = x
        elif(home_team[1][x][2] == "RF" and home_team[1][x][4] > current_RF_score):
            current_RF_score = home_team[1][x][4]
            home_RF = x
        elif(home_team[1][x][2] == "DH" and home_team[1][x][4] > current_DH_score):
            current_DH_score = home_team[1][x][4]
            home_DH = x
        elif(home_team[1][x][2] == "RP"):
            home_RP.append(x) #list of all available relief pitchers
        elif(home_team[1][x][2] == "CP" and home_team[1][x][4] > current_CP_score):
            current_CP_score = home_team[1][x][4]
            home_CP = x
        if(home_team[1][x][2] == "CP" or home_team[1][x][2] == "SP"):
            home_leftover_pitchers.append(x) #leftover pitchers that aren't relief pitchers

    home_leftover_pitchers.remove(home_CP) #remove first-choice CP from leftover pitchers
    home_leftover_pitchers.remove(home_SP) #remove first-choice SP from leftover pitchers
    home_team_defensive_lineup = [home_team[1][home_SP], home_team[1][home_C], home_team[1][home_1B], home_team[1][home_2B], home_team[1][home_3B], home_team[1][home_SS], home_team[1][home_LF], home_team[1][home_CF], home_team[1][home_RF]] #defensive lineup
    home_team_offensive_lineup = [home_team[1][home_C], home_team[1][home_1B], home_team[1][home_2B], home_team[1][home_3B], home_team[1][home_SS], home_team[1][home_LF], home_team[1][home_CF], home_team[1][home_RF], home_team[1][home_DH]] #offensive lineup
    
    #more definitions, same as above
    current_SP_score = current_CP_score = current_C_score = current_1B_score = current_2B_score = current_3B_score = current_SS_score = current_LF_score = current_CF_score = current_RF_score = current_DH_score = 0
    away_SP = away_CP = away_C = away_1B = away_2B = away_3B = away_SS = away_LF = away_CF = away_RF = away_DH = 0
    away_RP = []
    away_leftover_pitchers = []
    
    for x in range(len(away_team[1])): #determines the active lineup for the away team
        if(away_team[1][x][2] == "SP" and away_team[1][x][4] > current_SP_score):
            current_SP_score = away_team[1][x][4]
            away_SP = x
        elif(away_team[1][x][2] == "C" and away_team[1][x][4] > current_C_score):
            current_C_score = away_team[1][x][4]
            away_C = x
        elif(away_team[1][x][2] == "1B" and away_team[1][x][4] > current_1B_score):
            current_1B_score = away_team[1][x][4]
            away_1B = x
        elif(away_team[1][x][2] == "2B" and away_team[1][x][4] > current_2B_score):
            current_2B_score = away_team[1][x][4]
            away_2B = x
        elif(away_team[1][x][2] == "3B" and away_team[1][x][4] > current_3B_score):
            current_3B_score = away_team[1][x][4]
            away_3B = x
        elif(away_team[1][x][2] == "SS" and away_team[1][x][4] > current_SS_score):
            current_SS_score = away_team[1][x][4]
            away_SS = x
        elif(away_team[1][x][2] == "LF" and away_team[1][x][4] > current_LF_score):
            current_LF_score = away_team[1][x][4]
            away_LF = x
        elif(away_team[1][x][2] == "CF" and away_team[1][x][4] > current_CF_score):
            current_CF_score = away_team[1][x][4]
            away_CF = x
        elif(away_team[1][x][2] == "RF" and away_team[1][x][4] > current_RF_score):
            current_RF_score = away_team[1][x][4]
            away_RF = x #away team relief pitcher list
        elif(away_team[1][x][2] == "DH" and away_team[1][x][4] > current_DH_score):
            current_DH_score = away_team[1][x][4]
            away_DH = x
        elif(away_team[1][x][2] == "RP"):
            away_RP.append(x)
        elif(away_team[1][x][2] == "CP" and away_team[1][x][4] > current_CP_score):
            current_CP_score = away_team[1][x][4]
            away_CP = x
        if(away_team[1][x][2] == "CP" or away_team[1][x][2] == "SP"):
            away_leftover_pitchers.append(x) #leftover pitcher list

    away_leftover_pitchers.remove(away_CP) #remove the active CP from the leftover pitcher list
    away_leftover_pitchers.remove(away_SP) #remove the active SP from the leftover pitcher list
    away_team_defensive_lineup = [away_team[1][away_SP], away_team[1][away_C], away_team[1][away_1B], away_team[1][away_2B], away_team[1][away_3B], away_team[1][away_SS], away_team[1][away_LF], away_team[1][away_CF], away_team[1][away_RF]] #deffensive
    away_team_offensive_lineup = [away_team[1][away_C], away_team[1][away_1B], away_team[1][away_2B], away_team[1][away_3B], away_team[1][away_SS], away_team[1][away_LF], away_team[1][away_CF], away_team[1][away_RF], away_team[1][away_DH]] #offensive
    
    home_score = 0 #score of the home team
    away_score = 0 #score of the away team
    inning = 1 #defines which inning it is (whole number = top of the inning, 0.5 = bottom of the inning)
    balls = 0 #current count
    strikes = 0 #current count
    outs = 0 #current count
    man_on_first = [] #defines a list for which player is currently safe on first
    man_on_second = [] #defines a list for which player is currently safe on second
    man_on_third = [] #defines a list for which player is currently safe on third
    home_team_current_batter = 0 #max 8 - index for the batter who is batting for the home team
    away_team_current_batter = 0 #max 8 - index for the batter who is batting for the away team

    #lowkey dont know what this second grid definition does and im too scared to remove it
    grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' '], [' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' '], [' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '▢', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' '], ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], ['|', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '|'], ['|', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', '|'], ['|', ' ', ' ', '\\', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/', ' ', ' ', '|'], ['|', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', ' ', '/', '-', '\\', ' ', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', '|'], [' ', '\\', ' ', ' ', ' ', '▢', ' ', ' ', ' ', ' ', ' ', '|', '▢', '|', ' ', ' ', ' ', ' ', ' ', '▢', ' ', ' ', ' ', '/', ' '], [' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '\\', '-', '/', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' '], [' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '▢', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '_', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    while(True): #infinite loop that plays the entire game
        if(inning == 9.5 and home_score > away_score): #end the game early if the home team is up going into the bottom of the 9th
            break
        if(inning == 10 and home_score != away_score):  #end game after the bottom of the 9th if there is a difference in scores
            break
        if(inning > 9.5 and inning % 1 == 0.5 and home_score != away_score): #end the game if it is the bottom of an inning in extera innings and there is a difference in scores
            break
        if(len(man_on_first) == 1):
            grid[15][19] = 'X' #replaces base on the grid with an X to indicate that a player is on first
        else:
            grid[15][19] = '▢' #returns the plate icon to the grid
        if(len(man_on_second) == 1):
            grid[8][12] = 'X' #replaces base on the grid with an X to indicate that a player is on second
        else:
            grid[8][12] = '▢' #returns the plate icon to the grid
        if(len(man_on_third) == 1):
            grid[15][5] = 'X' #replaces base on the grid with an X to indicate that a player is on third
        else:
            grid[15][5] = '▢' #returns the plate icon to the grid

        time.sleep(2) #artificial pause
        system('cls') #Clears past print in cmd prompt
        grid_length = [len(str(num)) for x in grid for num in x] #takes each row in the grid
        width = max(grid_length) #gets the max width of the grid
        for a in grid:
            a = ''.join(str(num).ljust(width + 1) for num in a)
            print(a) #prints each row

        home_score_tens = int(home_score % 100) // 10 #gets the home score tens place digit
        if(home_score_tens == 0):
            home_score_tens = ' ' #if the digit is zero, replace it with a space
        home_score_ones = int(home_score % 10) #gets the home score ones place digit
        away_score_tens = int(away_score % 100) // 10 #gets the away score tens place digit
        if(away_score_tens == 0):
            away_score_tens = ' ' #if the digit is zero, replace it with a space
        away_score_ones = int(away_score % 10) #gets the away score ones place digit
        
        inning_tens = int(inning % 100) // 10 #gets the inning tens place digit
        if(inning_tens == 0):
            inning_tens = ' ' #if the digit is zero, replace it with a space
        inning_ones = int(inning % 10) #gets the inning ones place digit

        print("-=====-========-================-=========-") #nice boundary line
        if(balls == 0): #prints top part of the scoreboard
            print("| {} |   {}{}   | BALLS:   ○ ○ ○ | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        elif(balls == 1):
            print("| {} |   {}{}   | BALLS:   ● ○ ○ | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        elif(balls == 2):
            print("| {} |   {}{}   | BALLS:   ● ● ○ | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        elif(balls == 3):
            print("| {} |   {}{}   | BALLS:   ● ● ● | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        if(strikes == 0): #prints middle part of the scoreboard
            print("---------------| STRIKES: ○ ○   |   {}{}    |".format(inning_tens, inning_ones))
        elif(strikes == 1):
            print("---------------| STRIKES: ● ○   |   {}{}    |".format(inning_tens, inning_ones))
        elif(strikes == 2):
            print("---------------| STRIKES: ● ●   |   {}{}    |".format(inning_tens, inning_ones))
        if(outs == 0 and (inning % 1) == 0): #prints bottom part of the scoreboard
            print("| {} |   {}{}   | OUTS:    ○ ○   |    ▲    |".format(away_team[0][1], away_score_tens, away_score_ones))
        elif(outs == 1 and (inning % 1) == 0):
            print("| {} |   {}{}   | OUTS:    ● ○   |    ▲    |".format(away_team[0][1], away_score_tens, away_score_ones))
        elif(outs == 2 and (inning % 1) == 0):
            print("| {} |   {}{}   | OUTS:    ● ●   |    ▲    |".format(away_team[0][1], away_score_tens, away_score_ones))
        elif(outs == 0 and (inning % 1) == 0.5):
            print("| {} |   {}{}   | OUTS:    ○ ○   |    ▼    |".format(away_team[0][1], away_score_tens, away_score_ones))
        elif(outs == 1 and (inning % 1) == 0.5):
            print("| {} |   {}{}   | OUTS:    ● ○   |    ▼    |".format(away_team[0][1], away_score_tens, away_score_ones))
        elif(outs == 2 and (inning % 1) == 0.5):
            print("| {} |   {}{}   | OUTS:    ● ●   |    ▼    |".format(away_team[0][1], away_score_tens, away_score_ones))
        print("-=====-========-================-=========-") #nice boundary line
        
        if(inning % 1 == 0): #checks to see if the inning is the top of the inning to know which team is offensive or defensive
            #a pitch is thrown, the hitting function is called, and the pitch count is increased for the home team.
            hit = hitting(away_team_offensive_lineup[away_team_current_batter], home_team_defensive_lineup[0], balls, strikes, home_pitches_thrown, inning)
            time_in_air = hit[3]
            home_pitches_thrown += 1
            if(home_pitches_thrown > random.randint(98, 102) and strikes == 0 and balls == 0): #checks to see if a pitching substitution should be made
                if(len(home_RP) > 0): #makes sure there is RPs to choose from
                    choice = random.choice(home_RP) #chooses a random pitcher from the RP lineup
                    home_RP.remove(choice) #removes the choice from the list
                    print(">> {} replaces Pitcher {} with Pitcher {} <<".format(home_team[0][0], home_team_defensive_lineup[0][0], home_team[1][choice][0])) #announces the pitching substitution
                    time.sleep(2)
                    home_team_defensive_lineup[0] = home_team[1][choice] #substitutes the pitcher
                    home_pitches_thrown = 0 #resets the pitch count
                elif(len(home_leftover_pitchers) > 0): #same code as above but if there isnt any relief pitchers available
                    choice = random.choice(home_leftover_pitchers)
                    home_leftover_pitchers.remove(choice)
                    print(">> {} replaces Pitcher {} with Pitcher {} <<".format(home_team[0][0], home_team_defensive_lineup[0][0], home_team[1][choice][0]))
                    time.sleep(2)
                    home_team_defensive_lineup[0] = home_team[1][choice]
                    home_pitches_thrown = 0
            elif((inning == 9 and strikes == 0 and balls == 0 and cp_replace_home == 0) or (inning == 8 and strikes == 0 and balls == 0 and outs >= 1 and cp_replace_home == 0)): #when to sub in the CP
                print(">> {} replaces Pitcher {} with Pitcher {} <<".format(home_team[0][0], home_team_defensive_lineup[0][0], home_team[1][home_CP][0]))
                time.sleep(2)
                home_team_defensive_lineup[0] = home_team[1][home_CP]
                cp_replace_home = 1
                home_pitches_thrown = 0
        else: #same as above code but for the away team
            hit = hitting(home_team_offensive_lineup[home_team_current_batter], away_team_defensive_lineup[0], balls, strikes, away_pitches_thrown, inning)
            time_in_air = hit[3]
            away_pitches_thrown += 1
            if(away_pitches_thrown > random.randint(98, 102) and strikes == 0 and balls == 0):
                if(len(away_RP) > 0):
                    choice = random.choice(away_RP)
                    away_RP.remove(choice)
                    print(">> {} replaces Pitcher {} with Pitcher {} <<".format(away_team[0][0], away_team_defensive_lineup[0][0], away_team[1][choice][0]))
                    time.sleep(2)
                    away_team_defensive_lineup[0] = away_team[1][choice]
                    away_pitches_thrown = 0
                elif(len(away_leftover_pitchers) > 0):
                    choice = random.choice(away_leftover_pitchers)
                    away_leftover_pitchers.remove(choice)
                    print(">> {} replaces Pitcher {} with Pitcher {} <<".format(away_team[0][0], away_team_defensive_lineup[0][0], away_team[1][choice][0]))
                    time.sleep(2)
                    away_team_defensive_lineup[0] = away_team[1][choice]
                    away_pitches_thrown = 0
            elif((inning == 9 and strikes == 0 and balls == 0 and cp_replace_away == 0) or (inning == 8 and strikes == 0 and balls == 0 and outs >= 1 and cp_replace_away == 0)):
                print(">> {} replaces Pitcher {} with Pitcher {} <<".format(away_team[0][0], away_team_defensive_lineup[0][0], away_team[1][away_CP][0]))
                time.sleep(2)
                away_team_offensive_lineup[0] = away_team[1][away_CP]
                cp_replace_away = 1
                away_pitches_thrown = 0
        
        if(hit[0][0] == "Nohit"): #checks to see if the pitch is a nohit
            balls = hit[1] #gets the ball count from the hitting function
            strikes = hit[2] #gets the strike coutn from the hitting function
        else:
            hit_type = hit[0][0] #0, foul, or homerun
            position = hit[0][1] #which position the ball is hit to
            
            if(inning % 1 == 0): #home team defending, away team on offense
                if(hit_type == "Homerun"):
                    away_score += (1 + len(man_on_first) + len(man_on_second) + len(man_on_third)) #adds to score
                    man_on_first.clear() #clears the bases
                    man_on_second.clear()
                    man_on_third.clear()
                    strikes = balls = 0 #clears counts
                elif(hit_type == "Foul"):
                    if(position == "LF"): #ball is hit foul but is catchable by the left fielder
                        LF_stats = home_team_defensive_lineup[6]
                        fielding_score_LF = (LF_stats[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100)
                        if(random.randint(1, 100) > fielding_score_LF): #error
                            if(strikes != 2):
                                strikes += 1
                        else:
                            outs += 1
                    elif(position == "RF"): #ball is hit foul but is catchable by the right fielder
                        RF_stats = home_team_defensive_lineup[8]
                        fielding_score_RF = (RF_stats[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100)
                        if(random.randint(1, 100) > fielding_score_RF): #error
                            if(strikes != 2):
                                strikes += 1
                        else:
                            outs += 1
                    else:
                        if(strikes != 2):
                            strikes += 1
                elif(hit_type == 0): #check to see if the hit is to a position
                    if(position == "LF"):
                        print("placeholder")
                    elif(position == "CF"):
                        print("placeholder")
                    elif(position == "RF"):
                        print("placeholder")
                    elif(position == "3B"):
                        third_baseman_stats = home_team_defensive_lineup[4][5]
                        second_baseman_stats = home_team_defensive_lineup[3][5]
                        current_batter = away_team_offensive_lineup[away_team_current_batter]
                        fielding_score_3B = (third_baseman_stats[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100)
                        if(len(man_on_first) == 1 and len(man_on_second) == 1 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else:
                                    outs += 1 #tag third for last out
                            elif(outs == 1):
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                elif(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else:
                                    outs += 1 #tag third
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_first[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third.clear()
                                        man_on_second[0] = man_on_first[0]
                                        man_on_first[0] = current_batter
                                        away_score += 1
                                    else: #runner is out at first
                                        outs += 1
                            else:
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                elif(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else:
                                    outs += 1 #tag third
                                    man_on_third.clear()
                                    if(man_on_first[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]): #first base runner is safe at second
                                        man_on_second[0] = man_on_first[0]
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                            man_on_first[0] = current_batter
                                        else: #runner is out at first
                                            outs += 1
                                        away_score += 1
                                    else: #runner is out at second
                                        outs += 1
                                        man_on_second.clear()
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                            man_on_first[0] = current_batter
                                            away_score += 1
                                        else: #runner is out at first
                                            outs += 1
                        elif(len(man_on_first) == 1 and len(man_on_second) == 1 and len(man_on_third) == 0):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third.append(man_on_second[0]) #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else:
                                    outs += 1 #tag third for last out
                            else:
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                elif(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third.append(man_on_second[0]) #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else:
                                    outs += 1 #tag third out
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_first[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]): #first base runner is safe at second
                                        man_on_second[0] = man_on_first[0]
                                        fixed_int = random.randint(0, 99)
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                            man_on_first[0] = current_batter
                                        else:
                                            outs += 1
                                    else:
                                        outs += 1
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                            man_on_first[0] = current_batter
                                        else:
                                            outs += 1
                        elif(len(man_on_first) == 0 and len(man_on_second) == 1 and len(man_on_third) == 1):
                            if(random.randint(1, 100) > fielding_score_3B): #error
                                man_on_third[0] = man_on_second[0] #second advances to third
                                man_on_second.clear()
                                man_on_first.append(current_batter) #batter advances to first
                                away_score += 1
                            else:
                                if(man_on_third[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]): #first base runner is safe at second
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second.clear()
                                    man_on_first.append(current_batter)
                                    away_score += 1
                                else:
                                    outs += 1
                        elif(len(man_on_first) == 1 and len(man_on_second) == 0 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third.clear() #second advances to third
                                    man_on_second.append(man_on_first[0])
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_first[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third.clear()
                                        man_on_second.append(man_on_first[0])
                                        man_on_first[0] = current_batter 
                                        away_score += 1
                                    else:
                                        outs += 1
                            elif(outs == 1):
                                if(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third.clear() #second advances to third
                                    man_on_second.append(man_on_first[0])
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_first[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third.clear()
                                        man_on_second.append(man_on_first[0])
                                        away_score += 1
                                        fixed_int = random.randint(0, 99)
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                            man_on_first[0] = current_batter
                                        else:
                                            outs += 1
                                    else:
                                        outs += 1
                                        fixed_int = random.randint(0, 99)
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                            man_on_first[0] = current_batter
                                        else:
                                            outs += 1
                            else:
                                if(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third.clear() #second advances to third
                                    man_on_second.append(man_on_first[0])
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    man_on_second.append(man_on_first[0])
                                    man_on_first[0] = current_batter #batter advances to first
                                    if(man_on_third[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]):
                                        man_on_third.clear()
                                        away_score += 1
                                    else:
                                        man_on_third.clear()
                                        outs += 1
                        elif(len(man_on_first) == 1 and len(man_on_second) == 0 and len(man_on_third) == 0):
                            if(random.randint(1, 100) > fielding_score_3B): #error
                                man_on_second.append(man_on_first[0])
                                man_on_first[0] = current_batter #batter advances to first
                            else:
                                fixed_int = random.randint(0, 99)
                                if(man_on_first[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]): #first base runner is safe at second
                                    man_on_second.append(man_on_first[0])
                                    away_score += 1
                                    if(current_batter[5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]):
                                        man_on_first[0] = current_batter
                                    else:
                                        outs += 1
                                else:
                                    outs += 1
                                    if(current_batter[5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]):
                                        man_on_first[0] = current_batter
                                    else:
                                        outs += 1
                        elif(len(man_on_first) == 0 and len(man_on_second) == 1 and len(man_on_third) == 0):
                            if(random.randint(1, 100) > fielding_score_3B): #error
                                man_on_third.append(man_on_second[0])
                                man_on_second.clear()
                                man_on_first.append(current_batter) #batter advances to first
                            else:
                                if(current_batter[5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]):
                                    man_on_first.append(current_batter)
                                else:
                                    outs += 1
                        elif(len(man_on_first) == 0 and len(man_on_second) == 0 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_3B): #error
                                    man_on_third.clear()
                                    man_on_first.append(current_batter) #batter advances to first
                                    away_score += 1
                                else:
                                    if(current_batter[5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]):
                                        man_on_first.append(current_batter)
                                    else:
                                        outs += 1
                            else:
                                if(man_on_third[0][5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]):
                                    man_on_third.clear()
                                    man_on_first.append(current_batter)
                                    away_score += 1
                                else:
                                    man_on_third.clear()
                                    man_on_first.append(current_batter)
                                    outs += 1
                        else:
                            if(random.randint(1, 100) > fielding_score_3B): #error
                                man_on_first.append(current_batter) #batter advances to first
                            else:
                                if(current_batter[5][2] >= third_baseman_stats[4] or fixed_int > third_baseman_stats[3]):
                                    man_on_first.append(current_batter)
                                else:
                                    outs += 1

                    elif(position == "SS"):
                        ss_stats = home_team_defensive_lineup[5][5]
                        fielding_score_SS = (ss_stats[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100)
                        if(len(man_on_first) == 1 and len(man_on_second) == 1 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_SS): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else:
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_first[0][5][2] >= ss_stats[4] or fixed_int > ss_stats[3]):
                                        man_on_third[0] = man_on_second[0] #second advances to third
                                        man_on_second[0] = man_on_first[0] #first advances to second
                                        man_on_first[0] = current_batter #batter advances to first
                                        away_score += 1 #increase away team score
                                    else:
                                        outs += 1
                                        man_on_second.clear()
                            elif(outs == 1):
                                if(random.randint(1, 100) > fielding_score_SS): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else:
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_first[0][5][2] >= ss_stats[4] or fixed_int > ss_stats[3]):
                                        man_on_third[0] = man_on_second[0] #second advances to third
                                        man_on_second[0] = man_on_first[0] #first advances to second
                                        away_score += 1 #increase away team score
                                        fixed_int = random.randint(0, 99)
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                            man_on_first[0] = current_batter #batter advances to first
                                        else:
                                            outs += 1
                                            man_on_first.clear()
                                    else:
                                        outs += 1
                                        man_on_third[0] = man_on_second[0] #second advances to third
                                        man_on_second.clear()
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                            man_on_first[0] = current_batter #batter advances to first
                                            away_score += 1
                                        else:
                                            outs += 1
                                            man_on_first.clear()
                            else:
                                if(random.randint(1, 100) > fielding_score_SS): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else:
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_third[0][5][2] >= ss_stats[4] or fixed_int > ss_stats[3]):
                                        man_on_third[0] = man_on_second[0] #second advances to third
                                        man_on_second[0] = man_on_first[0] #first advances to second
                                        man_on_first[0] = current_batter
                                        away_score += 1
                                    else:
                                        man_on_third[0] = man_on_second[0] #second advances to third
                                        man_on_second[0] = man_on_first[0] #first advances to second
                                        man_on_first[0] = current_batter
                                        outs += 1
                    elif(position == "2B"):
                        second_baseman_stats = home_team_defensive_lineup[3][5] #just calling the 2B's stats
                        current_batter = away_team_offensive_lineup[away_team_current_batter] #getting the current batter's stats
                        fielding_score_2B = (second_baseman_stats[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100) #fielding score = (fielding + ((time_in_air - 1.5) // 1.5)) * (99 / 100)
                        if(len(man_on_first) == 1 and len(man_on_second) == 1 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else:
                                    outs += 1 #tag second for last out
                            elif(outs == 1):
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                elif(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else:
                                    outs += 1 #tag second out
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third[0] = man_on_second[0]
                                        man_on_second.clear()
                                        man_on_first[0] = current_batter
                                        away_score += 1
                                    else: #runner is out at first
                                        outs += 1
                            else: #outs == 0
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                elif(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second[0] = man_on_first[0]
                                    man_on_first[0] = current_batter
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    outs += 1 #tags second
                                    if(man_on_third[0][5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                        away_score += 1 #throw to home is unsuccessful, runner scores
                                    else: #throw to home is successful, runner is out
                                        outs += 1
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second.clear()
                                    man_on_first[0] = current_batter
                        elif(len(man_on_first) == 1 and len(man_on_second) == 1 and len(man_on_third) == 0):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third.append(man_on_second[0]) #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else:
                                    outs += 1 #tag second for last out
                            else:
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                elif(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third.append(man_on_second[0]) #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else:
                                    outs += 1 #tag second out
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third.append(man_on_second[0])
                                        man_on_second.clear()
                                        man_on_first[0] = current_batter
                                    else: #runner is out at first
                                        outs += 1
                        elif(len(man_on_first) == 1 and len(man_on_second) == 0 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third.clear()
                                    man_on_second.append(man_on_first[0]) #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else:
                                    outs += 1 #tag second for last out
                            else:
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third.clear()
                                    man_on_second.append(man_on_first[0]) #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else:
                                    outs += 1 #tag second out
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third.clear()
                                        man_on_first[0] = current_batter #batter advances to first
                                        away_score += 1
                                    else: #runner is out at first
                                        outs += 1
                        elif(len(man_on_first) == 0 and len(man_on_second) == 1 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second.clear()
                                    man_on_first.append(current_batter) #batter advances to first
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third[0] = man_on_second[0]
                                        man_on_second.clear()
                                        man_on_first.append(current_batter) #batter advances to first
                                        away_score += 1
                                    else: #runner is out at first
                                        outs += 1
                            else:
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second.clear()
                                    man_on_first.append(current_batter)
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_third[0][5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                        away_score += 1 #throw to home is unsuccessful, runner scores
                                    else: #throw to home is successful, runner is out
                                        outs += 1
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second.clear()
                                    man_on_first.append(current_batter)
                        elif(len(man_on_first) == 1 and len(man_on_second) == 0 and len(man_on_third) == 0):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_second.append(man_on_first[0]) #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else:
                                    outs += 1 #tag second for last out
                            else:
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_second.append(man_on_first[0]) #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else:
                                    outs += 1 #tag second out
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                        man_on_first[0] = current_batter #batter advances to first
                                    else: #runner is out at first
                                        outs += 1
                        elif(len(man_on_first) == 0 and len(man_on_second) == 1 and len(man_on_third) == 0):
                            if(random.randint(1, 100) > fielding_score_2B): #error
                                man_on_third.append(man_on_second[0])
                                man_on_second.clear()
                                man_on_first.append(current_batter) #batter advances to first
                            else:
                                #second wont run to third unless there is an error
                                fixed_int = random.randint(0, 99)
                                #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                    man_on_first.append(current_batter) #batter advances to first
                                else: #runner is out at first
                                    outs += 1
                        elif(len(man_on_first) == 0 and len(man_on_second) == 0 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third.clear()
                                    man_on_first.append(current_batter) #batter advances to first
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                        man_on_third.clear()
                                        man_on_first.append(current_batter) #batter advances to first
                                        away_score += 1
                                    else: #runner is out at first
                                        outs += 1
                            else:
                                if(random.randint(1, 100) > fielding_score_2B): #error
                                    man_on_third.clear()
                                    man_on_first.append(current_batter) #batter advances to first
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    if(man_on_third[0][5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]):
                                        away_score += 1 #throw to home is unsuccessful, runner scores
                                    else: #throw to home is successful, runner is out
                                        outs += 1
                                    man_on_third.clear()
                                    man_on_first.append(current_batter) #batter advances to first
                        else:
                            if(random.randint(1, 100) > fielding_score_2B): #error
                                man_on_first.append(current_batter) #batter advances to first
                            else:
                                fixed_int = random.randint(0, 99)
                                #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #first base runner is safe at second
                                    man_on_first.append(current_batter) #batter advances to first
                                else: #runner is out at first
                                    outs += 1

                    elif(position == "1B"):
                        first_baseman_stats = home_team_defensive_lineup[2][5] #just calling the 1B's stats
                        second_baseman_stats = home_team_defensive_lineup[3][5] #just calling the 2B's stats
                        current_batter = away_team_offensive_lineup[away_team_current_batter] #getting the current batter's stats
                        fielding_score_1B = (first_baseman_stats[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100) #fielding score = (fielding + ((time_in_air - 1.5) // 1.5)) * (99 / 100)
                        if(len(man_on_first) == 1 and len(man_on_second) == 1 and len(man_on_third) == 1): #bases loaded
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else: #tag base for the out
                                    outs += 1
                            elif(outs == 1):
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                    print("INFIELD FLY!")
                                elif(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second[0] = man_on_first[0]
                                    man_on_first[0] = current_batter
                                    away_score += 1
                                else: #catch the ball and go for the double play
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(man_on_first[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]): #first base runner is safe at second
                                            man_on_third[0] = man_on_second[0]
                                            man_on_second[0] = man_on_first[0]
                                            if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                                man_on_first[0] = current_batter #safe
                                            else:
                                                outs += 1
                                            away_score += 1
                                    else: #runner is out
                                        fixed_int = random.randint(0, 99)
                                        man_on_third[0] = man_on_second[0] #runner on second gets to third
                                        man_on_second.clear() #no one on second
                                        outs += 1 #increment out because runner from first to second got out on the throw to second from first
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                            man_on_first[0] = current_batter #safe
                                            away_score += 1 #the man who is running home scores because there is only two outs on the play
                                        else:
                                            outs += 1 #batter is out at first
                            else: #outs == 0
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                    print("INFIELD FLY!")
                                elif(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second[0] = man_on_first[0]
                                    man_on_first[0] = current_batter
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    outs += 1 #tags first
                                    if(man_on_third[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]):
                                        away_score += 1 #throw to home is unsuccessful, runner scores
                                    else: #throw to home is successful, runner is out
                                        outs += 1
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second[0] = man_on_first[0]
                                    man_on_first.clear()
                        elif(len(man_on_first) == 1 and len(man_on_second) == 1 and len(man_on_third) == 0):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.append(man_on_second[0]) #second advances to third
                                    man_on_second[0] = man_on_first[0] #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else: #tag base for the out
                                    outs += 1
                            else: #same action if outs == 0 or outs == 1
                                if(time_in_air >= 3):
                                    outs += 1 #infield fly rule
                                    print("INFIELD FLY!")
                                elif(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.append(man_on_second[0])
                                    man_on_second[0] = man_on_first[0]
                                    man_on_first[0] = current_batter
                                else: #catch the ball and go for the double play
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(man_on_first[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]): #first base runner is safe at second
                                            man_on_third.append(man_on_second[0])
                                            man_on_second[0] = man_on_first[0]
                                            if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                                man_on_first[0] = current_batter #safe
                                            else:
                                                outs += 1
                                    else: #runner is out
                                        fixed_int = random.randint(0, 99)
                                        man_on_third.append(man_on_second[0]) #runner on second gets to third
                                        man_on_second.clear() #no one on second
                                        outs += 1 #increment out because runner from first to second got out on the throw to second from first
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                            man_on_first[0] = current_batter #safe
                                        else:
                                            outs += 1 #batter is out at first
                        elif(len(man_on_first) == 1 and len(man_on_second) == 0 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.clear()
                                    man_on_second.append(man_on_first[0]) #first advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else: #tag base for the out
                                    outs += 1
                            elif(outs == 1):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.clear()
                                    man_on_second.append(man_on_first[0])
                                    man_on_first[0] = current_batter
                                    away_score += 1
                                else: #catch the ball and go for the double play
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(man_on_first[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]): #first base runner is safe at second
                                            man_on_third[0] = man_on_second[0]
                                            man_on_second[0] = man_on_first[0]
                                            if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                                man_on_first[0] = current_batter #safe
                                            else:
                                                outs += 1
                                            away_score += 1
                                    else: #runner is out
                                        fixed_int = random.randint(0, 99)
                                        man_on_third.clear() #runner on third runs for home
                                        man_on_second.clear() #no one on second
                                        outs += 1 #increment out because runner from first to second got out on the throw to second from first
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                            man_on_first[0] = current_batter #safe
                                            away_score += 1 #the man who is running home scores because there is only two outs on the play
                                        else:
                                            outs += 1 #batter is out at first
                            else: #outs == 0
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.clear()
                                    man_on_second[0] = man_on_first[0]
                                    man_on_first[0] = current_batter
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    outs += 1 #tags first
                                    if(man_on_third[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]):
                                        away_score += 1 #throw to home is unsuccessful, runner scores
                                    else: #throw to home is successful, runner is out
                                        outs += 1
                                    man_on_third.clear()
                                    man_on_second[0] = man_on_first[0]
                                    man_on_first.clear()
                        elif(len(man_on_first) == 0 and len(man_on_second) == 1 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third[0] = man_on_second[0] #second advances to third
                                    man_on_second.clear()
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1 #increase away team score
                                else: #tag base for the out
                                    outs += 1
                            else: #same action if outs == 0 or outs == 1
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second.clear()
                                    man_on_first[0] = current_batter
                                    away_score += 1
                                else:
                                    fixed_int = random.randint(0, 99)
                                    outs += 1 #tags first
                                    if(man_on_third[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]):
                                        away_score += 1 #throw to home is unsuccessful, runner scores
                                    else: #throw to home is successful, runner is out
                                        outs += 1
                                    man_on_third[0] = man_on_second[0]
                                    man_on_second.clear()
                                    man_on_first.clear()
                        elif(len(man_on_first) == 1 and len(man_on_second) == 0 and len(man_on_third) == 0):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_second.append(man_on_first[0]) #runner advances to second
                                    man_on_first[0] = current_batter #batter advances to first
                                else: #tag base for the out
                                    outs += 1
                            else: #outs == 0 and outs == 1: same scenario
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_second.append(man_on_first[0])
                                    man_on_first[0] = current_batter
                                else: #catch the ball and go for the double play
                                    fixed_int = random.randint(0, 99)
                                    #compares runner speed to thrower's pitch speed or the fixed int and the thrower's accuracy
                                    if(man_on_first[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]): #first base runner is safe at second
                                            man_on_second.append(man_on_first[0])
                                            if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                                man_on_first[0] = current_batter #safe
                                            else:
                                                outs += 1
                                    else: #runner is out
                                        fixed_int = random.randint(0, 99)
                                        outs += 1 #increment out because runner from first to second got out on the throw to second from first
                                        if(current_batter[5][2] >= second_baseman_stats[4] or fixed_int > second_baseman_stats[3]): #throw from second back to first unsuccessful
                                            man_on_first[0] = current_batter #safe
                                        else:
                                            outs += 1 #batter is out at first
                        elif(len(man_on_first) == 0 and len(man_on_second) == 1 and len(man_on_third) == 0):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.append(man_on_second[0]) #runner advances to second
                                    man_on_second.clear()
                                    man_on_first[0] = current_batter #batter advances to first
                                else: #tag base for the out
                                    outs += 1
                            else: #same as outs == 0 or outs == 1
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.append(man_on_second[0]) #runner advances to second
                                    man_on_second.clear()
                                    man_on_first[0] = current_batter #batter advances to first
                                else: #tag base for the out
                                    outs += 1
                        elif(len(man_on_first) == 0 and len(man_on_second) == 0 and len(man_on_third) == 1):
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.clear()
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else: #tag base for the out
                                    outs += 1
                            else:
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_third.clear()
                                    man_on_first[0] = current_batter #batter advances to first
                                    away_score += 1
                                else: #tag base for the out
                                    fixed_int = random.randint(0, 99)
                                    outs += 1 #tags first
                                    if(man_on_third[0][5][2] >= first_baseman_stats[4] or fixed_int > first_baseman_stats[3]):
                                        away_score += 1 #throw to home is unsuccessful, runner scores
                                    else: #throw to home is successful, runner is out
                                        outs += 1
                                    man_on_third.clear()
                        else: #no one on base
                            if(outs == 2):
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_first.append(current_batter) #batter advances to first
                                else: #tag base for the out
                                    outs += 1
                            else:
                                if(random.randint(1, 100) > fielding_score_1B): #error
                                    man_on_first.append(current_batter) #batter advances to first
                                else: #tag base for the out
                                    outs += 1
                    elif(position == "Pitcher"):
                        print("placeholder")
                    elif(position == "C"):
                        print("placeholder")
            else: #away team defending, home team on offense
                print("COPY-PASTE CODE FROM ABOVE")

        if(balls == 4):
            strikes = 0
            balls = 0
            if(len(man_on_first) == 1):
                if(len(man_on_second) == 1):
                    if(len(man_on_third) == 1):
                        if(inning % 1 == 0):
                            away_score += 1
                        else:
                            home_score += 1
                    else:
                        man_on_third.clear()
                        man_on_third.appeand(man_on_second[0])
                else:
                    man_on_second.clear()
                    man_on_second.appeand(man_on_first[0])
            else:
                man_on_first.clear()
                if(inning % 1 == 0):
                    man_on_first.appeand(away_team_current_batter)
                else:
                    man_on_first.appeand(home_team_current_batter)
            if(inning % 1 == 0):
                away_team_current_batter += 1
                if(away_team_current_batter > 8):
                    away_team_current_batter = 0
            else:
                home_team_current_batter += 1
                if(home_team_current_batter > 8):
                    home_team_current_batter = 0
            
        if(strikes == 3):
            outs += 1
            strikes = 0
            balls = 0
            if(inning % 1 == 0):
                away_team_current_batter += 1
                if(away_team_current_batter > 8):
                    away_team_current_batter = 0
            else:
                home_team_current_batter += 1
                if(home_team_current_batter > 8):
                    home_team_current_batter = 0
 
        if(outs == 3):
            inning += 0.5
            balls = 0
            strikes = 0
            outs = 0
            man_on_first.clear()
            man_on_second.clear()
            man_on_third.clear()
    system('cls')
    print("FINAL SCORE:")
    print("{} - {}".format(home_team[0][0], home_score))
    print("{} - {}".format(away_team[0][0], away_score))
    return (home_score, away_score)

def scrimmage():
    print("")
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
    generate_game(home_team, away_team)
    return

def season(): #WIP
    print("")
    print("Generating Leagues...")
    time.sleep(1)
    leagues = league_generator(current_year)
    print("League Generation Finished!")
    time.sleep(0.5)
    system('cls') #Clears past print in cmd prompt
    print("Creating Regular Season Schedule")
    return

df = random.randint(0, 9999)
selection_state = 0
system('cls')
if(df == 2006):
    screen_df = 1
    winsound.PlaySound("resources/sound/df.wav", winsound.SND_ASYNC | winsound.SND_LOOP | winsound.SND_FILENAME)
    print("\u001b[31mSlaves to Armok: God of Blood\u001b[0m")
    print("Chapter III: Baseball")
    print("")
    print("Dwarf Fortress <<")
    print("Adventurer")
else:
    screen_df = 0
    winsound.PlaySound("resources/sound/yes.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)
    print("\u001b[32mRyan's Insane Baseball Simulator\u001b[0m")
    print("Scrimmage Mode <<")
    print("Season Mode")

while True:
    keyboard_input = getkey()
    if(keyboard_input == 'escape'):
        sys.exit()
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
    elif(keyboard_input == 'enter' or keyboard_input == 'space'):
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
            winsound.PlaySound(None, winsound.SND_PURGE)
            system('cls')
            scrimmage()