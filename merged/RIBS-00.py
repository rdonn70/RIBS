import random
import time
from os import system, name

def clear():
	if name == 'nt': # for windows
		_ = system('cls')
	else: # for mac and linux
		_ = system('clear')

def generate_name():
    first_names = ["James", "Robert", "John", "Michael", "William", "David", "Richard", "Thomas", "Charles", "Christopher", "Daniel",
                   "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian", "George",
                   "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen",
                   "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Gregory", "Frank", "Alexander", "Raymond", "Patrick",
                   "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Adam", "Henry", "Nathan", "Douglas", "Zachary", "Peter", "Kyle",
                   "Walter", "Ethan", "Jeremy", "Harold", "Keith", "Christian", "Roger", "Noah", "Gerald", "Carl", "Terry", "Sean", 
                   "Austin", "Arthur", "Lawrence", "Jesse", "Dylan", "Bryan", "Joe", "Jordan", "Billy", "Bruce", "Albert", "Willie", 
                   "Gabriel", "Logan", "Alan", "Juan", "Wayne", "Roy", "Ralph", "Randy", "Eugene", "Vincent", "Russell", "Elijah", 
                   "Louis", "Bobby", "Philip", "Johnny", "Arman", "Gino"]
    last_names = ["Blackmond", "Brinlee", "Everly", "Mclean", "Rozmus", "Fabian", "Ricklefs", "Lisiecki", "Gowen", "Lainhart", "Tague",
                  "Boldwyn", "Gowen", "Guterriez", "Averill", "Brage", "Herrold", "Silvaggio", "Pomberg", "Linard", "Baymon", "Cipolone",
                  "Martinez", "Viney", "Sampaga", "Smith", "Jonhson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez",
                  "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright",
                  "Scott", "Torres", "Hill", "Flores", "Green", "Adams", "Nelson", "Nguyen", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
                  "Carter", "Roberts", "Johnson"]
    name = random.choice(first_names) + ' ' + random.choice(last_names)
    return name

def person_generator():
    name = generate_name()
    age = int(abs(random.normalvariate(28.20787, 3.564317)))
    general_position = random.choices(["IF", "OF", "C", "P", "DH"], weights=[20.95722, 16.31617, 7.976795, 54.02466, 0.725163])[0]
    if(general_position == "IF"):
        primary_position = random.choices(["1B", "2B", "3B", "SS"], weights=[21.79931, 36.33218, 20.0692, 21.79931])[0]
        secondary_list = ["1B", "2B", "3B", "SS", "None"]
        secondary_list.remove(primary_position)
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["LF", "CF", "RF", "C", "DH"])
        else:
            secondary_position = random.choice(secondary_list)
    elif(general_position == "OF"):
        primary_position = random.choice(["LF", "CF", "RF"])
        secondary_list = ["LF", "CF", "RF", "None"]
        secondary_list.remove(primary_position)
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["1B", "2B", "3B", "SS", "DH"])
        else:
            secondary_position = random.choice(secondary_list)
    elif(general_position == "C"):
        primary_position = "C"
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["1B", "LF", "CF", "RF", "DH"])
        else:
            secondary_position = random.choice(["None", "DH"])
    elif(general_position == "P"):
        primary_position = random.choice(["SP", "RP", "CP"])
        secondary_list = ["SP", "RP", "CP", "None"]
        secondary_list.remove(primary_position)
        secondary_position = random.choice(secondary_list)
    elif(general_position == "DH"):
        primary_position = "DH"
        secondary_position = "None"
    else:
        primary_position = random.choice["IF", "OF", "C", "P", "DH"]
        
    stats = ["power", "contact", "speed", "throw_accuracy", "throw_speed", "fielding"]
    personality_traits = ['hard-working', 'punctual', 'conformist', 'active', 'trusting', 'lenient', 'good-natured', 'temperamental', 'self-conscious', 'emotional']

    #hard-working = 1 - 2 % increase in all stats
    #punctual = if zero, have a 2.5% chance of not showing up for a game
    #conformist = if one, team morale +1%. if zero, team morale -1%
    #active = if one, 1 - 2 % increase in all stats. if zero, 1 - 2 % decrease in all stats.
    #trusting = if one, team morale +1%. if zero, team morale -1%
    #lenient = if one, team morale +1%. if zero, team morale -1%
    #good-natured = if one, team morale +2%. if zero, team morale -5%
    #temperamental = if one, random chance to either have a 1 - 2% decrease in hitting if strikeout or have a 1 - 2 % increase in hitting if strikeout
    #self-conscious = if one, 1 - 2% decrease in hitting and catching
    #emotional = if one, 2 - 4% decrease in stats if error/strikeout/doubleplay/tripleplay

    for y in range(len(personality_traits)):
        personality_traits[y] = random.randint(0, 1)
    for x in range(len(stats)):
        stats[x] = random.randint(39, 89)
        if(personality_traits[3] == 1):
            stats[x] += random.randint(2, 5)
        else:
            stats[x] -= random.randint(2, 5)
        if(personality_traits[0] == 1):
            stats[x] += random.randint(2, 5)
    if(personality_traits[8] == 1):
        stats[0] -= random.randint(2, 5)
        stats[1] -= random.randint(2, 5)
        stats[5] -= random.randint(2, 5)
    if(primary_position == "DH"):
        stats[0] += random.randint(5, 8)
        stats[1] += random.randint(5, 8)
        stats[2] -= random.randint(5, 10)
        stats[3] -= random.randint(5, 10)
        stats[4] -= random.randint(5, 10)
    if(secondary_position == "DH"):
        stats[0] += random.randint(5, 8)
        stats[1] += random.randint(5, 8)
    if(primary_position in ["SP", "RP", "CP"]):
        stats[0] -= random.randint(30, 50)
        stats[1] -= random.randint(30, 50)
        stats[2] -= random.randint(15, 25)
        stats[3] += random.randint(15, 25)
        stats[4] += random.randint(15, 25)
        stats[5] += random.randint(2, 5)
    for z in range(len(stats)):
        if(stats[z] > 99):
            coin_toss = random.randint(0, 1)
            if(coin_toss == 0):
                stats[z] = 99
            else:
                stats[z] = 99 - random.randint(1, 4)
        if(stats[z] < 0):
            coin_toss = random.randint(0, 1)
            if(coin_toss == 0):
                stats[z] = 0
            else:
                stats[z] = 0 + random.randint(1, 4)
    combined_stats = 0
    for n in stats:
        combined_stats += n
    
    pitches = ["Four-seam fastball", "Two-seam fastball", "Cut-fastball", "Split-finger fastball", "Change-up", "Curveball", "Slider", "Knuckleball", "Forkball"]
    if(primary_position == "SP"):
        kv = random.randint(3, 4)
        pitch_types = []
        while(len(pitch_types) < kv):
            pitch = random.choices(pitches, k=1, weights=[50, 7.5, 7.5, 4, 7.5, 7.5, 7.5, 1, 7.5])
            if(pitch not in pitch_types):
                pitch_types.append(pitch)
    elif(primary_position == "RP" or primary_position == "CP"):
        kv = random.randint(2, 3)
        pitch_types = []
        while(len(pitch_types) < kv):
            pitch = random.choices(pitches, k=1, weights=[50, 7.5, 7.5, 4, 7.5, 7.5, 7.5, 1, 7.5])
            if(pitch not in pitch_types):
                pitch_types.append(pitch)
    else:
        randomness = random.randint(0, 99)
        pitch_types = ["Four-seam fastball"]
        if(randomness == 99):
            pitches.remove("Four-seam fastball")
            pitch_types.append(random.choice(pitches))

    return [name, age, primary_position, secondary_position, combined_stats, stats, personality_traits, pitch_types]

def team_generator(city, team_name):
    if(len(city[1]) == 2):
        abbreviation = city[1] + team_name[0].capitalize()
    else:
        abbreviation = city[1]
    team_name = [(city[0] + ' ' + team_name), abbreviation]
    
    count_SP = 4
    count_RP = 6
    count_CP = 3
    count_1B = 1
    count_2B = 2
    count_3B = 1
    count_SS = 1
    count_LF = 2
    count_CF = 1
    count_RF = 2
    count_C = 2
    count_DH = 1
    
    roster = []
    while(count_SP > 0 or count_RP > 0 or count_CP > 0 or count_1B > 0 or count_2B > 0 or count_3B > 0 or count_SS > 0 or count_LF > 0 or count_CF > 0 or count_RF > 0 or count_C > 0 or count_DH > 0):
        player = person_generator()
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

def league_generator():
    cities = [("New York", "NY"), ("Los Angeles", "LA"), ("Chicago", "CHI"), ("Houston", "HOU"), ("Phoenix", "PHX"), ("Philadelphia", "PHI"), ("San Antonio", "SA"), ("San Diego", "SD"), ("Dallas", "DAL"), ("San Jose", "SJ"), ("Fort Worth", "FW"), ("Jacksonville", "JXV"), ("Columbus", "COL"), ("Charlotte", "CHO"), ("Indianapolis", "IND"), ("San Francisco", "SF"), ("Seattle", "SEA"), ("Denver", "DEN"), ("Washington", "WAS"), ("Boston", "BOS"), ("El Paso", "ELP"), ("Nashville", "NAS"), ("Oklahoma City", "OKC"), ("Las Vegas", "LV"), ("Detroit", "DET"), ("Portland", "POR"), ("Memphis", "MEM"), ("Louisville", "LOV"), ("Milwaukee", "MIL"), ("Baltimore", "BAL"), ("Albuquerque", "ALB"), ("Tucson", "TUC"), ("Mesa", "MES"), ("Fresno", "FRS"), ("Sacramento", "SAC"), ("Atlanta", "ATL"), ("Kansas City", "KC"), ("Miami", "MIA"), ("Oakland", "OAK"), ("New Orleans", "NO"), ("Honolulu", "HON"), ("Newark", "NEK"), ("Cincinnati", "CIN")]
    team_names = ["Reacharounds", "Comets", "Snakes", "Stark", "Knights", "Enchanted", "Novas", "Tornadoes", "Shades", "Jackals", "Enigmas", "Moons", "Boomers", "Claws", "Kings", "Boomerangs", "Sparks", "Aces", "Ghosts", "Runners", "Imps", "Legends", "Vikings", "Goblins", "Orcas", "Stallions", "Lucky", "Ninjas", "Furies", "Crusaders", "Beavers", "Gifted", "Robots", "Jesters", "Prowlers", "Crocs", "Robins", "Nightingales", "Martians", "Warhawks", "Grave", "Titans", "Spikes", "Demons", "Yetis", "Blues", "Pythons", "Spiders", "Agents"]
    conference_names = [("American League", "National League")]
    
    conferences = random.choice(conference_names)
    conference1 = conferences[0]
    conference1_team_counts = 15
    conference1_team_list = []
    while(conference1_team_counts > 0):
        team_name_choice = random.choice(team_names)
        team_names.remove(team_name_choice)
        city_choice = random.choice(cities)
        cities.remove(city_choice)
        conference1_team_list.append(team_generator(city_choice, team_name_choice))
        conference1_team_counts -= 1
    conference2 = conferences[1]
    conference2_team_counts = 15
    conference2_team_list = []
    while(conference2_team_counts > 0):
        team_name_choice = random.choice(team_names)
        team_names.remove(team_name_choice)
        city_choice = random.choice(cities)
        cities.remove(city_choice)
        conference2_team_list.append(team_generator(city_choice, team_name_choice))
        conference2_team_counts -= 1
    
    return [[conference1, conference1_team_list], [conference2, conference2_team_list]]

def hitting(batter, pitcher, balls=0, strikes=0):
    pitcher_accuracy = pitcher[5][3]
    pitcher_throw_speed = pitcher[5][4]
    pitcher_available_pitches = pitcher[7]
    
    batter_power = batter[5][0]
    batter_contact = batter[5][1]
    batter_speed = batter[5][2]
    
    thrown_pitch = random.choice(pitcher_available_pitches)
    if(thrown_pitch == "Four-seam fastball"):
        pitch_speed = random.normalvariate(93.0929, 2.365829) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        pitch_accuracy = random.randint(75, 92) + (93.0929 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    elif(thrown_pitch == "Two-seam fastball"):
        pitch_speed = random.normalvariate(92.73333, 2.588234) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        pitch_accuracy = random.randint(72, 88) + (92.73333 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    elif(thrown_pitch == "Cut-fastball"):
        pitch_speed = random.normalvariate(88.18714, 2.635319) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        pitch_accuracy = random.randint(62, 80) + (88.18714 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    elif(thrown_pitch == "Split-finger fastball"):
        pitch_speed = random.normalvariate(86.2875, 1.852161) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        pitch_accuracy = random.randint(64, 82) + (86.2875 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    elif(thrown_pitch == "Change-up"):
        pitch_speed = random.normalvariate(85.36199, 3.100857) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        pitch_accuracy = random.randint(75, 88) + (85.36199 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    elif(thrown_pitch == "Curveball"):
        pitch_speed = random.normalvariate(78.33789, 3.560038) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        pitch_accuracy = random.randint(77, 90) + (78.33789 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    elif(thrown_pitch == "Slider"):
        pitch_speed = random.normalvariate(84.48121, 3.207832) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        pitch_accuracy = random.randint(70, 85) + (84.48121 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    elif(thrown_pitch == "Knuckleball"):
        pitch_speed = random.normalvariate(70.30231, 4.059382) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        # this is made up because who the fuck throws knuckleballs in the majors
        pitch_accuracy = random.randint(50, 75) + (70.30231 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    else:
        pitch_speed = random.normalvariate(80.45333, 3.024301) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        # this is also made up
        pitch_accuracy = random.randint(55, 75) + (80.45333 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))

    if(balls == 3):
        pitch_intention = 1 # 0 = outside, 1 = inside
    elif(strikes == 0 and balls == 0):
        if(random.randint(1, 100) > 40):
            pitch_intention = 1
        else:
            pitch_intention = 0
    else:
        pitch_intention = random.randint(0, 1)
    if(pitch_intention == 1):
        if(random.randint(1, 100) > pitch_accuracy):
            in_strike_zone = 0 #not in the strike zone
        else:
            in_strike_zone = 1
    else:
        if(random.randint(1, 100) > pitch_accuracy):
            in_strike_zone = 1
        else:
            in_strike_zone = 0
    
    #checks to see if batter swings
    if(in_strike_zone == 1):
        if(random.randint(1, 100) > 32):
            swing = 1
        else:
            swing = 0
    else:
        if(random.randint(1, 100) > 69):
            swing = 1
        else:
            swing = 0
    
    hit = ["Nohit", "Nohit", "Nohit"]
    
    if(swing == 1 and in_strike_zone == 1):
        z_contact_percent = 84
        z_contact_modified = ((z_contact_percent - batter_contact) // 2) + z_contact_percent
        if(random.randint(1, 100) > (100 - z_contact_modified)):
            hit_power = batter_power + (random.randint(-1, 1) * (random.randint(1, 10)))
            if(hit_power < 0):
                hit_power = 0
            elif(hit_power > 99):
                hit_power = 99
            hit_angle_horizontal = random.randint(0, 180)
            hit_angle_vertical = random.randint(-90, 90)
            hit = [hit_power, hit_angle_horizontal, hit_angle_vertical]
        else:
            strikes +=1
    elif(swing == 1 and in_strike_zone == 0):
        o_contact_percent = 62
        o_contact_modified = ((o_contact_percent - batter_contact) // 2) + o_contact_percent
        if(random.randint(1, 100) > (100 - o_contact_modified)):
            hit_power = batter_power - (random.randint(1, 10))
            if(hit_power < 0):
                hit_power = 0
            elif(hit_power > 99):
                hit_power = 99
            hit_angle_horizontal = random.randint(0, 180)
            hit_angle_vertical = random.randint(-90, 90)
            hit = [hit_power, hit_angle_horizontal, hit_angle_vertical]
        else:
            strikes += 1
    elif(swing == 0 and in_strike_zone == 1):
        strikes +=1
    elif(swing == 0 and in_strike_zone == 0):
        balls += 1
    else:
        strikes += 1
    
    return (hit, balls, strikes)

def generate_game(home_team, away_team):
    grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' ', ' '], [' ', ' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' ', ' '], [' ', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '▢', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', ' '], ['|', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '/', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '|'], ['|', '#', '#', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '#', '#', '|'], ['|', '\\', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '/', '|'], ['|', '#', '\\', '#', '#', '#', '#', '#', '/', '#', '#', '#', '#', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '/', '#', '|'], ['|', '#', '#', '\\', '#', '#', '#', '/', '#', '#', '#', '#', '#', '#', '#', '#', '#', '\\', '#', '#', '#', '/', '#', '#', '|'], ['|', '#', '#', '#', '\\', '#', '/', '#', '#', '#', '#', '/', '-', '\\', '#', '#', '#', '#', '\\', '#', '/', '#', '#', '#', '|'], [' ', '\\', '#', '#', '#', '▢', '#', '#', '#', '#', '#', '|', '▢', '|', '#', '#', '#', '#', '#', '▢', '#', '#', '#', '/', ' '], [' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '\\', '-', '/', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' '], [' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '#', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '\\', '#', '/', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '▢', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '#', '#', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '#', '#', '#', '/', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '_', '_', '_', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    current_SP_score = current_C_score = current_1B_score = current_2B_score = current_3B_score = current_SS_score = current_LF_score = current_CF_score = current_RF_score = current_DH_score = 0
    home_SP = home_C = home_1B = home_2B = home_3B = home_SS = home_LF = home_CF = home_RF = home_DH = 0
    for x in range(len(home_team[1])):
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

    home_team_defensive_lineup = [home_team[1][home_SP], home_team[1][home_C], home_team[1][home_1B], home_team[1][home_2B], home_team[1][home_3B], home_team[1][home_SS], home_team[1][home_LF], home_team[1][home_CF], home_team[1][home_RF]]
    home_team_offensive_lineup = [home_team[1][home_C], home_team[1][home_1B], home_team[1][home_2B], home_team[1][home_3B], home_team[1][home_SS], home_team[1][home_LF], home_team[1][home_CF], home_team[1][home_RF], home_team[1][home_DH]]
    
    current_SP_score = current_C_score = current_1B_score = current_2B_score = current_3B_score = current_SS_score = current_LF_score = current_CF_score = current_RF_score = current_DH_score = 0
    
    away_SP = away_C = away_1B = away_2B = away_3B = away_SS = away_LF = away_CF = away_RF = away_DH = 0
    for x in range(len(away_team[1])):
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
            away_RF = x
        elif(away_team[1][x][2] == "DH" and away_team[1][x][4] > current_DH_score):
            current_DH_score = away_team[1][x][4]
            away_DH = x

    away_team_defensive_lineup = [away_team[1][away_SP], away_team[1][away_C], away_team[1][away_1B], away_team[1][away_2B], away_team[1][away_3B], away_team[1][away_SS], away_team[1][away_LF], away_team[1][away_CF], away_team[1][away_RF]]
    away_team_offensive_lineup = [away_team[1][away_C], away_team[1][away_1B], away_team[1][away_2B], away_team[1][away_3B], away_team[1][away_SS], away_team[1][away_LF], away_team[1][away_CF], away_team[1][away_RF], away_team[1][away_DH]]
    
    home_score = 0
    away_score = 0
    inning = 1
    balls = 0
    strikes = 0
    outs = 0
    man_on_first = 0
    man_on_second = 0
    man_on_third = 0
    home_team_current_batter = 0 #max 8
    away_team_current_batter = 0 #max 8

    grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' '], [' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' '], [' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '▢', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' '], ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], ['|', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '|'], ['|', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', '|'], ['|', ' ', ' ', '\\', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/', ' ', ' ', '|'], ['|', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', ' ', '/', '-', '\\', ' ', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', '|'], [' ', '\\', ' ', ' ', ' ', '▢', ' ', ' ', ' ', ' ', ' ', '|', '▢', '|', ' ', ' ', ' ', ' ', ' ', '▢', ' ', ' ', ' ', '/', ' '], [' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '\\', '-', '/', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' '], [' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '\\', ' ', '/', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '▢', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', '/', '', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '_', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    while(home_score == away_score or inning <= 9.5):
        if(inning == 9.5 and home_score > away_score):
            break
        if(inning > 9.5 and inning % 1 == 0.5 and home_score != away_score):
            break
        if(man_on_first == 1):
            grid[15][19] = 'X'
        else:
            grid[15][19] = '▢'
        if(man_on_second == 1):
            grid[8][12] = 'X'
        else:
            grid[8][12] = '▢'
        if(man_on_third == 1):
            grid[15][5] = 'X'
        else:
            grid[15][5] = '▢'

        time.sleep(2)
        clear() #Clears past print in cmd prompt
        grid_length = [len(str(num)) for x in grid for num in x]
        width = max(grid_length)
        for a in grid:
            a = ''.join(str(num).ljust(width + 1) for num in a)
            print(a)

        home_score_tens = int(home_score % 100) // 10
        if(home_score_tens == 0):
            home_score_tens = ' '
        home_score_ones = int(home_score % 10)
        away_score_tens = int(away_score % 100) // 10
        if(away_score_tens == 0):
            away_score_tens = ' '
        away_score_ones = int(away_score % 10)

        inning_tens = int(inning % 100) // 10
        if(inning_tens == 0):
            inning_tens = ' '
        inning_ones = int(inning % 10)

        print("-=====-========-================-=========-")
        if(balls == 0):
            print("| {} |   {}{}   | BALLS:   ○ ○ ○ | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        elif(balls == 1):
            print("| {} |   {}{}   | BALLS:   ● ○ ○ | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        elif(balls == 2):
            print("| {} |   {}{}   | BALLS:   ● ● ○ | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        elif(balls == 3):
            print("| {} |   {}{}   | BALLS:   ● ● ● | INNING: |".format(home_team[0][1], home_score_tens, home_score_ones))
        if(strikes == 0):
            print("---------------| STRIKES: ○ ○   |   {}{}    |".format(inning_tens, inning_ones))
        elif(strikes == 1):
            print("---------------| STRIKES: ● ○   |   {}{}    |".format(inning_tens, inning_ones))
        elif(strikes == 2):
            print("---------------| STRIKES: ● ●   |   {}{}    |".format(inning_tens, inning_ones))
        if(outs == 0 and (inning % 1) == 0):
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
        print("-=====-========-================-=========-")
        
        if(inning % 1 == 0):
            hit = hitting(away_team_offensive_lineup[away_team_current_batter], home_team_defensive_lineup[0], balls, strikes)
        else:
            hit = hitting(home_team_offensive_lineup[home_team_current_batter], away_team_defensive_lineup[0], balls, strikes)
        
        if(hit[0][0] == "Nohit"):
            balls = hit[1]
            strikes = hit[2]
        else:
            hit_power = hit[0][0]
            hit_angle_horizontal = hit[0][1]
            hit_angle_vertical = hit[0][2]
            if(hit_angle_horizontal <= 45 or hit_angle_horizontal >= 120):
                hit_type = "Foul"
            elif(hit_angle_vertical <= -80 or hit_angle_vertical >= 80):
                hit_type ="Out"
            elif(hit_power >= 95 and hit_angle_horizontal > 45 and hit_angle_horizontal < 120 and hit_angle_vertical >= 17 and hit_angle_vertical <= 44):
                hit_type = "Homerun"
            elif((hit_angle_horizontal >= 45 and hit_angle_horizontal <= 50) or (hit_angle_horizontal <= 120 and hit_angle_horizontal >= 115)):
                if(hit_power >= 80):
                    coin_flip = random.randint(0, 1)
                    if(coin_flip == 0):
                        hit_type = "Out"
                    else:
                        coin_flip = random.randint(0, 1)
                        if(coin_flip == 0):
                            hit_type = "Single"
                        else:
                            hit_type = "Double"
                elif(hit_power < 80 and hit_power >= 75 ):
                    coin_flip = random.randint(0, 2)
                    if(coin_flip == 0):
                        hit_type = "Triple"
                    elif(coin_flip == 1):
                        hit_type = "Double"
                    else:
                        hit_type = "Single"
                else:
                    coin_flip = random.randint(0, 1)
                    if(coin_flip == 0):
                        hit_type = "Single"
                    else:
                        hit_type = "Out"
            elif(hit_power <= 75):
                coin_flip = random.randint(0, 1)
                if(coin_flip == 0):
                    hit_type = "Single"
                else:
                    hit_type = "Out"
            else:
                coin_flip = random.randint(0, 3)
                if(coin_flip == 0):
                    hit_type = "Single"
                elif(coin_flip == 1):
                    hit_type = "Double"
                else:
                    hit_type = "Out"
            
            if(hit_type == "Single"):
                if(man_on_third == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
                if(man_on_second == 1):
                    man_on_second = 0
                    man_on_third = 1
                if(man_on_first == 1):
                    man_on_first = 0
                    man_on_second = 1

                man_on_first = 1

            elif(hit_type == "Double"):
                if(man_on_third == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
                if(man_on_second == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
                if(man_on_first == 1):
                    man_on_first = 0
                    man_on_third = 1
                    
                man_on_second = 1

            elif(hit_type == "Triple"):
                if(man_on_third == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
                if(man_on_second == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
                if(man_on_first == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1

                man_on_third = 1

            elif(hit_type == "Homerun"):
                if(inning % 1 == 0):
                    away_score += 1
                else:
                    home_score += 1
                if(man_on_first == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
                if(man_on_second == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
                if(man_on_third == 1):
                    if(inning % 1 == 0):
                        away_score += 1
                    else:
                        home_score += 1
            elif(hit_type == "Foul"):
                if(strikes != 2):
                    strikes += 1                    
            else:
                strikes = 0
                balls = 0
                outs += 1

        if(balls == 4):
            strikes = 0
            balls = 0
            if(man_on_first == 1):
                if(man_on_second == 1):
                    if(man_on_third == 1):
                        if(inning % 1 == 0):
                            away_score += 1
                        else:
                            home_score += 1
                    else:
                        man_on_third = 1
                else:
                    man_on_second = 1
            else:
                man_on_first = 1
        if(strikes == 3):
            outs += 1
            strikes = 0
            balls = 0
            man_on_first = 0
            man_on_second = 0
            man_on_third = 0
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
            man_on_first = 0
            man_on_second = 0
            man_on_third = 0

    clear()
    print("FINAL SCORE:")
    print("{} - {}".format(home_team[0][0], home_score))
    print("{} - {}".format(away_team[0][0], away_score))
    return

def scrimmage():
    print("")
    print("Generating Leagues...")
    time.sleep(1)
    leagues = league_generator()
    home_team = leagues[0][1][0]
    away_team = leagues[0][1][1]
    clear() #Clears past print in cmd prompt
    print("League Generation Finished!")
    print("Starting Game - {} at {}".format(away_team[0][0], home_team[0][0]))
    print("")
    time.sleep(3)
    generate_game(home_team, away_team)
    return

valid_selection = False
while(valid_selection == False):
    print("Ryan's Insane Baseball Simulator - RIBS")
    print("(1) Scrimmage Mode")
    print("(2) More Coming Soon!")
    print("")
    inp = int(input("Enter a Choice: "))

    if(inp == 1):
        valid_selection = True
        clear() #Clears past print in cmd prompt
        scrimmage()
    else:
        print("")
        print("  !!! IVALID NUMBER !!!")
        print("Please Enter a Valid Number")
        print("")
        time.sleep(2)
        clear() #Clears past print in cmd prompt
