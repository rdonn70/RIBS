import random

def generate_name():                                                            #generates a person's name
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

def birthday_generator(age, current_year):
    month = random.randint(1, 12)
    if(month == 2):
        day = random.randint(1, 28)                                             #just assumes that the person will have their birthday on the 28th if they are born in a leap year
    elif(month == 4 or month == 6 or month == 9 or month == 11):                #April, June, September and November have 30 days
        day = random.randint(1, 30)
    else:                                                                       #the rest have 31
        day = random.randint(1, 31)
    year = current_year - age                                                   #birth year
    return (month, day, year)                                                   #mm/dd/yyyy           

def person_generator(current_year):                                                         #generates a player
    name = generate_name()                                                      #call generate name function which chooses a first and last name
    age = int(abs(random.normalvariate(28.20787, 3.564317)))                    #gets a random age from a normal distribution of ages in the MLB
    birthday = birthday_generator(age, current_year)
    general_position = random.choices(["IF", "OF", "C", "P", "DH"], weights=[20.95722, 16.31617, 7.976795, 54.02466, 0.725163])[0]
    
    if(general_position == "IF"):                                   #select from infield positions
        primary_position = random.choices(["1B", "2B", "3B", "SS"], weights=[21.79931, 36.33218, 20.0692, 21.79931])[0]
        secondary_list = ["1B", "2B", "3B", "SS", "None"]                       #just define the secondary positions list
        secondary_list.remove(primary_position)                                 #removes the primary position so that the primary and secondary positions are different
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["LF", "CF", "RF", "C", "DH"])   #adds some variety to the secondary position ~5% chance
        else:
            secondary_position = random.choice(secondary_list)                  #chooses another IF position as the secondary position
    elif(general_position == "OF"):                                             #select from outfield positions
        primary_position = random.choice(["LF", "CF", "RF"])                    #choose an outfield position
        secondary_list = ["LF", "CF", "RF", "None"]                             #define secondary outfield list
        secondary_list.remove(primary_position)                                 #remove the primary position from the secondary position list
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["1B", "2B", "3B", "SS", "DH"])  #5% chance to choose an infield position as secondary position
        else:
            secondary_position = random.choice(secondary_list)                  #choose from the secondary outfield list
    elif(general_position == "C"):
        primary_position = "C"                                                  #only one choice for catcher position - catcher
        if(random.randint(1, 100) <= 5):
            secondary_position = random.choice(["1B", "LF", "CF", "RF", "DH"])  #a little unlikely to be playing other positions
        else:
            secondary_position = random.choice(["None", "DH"])                  #usually will only be a catcher or DH
    elif(general_position == "P"):
        primary_position = random.choice(["SP", "RP", "CP"])                    #choose between starting, relief, or closing
        secondary_list = ["SP", "RP", "CP", "None"]                             #secondary pitcher list definition
        secondary_list.remove(primary_position)                                 #remove pitcher
        secondary_position = random.choice(secondary_list)
    elif(general_position == "DH"):                                             #designated hitter is the primary position and only position
        primary_position = "DH"
        secondary_position = "None"
    else:                                                                       #randomly choose a primary position just in case something screws up
        primary_position = random.choice(["1B", "2B", "3B", "SS", "LF", "CF", "RF", "C", "SP", "RP", "CP"])
        secondary_position = "None"
    
    stats = ["power", "contact", "speed", "throw_accuracy", "throw_speed", "fielding"]
    personality_traits = ['hard-working', 'active', 'trusting', 'self-conscious']
    
    for trait in range(len(personality_traits)):                                #randomly assign a 0 or 1 to each personality trait
        personality_traits[trait] = random.randint(0, 1)
    for stat in range(len(stats)):
        stats[stat] = random.randint(39, 79)                                    #randomly generate each stat as a number from 39-89
        if(personality_traits[0] == 1):                                         #if the player has the hard-working trait, do a 2-5 increase to all stats
            stats[stat] += random.randint(2, 5)
        if(personality_traits[1] == 1):                                         #if the player has the active trait, do a 2-5 increase to all stats
            stats[stat] += random.randint(2, 5)
        else:                                                                   #otherwise, do a 2-5 decrease of all stats
            stats[stat] -= random.randint(2, 5)
    
    if(personality_traits[2] == 1):                                             #if the player is trusting...
        stats[3] -= random.randint(1, 4)                                            #decrease throw accuracy by 1-4
        stats[4] += random.randint(1, 4)                                            #increase throw speed by 1-4
        if(primary_position in ["SS", "2B", "LF", "CF", "RF", "SP", "RP", "CP"]):
            stats[5] -= random.randint(1, 4)                                        #decrease fielding by 1-4 if the primary position is one which requires a lot of "trust"
    else:                                                                       #player is untrusting...
        stats[3] += random.randint(1, 2)                                            #increase throw accuracy by 1-2
        stats[4] -= random.randint(1, 2)                                            #decrease throw speed by 1-2
    if(personality_traits[3] == 1):                                             #if the player is self-conscious...
        stats[0] -= random.randint(2, 5)                                            #decrease power by 2-5
        stats[1] -= random.randint(2, 5)                                            #decrease contact by 2-5
        stats[5] -= random.randint(2, 5)                                            #decrease fielding by 2-5
    if(primary_position == "DH"):                                               #if the player is primarily a designated hitter...
        stats[0] += random.randint(5, 8)                                            #increase power by 5-8
        stats[1] += random.randint(5, 8)                                            #increase contact by 5-8
        stats[3] -= random.randint(5, 10)                                           #decrease throw accuracy by 5-10
        stats[4] -= random.randint(5, 10)                                           #decrease throw speed by 5-10
        stats[5] -= random.randint(5, 10)                                           #decrease fielding by 5-10
    if(secondary_position == "DH"):                                             #if the player is a designated hitter as their secondary position...
        stats[0] += random.randint(2, 4)                                            #increase power by 2-4
        stats[1] += random.randint(2, 4)                                            #increase contact by 2-4
    if(primary_position in ["SP", "RP", "CP"]):                                 #if the player is primarily a pitcher...
        stats[0] -= random.randint(30, 50)                                          #pitchers are bad at batting
        stats[1] -= random.randint(30, 50)
        stats[3] += random.randint(5, 10)                                           #increase throw_accuracy by 5-10
        stats[4] += random.randint(10, 20)                                          #increase throw_speed by 10-20

    for z in range(len(stats)):                                                 #get each stat once again
        if(stats[z] >= 99):                                                     #if the stat is greater than or equal to 99
            if(random.randint(0, 5) == 0):                                      #randomly determine if the stat should truly be 99
                stats[z] = 99                                                   #set the stat to 99
            else:
                stats[z] = 99 - random.randint(3, 7)                            #decrease the stat from 99 by 3-7
        if(stats[z] <= 0):                                                      #if the stat is less than or equal to zero
            if(random.randint(0, 5) == 0):                                      #randomly determine if the stat should truly be 0
                stats[z] = 1                                                    #set the stat to 1
            else:
                stats[z] = 0 + random.randint(2, 7)                             #increase the stat from 0 by 2-7

    combined_stats = 0
    for n in stats:
        combined_stats += n                                                     #sum up all the stats and store it as combined_stats
    
    pitches = ["Four-seam fastball", "Two-seam fastball", "Cut-fastball", "Split-finger fastball", "Change-up", "Curveball", "Slider", "Knuckleball", "Forkball"]
    
    if(primary_position == "SP"): 
        kv = random.randint(3, 4)                                               #total number of pitch types for a starting pitcher
        pitch_types = []                                                        #pitch list
        while(len(pitch_types) < kv):                                           #while loop for total amount of pitchers in a pitcher's arsenal 
            pitch = random.choices(pitches, k=1, weights=[50, 7.5, 7.5, 4, 7.5, 7.5, 7.5, 1, 7.5]) #randomly choose pitch type based on "stats"
            if(pitch not in pitch_types):                                       #choose pitch types that are not already in the pitch_type list
                pitch_types.append(pitch)                                       #adds the pitch type to the list
    elif(primary_position == "RP" or primary_position == "CP"): 
        kv = random.randint(2, 3)                                               #total number of pitch types for a relief/closing pitcher
        pitch_types = []                                                        #pitch list 
        while(len(pitch_types) < kv):                                           #same while loop as the starting pitcher
            pitch = random.choices(pitches, k=1, weights=[50, 7.5, 7.5, 4, 7.5, 7.5, 7.5, 1, 7.5])
            if(pitch not in pitch_types):
                pitch_types.append(pitch)
    else:                                                                       #code for the average player, in case they get subbed into a game as a pitcher
        randomness = random.randint(1, 100)
        pitch_types = ["Four-seam fastball"]                                    #always assign them the fastball pitch
        if(randomness == 100):                                                  #~1% chance for the non-pitcher to have a second, completely random pitch type
            pitch_types.append(random.choice(pitches))
    
    return [name, birthday, primary_position, secondary_position, combined_stats, stats, personality_traits, pitch_types]