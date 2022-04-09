import random
from person_generation import person_generator

def team_generator(city, team_name, current_year):
    if(len(city[1]) == 1): #checks to see if the city abbreviation is only 1 character
        abbreviation = city[1] + team_name[0].capitalize() + team_name[1].capitalize() #adds the team's first two letters to the 1 character city abbreviation
    elif(len(city[1]) == 2): #checks to see if the city abbreviation is only 2 characters
        abbreviation = city[1] + team_name[0].capitalize() #adds the team name's first letter to the 2 characters of the city abbreviation
    else: #if the city abbreviation is greater than 3 characters
        abbreviation = city[1][0] + city[1][1] + city[1][2] #combines the first three characters of the abbreviation
    team_name = [(city[0] + ' ' + team_name), abbreviation]
    
    #normalish distribution of positions of a 26 man roster
    count_SP = 5
    count_RP = 5
    count_CP = 2
    count_1B = 1
    count_2B = 2
    count_3B = 2
    count_SS = 1
    count_LF = 2
    count_CF = 1
    count_RF = 2
    count_C = 2
    count_DH = 1

    roster = [] #creates the active roster list
    while(count_SP > 0 or count_RP > 0 or count_CP > 0 or count_1B > 0 or count_2B > 0 or count_3B > 0 or count_SS > 0 or count_LF > 0 or count_CF > 0 or count_RF > 0 or count_C > 0 or count_DH > 0):
        #a while loop that makes sure each position is field by generating random characters and fitting them into the active roster
        player = person_generator(current_year) #name, birthday, primary_position, secondary_position, combined_stats, stats, personality_traits, pitch_types
        if(player[2] == "SP" and count_SP > 0):
            roster.append(player)
            count_SP -= 1
        elif(player[2] == "RP" and count_RP > 0):
            roster.append(player)
            count_RP -= 1
        elif(player[2] == "CP" and count_CP > 0):
            roster.append(player)
            count_CP -= 1
        elif(player[2] == "1B" and count_1B > 0):
            roster.append(player)
            count_1B -= 1
        elif(player[2] == "2B" and count_2B > 0):
            roster.append(player)
            count_2B -= 1
        elif(player[2] == "3B" and count_3B > 0):
            roster.append(player)
            count_3B -= 1
        elif(player[2] == "SS" and count_SS > 0):
            roster.append(player)
            count_SS -= 1
        elif(player[2] == "LF" and count_LF > 0):
            roster.append(player)
            count_LF -= 1
        elif(player[2] == "CF" and count_CF > 0):
            roster.append(player)
            count_CF -= 1
        elif(player[2] == "RF" and count_RF > 0):
            roster.append(player)
            count_RF -= 1
        elif(player[2] == "C" and count_C > 0):
            roster.append(player)
            count_C -= 1
        elif(player[2] == "DH" and count_DH > 0):
            roster.append(player)
            count_DH -= 1
    return [team_name, roster]

def league_generator(current_year):
    cities = [("New York", "NY"), ("Los Angeles", "LA"), ("Chicago", "CHI"), ("Houston", "HOU"), ("Phoenix", "PHX"), ("Philadelphia", "PHI"), ("San Antonio", "SA"), ("San Diego", "SD"), ("Dallas", "DAL"), ("San Jose", "SJ"), ("Fort Worth", "FW"), ("Jacksonville", "JXV"), ("Columbus", "COL"), ("Charlotte", "CHO"), ("Indianapolis", "IND"), ("San Francisco", "SF"), ("Seattle", "SEA"), ("Denver", "DEN"), ("Washington", "WAS"), ("Boston", "BOS"), ("El Paso", "ELP"), ("Nashville", "NAS"), ("Oklahoma City", "OKC"), ("Las Vegas", "LV"), ("Detroit", "DET"), ("Portland", "POR"), ("Memphis", "MEM"), ("Louisville", "LOV"), ("Milwaukee", "MIL"), ("Baltimore", "BAL"), ("Albuquerque", "ALB"), ("Tucson", "TUC"), ("Mesa", "MES"), ("Fresno", "FRS"), ("Sacramento", "SAC"), ("Atlanta", "ATL"), ("Kansas City", "KC"), ("Miami", "MIA"), ("Oakland", "OAK"), ("New Orleans", "NO"), ("Honolulu", "HON"), ("Newark", "NEK"), ("Cincinnati", "CIN")]
    team_names = ["Reacharounds", "Comets", "Snakes", "Stark", "Knights", "Enchanted", "Novas", "Tornadoes", "Shades", "Jackals", "Enigmas", "Moons", "Boomers", "Claws", "Kings", "Boomerangs", "Sparks", "Aces", "Ghosts", "Runners", "Imps", "Legends", "Vikings", "Goblins", "Orcas", "Stallions", "Lucky", "Ninjas", "Furies", "Crusaders", "Beavers", "Gifted", "Robots", "Jesters", "Prowlers", "Crocs", "Robins", "Nightingales", "Martians", "Warhawks", "Grave", "Titans", "Spikes", "Demons", "Yetis", "Blues", "Pythons", "Spiders", "Agents"]
    conference_names = [("American League", "National League"), ("Central League", "Pacific League"), ("Eastern League", "Western League")] #im really uncreative
    conferences = random.choice(conference_names) #chooses one of the random tuples in the list of conferences

    conference1 = conferences[0] #label conference 1 as the first conference name in the tuple
    conference1_team_counts = 15 #define the amount of teams in the conference
    conference1_team_list = []
    while(conference1_team_counts > 0): #while not all the teams are filled in a conference
        team_name_choice = random.choice(team_names) #choose a random team name from the list of team names
        team_names.remove(team_name_choice) #remove the name from the list of team names so no 2 teams can have the same name
        city_choice = random.choice(cities) #choose a random city from the list of cities
        cities.remove(city_choice) #remove the city from the list of cities (while not realistic, i dont want 5 teams in NY, and im too lazy to figure out a better way right now)
        conference1_team_list.append(team_generator(city_choice, team_name_choice, current_year)) #generate a team
        conference1_team_counts -= 1 #remove the team count after one is successfully generated and added to the list

    conference2 = conferences[1] #same code as above but for the other conference
    conference2_team_counts = 15
    conference2_team_list = []
    while(conference2_team_counts > 0):
        team_name_choice = random.choice(team_names)
        team_names.remove(team_name_choice)
        city_choice = random.choice(cities)
        cities.remove(city_choice)
        conference2_team_list.append(team_generator(city_choice, team_name_choice, current_year))
        conference2_team_counts -= 1
    
    return [[conference1, conference1_team_list], [conference2, conference2_team_list]]