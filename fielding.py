#Completely overhauled fielding, still needs some calibration
import random

list_dict = {"P": 0, "C": 1, "1B": 2, "2B": 3, "3B": 4, "SS": 5, "LF": 6, "CF": 7, "RF": 8}

def throw(runner_stats, fielder_stats, receiver_stats, modifier=0):
    if(runner_stats[2] > (fielder_stats[4] - modifier) or random.randint(0, 98) > (fielder_stats[3] + receiver_stats[5]) / 2):
        return 0 #fail flag
    else:
        return 1

def error(fielding_score):
    if(random.randint(1, 100) > fielding_score):
        return 1
    else:
        return 0

#fielding output = [score_increase, men_on_bases, outs, message]
def fielding(defense_lineup, time_in_air, outs, men_on_bases, position, current_batter):
    if(position == "Pitcher"):
        position = "P"
    # men_on_bases = [man_on_first, man_on_second, man_on_third]
    # [P, C, 1, 2, 3, SS, LF, CF, RF]
    stats = [defense_lineup[0][5], defense_lineup[1][5], defense_lineup[2][5], defense_lineup[3][5], defense_lineup[4][5], defense_lineup[5][5], defense_lineup[6][5], defense_lineup[7][5], defense_lineup[8][5]]
    try:
        MOB_0 = men_on_bases[0][5]
    except:
        MOB_0 = [0, 0, 0, 0, 0]
    try:
        MOB_1 = men_on_bases[1][5]
    except:
        MOB_1 = [0, 0, 0, 0, 0]
    try:
        MOB_2 = men_on_bases[2][5]
    except:
        MOB_2 = [0, 0, 0, 0, 0]
    stats_dict = {"P": stats[0], "C": stats[1], "1B": stats[2], "2B": stats[3], "3B": stats[4], "SS": stats[5], "LF": stats[6], "CF": stats[7], "RF": stats[8], "1": MOB_0, "2": MOB_1, "3": MOB_2, "B": current_batter[5]}
    scores = [] #fielding scores list
    state = [len(men_on_bases[2]), len(men_on_bases[1]), len(men_on_bases[0])] #000, 001, 010, 011, 100, 101, 110, 111 (110 = bases load except first)
    for a in stats:
        scores.append((a[5] + ((time_in_air - 1.5) // 1.5)) * (99 / 100))

    if(error(scores[list_dict[position]]) == 1):
        if(state == [0, 0, 0]):
            return([0, [[current_batter], [], []], outs])
        elif(state == [0, 0, 1]):
            return([0, [[current_batter], [men_on_bases[0]], []], outs])
        elif(state == [0, 1, 0]):
            return([0, [[current_batter], [], [men_on_bases[1]]], outs])
        elif(state == [0, 1, 1]):
            return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], outs])
        elif(state == [1, 0, 0]):
            return([1, [[current_batter], [], []], outs])
        elif(state == [1, 0, 1]):
            return([1, [[current_batter], [men_on_bases[0]], []], outs])
        elif(state == [1, 1, 0]):
            return([1, [[current_batter], [], [men_on_bases[1]]], outs])
        else:
            return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], outs])
    elif(position in ["LF", "RF", "CF"] and time_in_air >= 2.5 and scores[list_dict[position]] >= random.randint(0, 99)): #outfielder catches flyball for out
        return([0, men_on_bases, (outs+1)])
    elif(outs == 2):
        if(position == "P"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([0, [[current_batter], [], []], outs])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([0, [[current_batter], [men_on_bases[0]], []], outs])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], outs])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], outs])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([1, [[current_batter], [], []], outs])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throw to first
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "C"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "1B"):
            return [0, [[], [], []], 3] #tag first
        elif(position == "2B"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "3B"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([0, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 1]):
                return([0, [[], [], []], 3]) #tag third
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([1, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                return([0, [[], [], []], 3]) #tag third
        elif(position == "SS"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"], 5) == 0): #throws to first
                    return([0, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"], 5) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"], 5) == 0): #throws to first
                    return([1, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"], 5) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "LF"):
            if(state == [0, 0, 0]):
                return([0, [[current_batter], [], []], 2]) #throw to cutoff, batter advances to first
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["LF"], stats_dict["2B"], 20) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                return([0, [[current_batter], [], [men_on_bases[1]]], 2]) #throw to cutoff, batter advances, second advances
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["2"], stats_dict["LF"], stats_dict["3B"], 15) == 0): #throws to third
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                return([1, [[current_batter], [], []], 2]) #throw to cutoff, batter advances, third scores
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["LF"], stats_dict["2B"], 20) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["2"], stats_dict["LF"], stats_dict["3B"], 15) == 0): #throws to third
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                if(throw(stats_dict["2"], stats_dict["LF"], stats_dict["3B"], 15) == 0): #throws to third
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "CF"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"], 20) == 0): #throws to first
                    return([0, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"], 15) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"], 20) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"], 15) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"], 20) == 0): #throws to first
                    return([1, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"], 15) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"], 20) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"], 15) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "RF"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([0, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([1, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([1, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            else:
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"], 15) == 0): #throws to first
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
    elif(outs == 1):
        if(position == "P"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["P"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"], 10) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], []], 1])
                    else:
                        return([0, [[], [men_on_bases[0]], []], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], []], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["2"], stats_dict["P"], stats_dict["3B"]) == 0): #throws to third
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [], []], 2])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["P"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                    else:
                        return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["3"], stats_dict["P"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 1])
                else:
                    return([0, [[current_batter], [], []], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["P"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [men_on_bases[0]], []], 1])
                    else:
                        return([1, [[], [men_on_bases[0]], []], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [], []], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["P"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["P"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                    else:
                        return([1, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                    else:
                        return([0, [[], [], []], 3])
        elif(position == "C"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
                else:
                    return([0, [[], [men_on_bases[0]], []], 2])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["2"], stats_dict["C"], stats_dict["3B"]) == 0): #throws to third
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "1B"):
            if(state == [0, 0, 0]):
                return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["1B"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                return([0, [[], [men_on_bases[0]], []], 2])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["1B"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 3])
            elif(state == [1, 0, 0]):
                return([0, [[], [], [men_on_bases[2]]], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["1B"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 2])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["1B"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[], [men_on_bases[0]], [men_on_bases[1]]], 3])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "2B"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], []], 1])
                else:
                    return([0, [[], [men_on_bases[1]], []], 2])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[2]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], [men_on_bases[2]]], 1])
                else:
                    return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 2])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "3B"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], []], 1])
                    else:
                        return([0, [[], [men_on_bases[0]], []], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], []], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
                else:
                    return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[2]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[2]]], 1])
                    else:
                        return([0, [[], [men_on_bases[0]], [men_on_bases[2]]], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], [men_on_bases[2]]], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"], 10) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], [men_on_bases[2]]], 1])
                else:
                    return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 2])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[1]], []], 2])
                else:
                    return([0, [[], [], []], 3])
        elif(position == "SS"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"], 5) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], []], 1])
                    else:
                        return([0, [[], [men_on_bases[0]], []], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], []], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"], 5) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                    else:
                        return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], [men_on_bases[1]]], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["3"], stats_dict["SS"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 1])
                else:
                    return([0, [[current_batter], [], []], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [men_on_bases[0]], []], 1])
                    else:
                        return([1, [[], [men_on_bases[0]], []], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [], []], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["SS"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"], (-10)) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                    else:
                        return([1, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [], [men_on_bases[1]]], 2])
                    else:
                        return([0, [[], [], []], 3])
        elif(position == "LF"):
            if(state == [0, 0, 0]):
                return([0, [[current_batter], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["LF"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
                else:
                    return([0, [[current_batter], [], []], 2])
            elif(state == [0, 1, 0]):
                return([0, [[current_batter], [men_on_bases[1]], []], 1])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["2"], stats_dict["LF"], stats_dict["3B"]) == 0): #throws to third
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["3"], stats_dict["LF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 1])
                else:
                    return([0, [[current_batter], [], []], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["3"], stats_dict["LF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], []], 1])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["LF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
            else:
                if(throw(stats_dict["3"], stats_dict["LF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
        elif(position == "CF"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
                else:
                    return([0, [[current_batter], [], []], 2])
            elif(state == [0, 1, 0]):
                return([0, [[current_batter], [men_on_bases[1]], []], 1])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], []], 1])
                else:
                    return([1, [[], [], []], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], []], 1])
                else:
                    return([1, [[current_batter], [], []], 2])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"]) == 0): #throws to first
                    return([1, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([1, [[], [], [men_on_bases[1]]], 2])
            else:
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([1, [[current_batter], [], [men_on_bases[1]]], 2])
        elif(position == "RF"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
                else:
                    return([0, [[], [men_on_bases[0]], []], 2])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 1])
                else:
                    return([0, [[current_batter], [], []], 2])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], []], 1])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 2])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
            else:
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 2])
    else:
        if(position == "P"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 0])
                else:
                    return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["P"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], []], 0])
                    else:
                        return([0, [[], [men_on_bases[0]], []], 1])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], []], 1])
                    else:
                        return([0, [[], [], []], 2])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], []], 0])
                else:
                    return([0, [[], [men_on_bases[1]], []], 1])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 1])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[2]]], 1])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["P"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 1])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["3"], stats_dict["P"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
        elif(position == "C"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 0])
                else:
                    return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[], [men_on_bases[0]], []], 1])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 0])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 1])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["2"], stats_dict["C"], stats_dict["3B"]) == 0): #throws to third
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 1])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[2]]], 1])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 1])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                if(throw(stats_dict["B"], stats_dict["C"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 2])
        elif(position == "1B"):
            if(state == [0, 0, 0]):
                return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["1B"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[], [men_on_bases[0]], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 1, 0]):
                return([0, [[], [], [men_on_bases[1]]], 1])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["1B"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [1, 0, 0]):
                return([0, [[], [], [men_on_bases[2]]], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["1B"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[], [men_on_bases[0]], [men_on_bases[2]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 2])
            elif(state == [1, 1, 0]):
                return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 1])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[2]]], 1])
        elif(position == "2B"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 0])
                else:
                    return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 1])
                else:
                    return([0, [[], [], []], 2])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], []], 0])
                else:
                    return([0, [[], [men_on_bases[1]], []], 1])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[2]]], 1])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 2])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 1])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["3"], stats_dict["2B"], stats_dict["C"]) == 0): #throws home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 1])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 2])
        elif(position == "3B"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 0])
                else:
                    return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], []], 0])
                    else:
                        return([0, [[], [men_on_bases[0]], []], 1])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], []], 1])
                    else:
                        return([0, [[], [], []], 2])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], []], 0])
                else:
                    return([0, [[], [men_on_bases[1]], []], 1])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], []], 1])
                    else:
                        return([0, [[], [men_on_bases[0]], []], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[], [], []], 2])
                    else:
                        return([0, [[], [], []], 3])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [], [men_on_bases[2]]], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[2]]], 0])
                    else:
                        return([0, [[], [men_on_bases[0]], [men_on_bases[2]]], 1])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], [men_on_bases[2]]], 1])
                    else:
                        return([0, [[], [], [men_on_bases[2]]], 2])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["3B"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], [men_on_bases[2]]], 0])
                else:
                    return([0, [[], [men_on_bases[1]], [men_on_bases[2]]], 1])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["3B"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [men_on_bases[0]], []], 1])
                    else:
                        return([1, [[], [men_on_bases[0]], []], 2])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([1, [[current_batter], [], []], 2])
                    else:
                        return([0, [[], [], []], 3])
        elif(position == "SS"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 0])
                else:
                    return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], []], 0])
                    else:
                        return([0, [[], [men_on_bases[0]], []], 1])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], []], 1])
                    else:
                        return([0, [[], [], []], 2])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["SS"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[1]], []], 0])
                else:
                    return([0, [[], [men_on_bases[1]], []], 1])
            elif(state == [0, 1, 1]):
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["SS"], stats_dict["2B"]) == 0): #throws to second
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                    else:
                        return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 1])
                else:
                    if(throw(stats_dict["B"], stats_dict["2B"], stats_dict["1B"]) == 0): #throws to first
                        return([0, [[current_batter], [], [men_on_bases[1]]], 1])
                    else:
                        return([0, [[], [], [men_on_bases[1]]], 2])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["3"], stats_dict["SS"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 0])
                else:
                    return([0, [[current_batter], [], []], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["SS"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["SS"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
            else:
                if(time_in_air >= 3):
                    return([0, men_on_bases, (outs+1)]) #infield fly rule
                elif(throw(stats_dict["1"], stats_dict["SS"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
        elif(position == "LF"):
            if(state == [0, 0, 0]):
                return([0, [[current_batter], [], []], 0])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["LF"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[current_batter], [], []], 1])
            elif(state == [0, 1, 0]):
                return([0, [[current_batter], [], [men_on_bases[1]]], 0])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["1"], stats_dict["LF"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["3"], stats_dict["LF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 0])
                else:
                    return([0, [[current_batter], [], []], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["LF"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["LF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
            else:
                if(throw(stats_dict["1"], stats_dict["LF"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])
        elif(position == "CF"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 0])
                else:
                    return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["2B"]) == 0): #throws to second
                    return([0, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[current_batter], [], []], 1])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["CF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 0])
                else:
                    return([0, [[current_batter], [], []], 1])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["1"], stats_dict["CF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
            elif(state == [1, 0, 0]):
                return([1, [[current_batter], [], []], 0]) #throw to cutoff
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["3"], stats_dict["CF"], stats_dict["2B"]) == 0): #throws to second
                    return([1, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([1, [[current_batter], [], []], 1])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["CF"], stats_dict["C"]) == 0): #throws to home
                    return([2, [[current_batter], [], []], 0])
                else:
                    return([1, [[current_batter], [men_on_bases[0]], []], 1])
            else:
                if(throw(stats_dict["3"], stats_dict["CF"], stats_dict["C"]) == 0): #throws to home
                    return([2, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([1, [[current_batter], [men_on_bases[0]], []], 1])
        elif(position == "RF"):
            if(state == [0, 0, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], []], 0])
                else:
                    return([0, [[], [], []], 1])
            elif(state == [0, 0, 1]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[], [men_on_bases[0]], []], 1])
            elif(state == [0, 1, 0]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [], [men_on_bases[1]]], 0])
                else:
                    return([0, [[], [], [men_on_bases[1]]], 1])
            elif(state == [0, 1, 1]):
                if(throw(stats_dict["B"], stats_dict["RF"], stats_dict["1B"]) == 0): #throws to first
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[], [men_on_bases[0]], [men_on_bases[1]]], 1])
            elif(state == [1, 0, 0]):
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], []], 0])
                else:
                    return([0, [[current_batter], [], []], 1])
            elif(state == [1, 0, 1]):
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], []], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], []], 1])
            elif(state == [1, 1, 0]):
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [], [men_on_bases[1]]], 1])
            else:
                if(throw(stats_dict["3"], stats_dict["RF"], stats_dict["C"]) == 0): #throws to home
                    return([1, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 0])
                else:
                    return([0, [[current_batter], [men_on_bases[0]], [men_on_bases[1]]], 1])