import random
from math import sin, cos, radians

def quadratic_equation(a, b, c):
    t1 = ((-b) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    t2 = ((-b) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    if(t2 > t1):
        t = t2
    else:
        t = t1
    return t

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