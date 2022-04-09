import random
import time
from os import system, name
from math import sin, cos, radians

current_year = 2022

def clear():
    if name == 'nt': # for windows
        _ = system('cls')
    else: # for mac and linux
        _ = system('clear')

def quadratic_equation(a, b, c):
    t1 = ((-b) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    t2 = ((-b) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    if(t2 > t1):
        t = t2
    else:
        t = t1
    return t

def generate_name(): #generates a person's name
    first_names = ["James", "Robert", "John", "Michael", "William", "David", "Richard", "Thomas", "Charles", "Christopher", "Daniel",
                   "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian", "George",
                   "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen",
                   "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Gregory", "Frank", "Alexander", "Raymond", "Patrick",
                   "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Adam", "Henry", "Nathan", "Douglas", "Zachary", "Peter", "Kyle",
                   "Walter", "Ethan", "Jeremy", "Harold", "Keith", "Bo", "Christian", "Roger", "Noah", "Gerald", "Carl", "Terry", "Sean", 
                   "Austin", "Arthur", "Lawrence", "Jesse", "Dylan", "Bryan", "Joe", "Jordan", "Billy", "Bruce", "Albert", "Willie", 
                   "Gabriel", "Logan", "Alan", "Juan", "Wayne", "Roy", "Ralph", "Randy", "Eugene", "Vincent", "Russell", "Elijah", 
                   "Louis", "Bobby", "Philip", "Johnny", "Arman", "Gino", "Ed"]
    last_names = ["Blackmond", "Brinlee", "Everly", "Mclean", "Rozmus", "Fabian", "Ricklefs", "Lisiecki", "Gowen", "Lainhart", "Tague",
                  "Boldwyn", "Gowen", "Guterriez", "Averill", "Brage", "Herrold", "Silvaggio", "Pomberg", "Linard", "Baymon", "Cipolone",
                  "Martinez", "Viney", "Sampaga", "Smith", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez",
                  "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King", "Wright",
                  "Scott", "Torres", "Hill", "Flores", "Green", "Adams", "Nelson", "Nguyen", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
                  "Carter", "Roberts", "Johnson"]
    name = random.choice(first_names) + ' ' + random.choice(last_names)
    return name

def birthday_generator(age):
    month = random.randint(1, 12)
    if(month == 2):
        day = random.randint(1, 28) # just assumes that the person will have their birthday on the 28th if they are born in a leap year
    elif(month == 4 or month == 6 or month == 9 or month == 11): #April, June, September and November have 30 days
        day = random.randint(1, 30)
    else: #the rest have 31
        day = random.randint(1, 31)
    year = current_year - age #birth year
    return (month, day, year) #mm/dd/yyyy           

def person_generator(): #generates a player
    name = generate_name() #call generate name function which chooses a first and last name
    age = int(abs(random.normalvariate(28.20787, 3.564317))) #gets a random age from a normal distribution of ages in the MLB
    birthday = birthday_generator(age)
    general_position = random.choices(["IF", "OF", "C", "P", "DH"], weights=[20.95722, 16.31617, 7.976795, 54.02466, 0.725163])[0]
    
    if(general_position == "IF"): #select from infield positions
        primary_position = random.choices(["1B", "2B", "3B", "SS"], weights=[21.79931, 36.33218, 20.0692, 21.79931])[0]
        secondary_list = ["1B", "2B", "3B", "SS", "None"] #just define the secondary positions list
        secondary_list.remove(primary_position) #removes the primary position so that the primary and secondary positions are different
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["LF", "CF", "RF", "C", "DH"]) #adds some variety to the secondary position ~5% chance
        else:
            secondary_position = random.choice(secondary_list) #chooses another IF position as the secondary position
    elif(general_position == "OF"): #select from outfield positions
        primary_position = random.choice(["LF", "CF", "RF"]) #choose an outfield position
        secondary_list = ["LF", "CF", "RF", "None"] #define secondary outfield list
        secondary_list.remove(primary_position) #remove the primary position from the secondary position list
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["1B", "2B", "3B", "SS", "DH"]) #5% chance to choose an infield position as secondary position
        else:
            secondary_position = random.choice(secondary_list) #choose from the secondary outfield list
    elif(general_position == "C"):
        primary_position = "C" #only one choice for catcher position - catcher
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["1B", "LF", "CF", "RF", "DH"]) #a little unlikely to be playing other positions
        else:
            secondary_position = random.choice(["None", "DH"]) #usually will only be a catcher or DH
    elif(general_position == "P"):
        primary_position = random.choice(["SP", "RP", "CP"]) #choose between starting, relief, or closing
        secondary_list = ["SP", "RP", "CP", "None"] #secondary pitcher list definition
        secondary_list.remove(primary_position) #remove pitcher
        secondary_position = random.choice(secondary_list)
    elif(general_position == "DH"): #designated hitter is the primary position and only position
        primary_position = "DH"
        secondary_position = "None"
    else: #randomly choose a primary position just in case something screws up
        primary_position = random.choice(["1B", "2B", "3B", "SS", "LF", "CF", "RF", "C", "SP", "RP", "CP"])
        secondary_position = "None"
    
    stats = ["power", "contact", "speed", "throw_accuracy", "throw_speed", "fielding"]
    personality_traits = ['hard-working', 'active', 'trusting', 'self-conscious']
    
    for trait in range(len(personality_traits)): #randomly assign a 0 or 1 to each personality trait
        personality_traits[trait] = random.randint(0, 1)
    for stat in range(len(stats)):
        stats[stat] = random.randint(39, 79) #randomly generate each stat as a number from 39-89
        if(personality_traits[0] == 1): #if the player has the hard-working trait, do a 2-5 increase to all stats
            stats[stat] += random.randint(2, 5)
        if(personality_traits[1] == 1): #if the player has the active trait, do a 2-5 increase to all stats
            stats[stat] += random.randint(2, 5)
        else: #otherwise, do a 2-5 decrease of all stats
            stats[stat] -= random.randint(2, 5)
    
    if(personality_traits[2] == 1): #if the player is trusting...
        stats[3] -= random.randint(1, 4) #decrease throw accuracy by 1-4
        stats[4] += random.randint(1, 4) #increase throw speed by 1-4
        if(primary_position in ["SS", "2B", "LF", "CF", "RF", "SP", "RP", "CP"]):
            stats[5] -= random.randint(1, 4) #decrease fielding by 1-4 if the primary position is one which requires a lot of "trust"
    else: #player is untrusting...
        stats[3] += random.randint(1, 2) #increase throw accuracy by 1-2
        stats[4] -= random.randint(1, 2) #decrease throw speed by 1-2
    if(personality_traits[3] == 1): #if the player is self-conscious...
        stats[0] -= random.randint(2, 5) #decrease power by 2-5
        stats[1] -= random.randint(2, 5) #decrease contact by 2-5
        stats[5] -= random.randint(2, 5) #decrease fielding by 2-5
    if(primary_position == "DH"): #if the player is primarily a designated hitter...
        stats[0] += random.randint(5, 8) #increase power by 5-8
        stats[1] += random.randint(5, 8) #increase contact by 5-8
        stats[3] -= random.randint(5, 10) #decrease throw accuracy by 5-10
        stats[4] -= random.randint(5, 10) #decrease throw speed by 5-10
        stats[5] -= random.randint(5, 10) #decrease fielding by 5-10
    if(secondary_position == "DH"): #if the player is a designated hitter as their secondary position...
        stats[0] += random.randint(2, 4) #increase power by 2-4
        stats[1] += random.randint(2, 4) #increase contact by 2-4
    if(primary_position in ["SP", "RP", "CP"]): #if the player is primarily a pitcher
        stats[0] -= random.randint(30, 50) #there is no good pitcher who can bat for power
        stats[1] -= random.randint(30, 50) #there is no good pitcher who can bat for contact
        stats[3] += random.randint(5, 10) #increase throw_accuracy by 5-10
        stats[4] += random.randint(10, 20) #increase throw_speed by 10-20

    for z in range(len(stats)): #get each stat once again
        if(stats[z] >= 99): #if the stat is greater than or equal to 99
            if(random.randint(0, 5) == 0): #randomly determine if the stat should truly be 99
                stats[z] = 99 #set the stat to 99
            else:
                stats[z] = 99 - random.randint(3, 7) #decrease the stat from 99 by 3-7
        if(stats[z] <= 0): #if the stat is less than or equal to zero
            if(random.randint(0, 5) == 0): #randomly determine if the stat should truly be 0
                stats[z] = 1 #set the stat to 1
            else:
                stats[z] = 0 + random.randint(2, 7) #increase the stat from 0 by 2-7

    combined_stats = 0
    for n in stats:
        combined_stats += n #sum up all the stats and store it as combined_stats
    
    pitches = ["Four-seam fastball", "Two-seam fastball", "Cut-fastball", "Split-finger fastball", "Change-up", "Curveball", "Slider", "Knuckleball", "Forkball"]
    
    if(primary_position == "SP"): 
        kv = random.randint(3, 4) #total number of pitch types for a starting pitcher
        pitch_types = [] #pitch list
        while(len(pitch_types) < kv): #while loop for total amount of pitchers in a pitcher's arsenal 
            pitch = random.choices(pitches, k=1, weights=[50, 7.5, 7.5, 4, 7.5, 7.5, 7.5, 1, 7.5]) #randomly choose pitch type based on "stats"
            if(pitch not in pitch_types): #choose pitch types that are not already in the pitch_type list
                pitch_types.append(pitch) #adds the pitch type to the list
    elif(primary_position == "RP" or primary_position == "CP"): 
        kv = random.randint(2, 3) #total number of pitch types for a relief/closing pitcher
        pitch_types = [] #pitch list 
        while(len(pitch_types) < kv): #same while loop as the starting pitcher
            pitch = random.choices(pitches, k=1, weights=[50, 7.5, 7.5, 4, 7.5, 7.5, 7.5, 1, 7.5])
            if(pitch not in pitch_types):
                pitch_types.append(pitch)
    else: #code for the average player, in case they get subbed into a game as a pitcher
        randomness = random.randint(1, 100)
        pitch_types = ["Four-seam fastball"] #always assign them the fastball pitch
        if(randomness == 100): #~1% chance for the non-pitcher to have a second, completely random pitch type
            pitch_types.append(random.choice(pitches))
    
    return [name, birthday, primary_position, secondary_position, combined_stats, stats, personality_traits, pitch_types]

def team_generator(city, team_name):
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
        player = person_generator() #name, birthday, primary_position, secondary_position, combined_stats, stats, personality_traits, pitch_types
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
    conference_names = [("American League", "National League"), ("Central League", "Pacific League")] #im really uncreative
    conferences = random.choice(conference_names) #chooses one of the random tuples in the list of conferences

    conference1 = conferences[0] #label conference 1 as the first conference name in the tuple
    conference1_team_counts = 15 #define the amount of teams in the conference
    conference1_team_list = []
    while(conference1_team_counts > 0): #while not all the teams are filled in a conference
        team_name_choice = random.choice(team_names) #choose a random team name from the list of team names
        team_names.remove(team_name_choice) #remove the name from the list of team names so no 2 teams can have the same name
        city_choice = random.choice(cities) #choose a random city from the list of cities
        cities.remove(city_choice) #remove the city from the list of cities (while not realistic, i dont want 5 teams in NY, and im too lazy to figure out a better way right now)
        conference1_team_list.append(team_generator(city_choice, team_name_choice)) #generate a team
        conference1_team_counts -= 1 #remove the team count after one is successfully generated and added to the list

    conference2 = conferences[1] #same code as above but for the other conference
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

def hit_location(hit_power, hit_angle_horizontal, hit_angle_vertical):
    hit_type = position = 0 #define initial type of hit (foul, homerun) and white position the ball is hit to
    g = 9.81 #gravity constant
    h = 0.64 #estimate about 0.3 m off the ground where the ball is hit (not that good of a simulation)
    v0 = (36.8925 + random.uniform(0, 1)) * (hit_power / 99) #determine exit velocity of baseball
    v0x = v0 * cos(radians(hit_angle_vertical)) #x component of initial velocity
    v0y = v0 * sin(radians(hit_angle_vertical)) #y component of initial velocity
    t = quadratic_equation((-0.5 * g), v0y, h) #total time in air
    hit_distance = v0x * t #hit distance
    wind_addition = random.uniform(0, 4.4704) * random.randint(-1, 1) * t #converts wind speed to displacement (negative or positive)
    hit_distance += wind_addition #adds the wind direction to hit distance
    hit_distance_feet = hit_distance * 3.281 #conversion from meters to feet

    if(hit_angle_vertical < 0 and hit_angle_vertical >= -30):
        hit_distance_feet += random.randint(20, 70) #see if a groundball will escape to a position
    elif(hit_angle_vertical < -30 and hit_angle_vertical >= -55):
        hit_distance_feet += random.randint(40, 80) #see if a groundball will escape to a position

    if(hit_angle_horizontal < -15 and hit_angle_horizontal >= -45):
        wall_distance = ((67 / 30) * hit_angle_horizontal) + (837 / 2) #line equation of the outfield wall from -45 to -15 degrees
    elif(hit_angle_horizontal >= -15 and hit_angle_horizontal < 0):
        wall_distance = ((23 / 15) * hit_angle_horizontal) + 408 #line equation of the outfield wall from -15 to 0 degrees
    elif(hit_angle_horizontal <= 15 and hit_angle_horizontal >= 0):
        wall_distance = ((-23 / 15) * hit_angle_horizontal) + 408 #line equation of the outfield wall from 0 to 15 degrees
    elif(hit_angle_horizontal > 15 and hit_angle_horizontal <= 45):
        wall_distance = ((-67 / 30) * hit_angle_horizontal) + (837 / 2) #line equation of the outfield wall from 15 to 45 degrees
    else:
        hit_type = "Foul" #if the ball is hit at any other angle besides -45 and 45 degrees
        wall_distance = 0 #just define the wall distance as 0

    if(wall_distance == 0 and hit_distance >= 318): #goes past fence in the foul zone
        return (hit_type, 0)
    elif(wall_distance == 0 and hit_angle_horizontal < -45 and hit_angle_horizontal >= -50 and hit_distance_feet < 318 and hit_distance_feet >= 158):
        return (hit_type, "LF") #returns LF if it is catchable by the left fielder
    elif(wall_distance == 0 and hit_angle_horizontal > 45 and hit_angle_horizontal <= 50 and hit_distance_feet < 318 and hit_distance_feet >= 158):
        return (hit_type, "RF") #returns RF if it is catchable by the right fielder
    elif(wall_distance == 0 and hit_angle_horizontal >= 45):
        return (hit_type, 0) #goes inside crowd
    elif(wall_distance == 0 and hit_angle_horizontal <= -45):
        return (hit_type, 0) #goes inside crowd
    else:
        time_to_reach_wall = (wall_distance / 3.281) / v0x
        distance_at_wall = (v0y * time_to_reach_wall) + ((-0.5 * g) * (time_to_reach_wall ** 2)) + h #distance above the wall when it reaches the wall

        if(distance_at_wall >= 2.57): #checks to see if it goes over the wall
            hit_type = "Homerun"
        else:
            if(hit_distance_feet >= 158): #sees if the ball goes into the outfield and which position it is hit to
                if(hit_angle_horizontal >= -45 and hit_angle_horizontal < -22.5):
                    position = "LF"
                elif(hit_angle_horizontal >= -22.5 and hit_angle_horizontal <= 22.5):
                    position = "CF"
                elif(hit_angle_horizontal > 22.5 and hit_angle_horizontal <= 45):
                    position = "RF"
            elif(hit_distance_feet < 158 and hit_distance_feet >= 80): #sees if the ball stays in the infield and what position it is hit to
                if(hit_angle_horizontal >= -45 and hit_angle_horizontal < -22.5):
                    position = "3B"
                elif(hit_angle_horizontal >= -22.5 and hit_angle_horizontal < -5):
                    position = "SS"
                elif(hit_angle_horizontal >= -5 and hit_angle_horizontal <= 22.5):
                    position = "2B"
                elif(hit_angle_horizontal > 22.5 and hit_angle_horizontal <= 45):
                    position = "1B"
            elif(hit_distance_feet < 80 and hit_distance_feet >= 45): #if it is hit between 45 and 80 feet, it goes to the pitcher
                position = "Pitcher"
            elif(hit_distance_feet < 45): #if hit anywhere less than 45 feet, it is the catcher's job
                position = "C"

        return (hit_type, position, t)

def hitting(batter, pitcher, balls=0, strikes=0, pitches_thrown=0, inning=1):
    pitcher_accuracy = pitcher[5][3] - (pitches_thrown // 5) #every 5 pitches thrown, decreases throw accuracy by 1
    pitcher_throw_speed = pitcher[5][4] - (pitches_thrown // 5) #every 5 pitches thrown, decrease throw accuracy by 1
    pitcher_available_pitches = pitcher[7]  #retrieves the available pitches of the pitcher
    
    batter_power = batter[5][0] - (inning // 3) #decreases batter_power by 1 every 3 innings
    batter_contact = batter[5][1] - (inning // 3) #decreases batter_contact by 1 every 3 innings
    thrown_pitch = random.choice(pitcher_available_pitches) #randomly chooses a pitch from the pitcher's available pitches
    #normal distribution of speed, and randomish accuracy each pitch
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
        # knuckleball speed normal distribution is made up because there is no data on it
        pitch_accuracy = random.randint(50, 75) + (70.30231 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))
    else:
        pitch_speed = random.normalvariate(80.45333, 3.024301) + (random.randint(-1, 1) * (pitcher_throw_speed / 75))
        # this is also made up
        pitch_accuracy = random.randint(55, 75) + (80.45333 - pitch_speed) + (random.randint(-1, 1) * (pitcher_accuracy / 50))

    if(balls == 3): #makes the pitcher want to throw a strike so they dont walk him
        pitch_intention = 1 # 0 = outside, 1 = inside
    elif(strikes == 0 and balls == 0):
        if(random.randint(1, 100) > 40): #more likely to throw the ball inside on the first pitch
            pitch_intention = 1
        else:
            pitch_intention = 0
    else:
        pitch_intention = random.randint(0, 1) #if no special circumstance, the intention is random

    if(pitch_intention == 1): #checks to see if the intended pitch will actually go where it is supposed to
        if(random.randint(1, 100) > pitch_accuracy):
            in_strike_zone = 0 #not in the strike zone
        else:
            in_strike_zone = 1
    else:
        if(random.randint(1, 100) > pitch_accuracy): #just flip it if it is meant to be thrown on the outside of the strike zone
            in_strike_zone = 1 #in strike zone
        else:
            in_strike_zone = 0
    
    #checks to see if batter swings
    if(in_strike_zone == 1):
        if(random.randint(1, 100) > 32): #~68% chance the batter swings when it is inside the strike zone 
            swing = 1
        else:
            swing = 0
    else:
        if(random.randint(1, 100) > 68): #~32% chance the batter swings when it is outside the strike zone
            swing = 1
        else:
            swing = 0
    
    hit = ["Nohit", 0] #(type of hit, position it is hit to)
    
    if(swing == 1 and in_strike_zone == 1):
        z_contact_percent = 84 #inside contact percent
        z_contact_modified = ((z_contact_percent - batter_contact) // 2) + z_contact_percent #modifies percent contact based on batter contact stat
        if(random.randint(1, 100) > (100 - z_contact_modified)):
            hit_power = batter_power + (random.randint(-1, 1) * (random.randint(1, 2))) #random hit power added to the batter's power
            if(hit_power < 0): #make sure the hit power doesnt go below 0
                hit_power = 0
            elif(hit_power > 99): #or above 99
                hit_power = 99
            hit_angle_horizontal = random.randint(-60, 60)
            hit_angle_vertical = random.randint(-90, 90)
            hit = hit_location(hit_power, hit_angle_horizontal, hit_angle_vertical)
        else:
            strikes +=1 #batter swings and misses
    elif(swing == 1 and in_strike_zone == 0):
        o_contact_percent = 62 #outside contact percent
        o_contact_modified = ((o_contact_percent - batter_contact) // 2) + o_contact_percent #modifies percent contact based on batter contact stat
        if(random.randint(1, 100) > (100 - o_contact_modified)):
            hit_power = batter_power - (random.randint(1, 2)) #random hit power subtracted from the batter's power
            if(hit_power < 0): #make sure the hit power doesnt go below 0
                hit_power = 0
            elif(hit_power > 99): #or above 99
                hit_power = 99
            hit_angle_horizontal = random.randint(-60, 60)
            hit_angle_vertical = random.randint(-90, 90)
            hit = hit_location(hit_power, hit_angle_horizontal, hit_angle_vertical) #calls hit location to see where it goes
        else:
            strikes += 1 #batter swings and misses
    elif(swing == 0 and in_strike_zone == 1):
        strikes +=1 #does not swing and it is inside the strike zone -> strike
    elif(swing == 0 and in_strike_zone == 0):
        balls += 1 #does not swing and it is outside the strike zone -> ball
    else:
        strikes += 1 #just add a strike if anything weird happens
    try: #too lazy to add extra lines for the time it's in the air, so here is a try-except statement
        time_in_air = hit[2]
    except:
        time_in_air = 0
    
    return (hit, balls, strikes, time_in_air)

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
        clear() #Clears past print in cmd prompt
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
    clear()
    print("FINAL SCORE:")
    print("{} - {}".format(home_team[0][0], home_score))
    print("{} - {}".format(away_team[0][0], away_score))
    return (home_score, away_score)

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

def season(): #WIP
    print("")
    print("Generating Leagues...")
    time.sleep(1)
    leagues = league_generator()
    print("League Generation Finished!")
    time.sleep(0.5)
    clear() #Clears past print in cmd prompt
    print("Creating Regular Season Schedule")
    return

valid_selection = False
df = random.randint(0, 9999)
while(valid_selection == False):
    if(df == 2006):
        screen_df = 1
        print("\u001b[31mSlaves to Armok: God of Blood\u001b[0m") # Shout out to Dwarf Fortress
        print("Chapter III: Baseball")
        print("")
    else:
        screen_df = 0
        print("\u001b[32mRyan's Insane Baseball Simulator\u001b[0m")
        print("")
    if(screen_df == 1):
        print("(1) Dwarf Fortress")
        print("(2) Adventurer")
    else:
        print("(1) Season Mode - NOT IMPLEMENTED")
        print("(2) Scrimmage Mode")
    inp = int(input("Enter a Choice: "))

    if(inp == 2):
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
