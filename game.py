import random
import time
from os import system
from physics import hitting
from fielding import fielding

def generate_game(home_team, away_team, debug=0):
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
            strikes = hit[2] #gets the strike count from the hitting function
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
                    strikes = balls = 0
                    #fielding output = [score_increase, men_on_bases, outs, message]
                    fielding_output = fielding(home_team_defensive_lineup, time_in_air, outs, [man_on_first, man_on_second, man_on_third], position, away_team_offensive_lineup[away_team_current_batter])
                    away_score += fielding_output[0]
                    man_on_first = fielding_output[1][0]
                    man_on_second = fielding_output[1][1]
                    man_on_third = fielding_output[1][2]
                    outs = fielding_output[2]
                    #print(">> {} <<".format(fielding_output[3]))
            else: #away team defending, home team on offense
                if(hit_type == "Homerun"):
                    home_score += (1 + len(man_on_first) + len(man_on_second) + len(man_on_third)) #adds to score
                    man_on_first.clear() #clears the bases
                    man_on_second.clear()
                    man_on_third.clear()
                    strikes = balls = 0 #clears counts
                elif(hit_type == "Foul"):
                    if(position == "LF"): #ball is hit foul but is catchable by the left fielder
                        LF_stats = away_team_defensive_lineup[6]
                        fielding_score_LF = (LF_stats[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100)
                        if(random.randint(1, 100) > fielding_score_LF): #error
                            if(strikes != 2):
                                strikes += 1
                        else:
                            outs += 1
                    elif(position == "RF"): #ball is hit foul but is catchable by the right fielder
                        RF_stats = away_team_defensive_lineup[8]
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
                    strikes = balls = 0
                    #fielding output = [score_increase, men_on_bases, outs, message]
                    fielding_output = fielding(away_team_defensive_lineup, time_in_air, outs, [man_on_first, man_on_second, man_on_third], position, home_team_offensive_lineup[home_team_current_batter])
                    away_score += fielding_output[0]
                    man_on_first = fielding_output[1][0]
                    man_on_second = fielding_output[1][1]
                    man_on_third = fielding_output[1][2]
                    outs = fielding_output[2]
                    #print(">> {} <<".format(fielding_output[3]))
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
                        man_on_third.append(man_on_second[0])
                else:
                    man_on_second.clear()
                    man_on_second.append(man_on_first[0])
            else:
                man_on_first.clear()
                if(inning % 1 == 0):
                    man_on_first.append(away_team_current_batter)
                else:
                    man_on_first.append(home_team_current_batter)
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