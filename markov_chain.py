#from Markov_Chain_ex import activity_forecast
import numpy as np
import random as rd

states = ["Eat", "Sleep", "Game", "Chew Gum"]
transitionName = [["EE","ES","EG","EC"],["SS","SG","SC","SE"],["GG","GC","GE","GS"],["CC","CE","CS","CG"]]
transitionMatrix = [[0.2,0.1,0.4,0.3],[0.2,0.0,0.3,0.5],[0.3,0.4,0.3,0.0],[0.3,0.2,0.2,0.3]]

if (sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[2]) + sum(transitionMatrix[3])) != 4:
    print("Something went wrong")
else:
    print("done")

oneortwochoice = str(input('Do you want choose to pick a state to start on or randomize it? "Pick" or "Random" '))

if oneortwochoice == "Pick":

    print("What state do you want the method to start on? ")
    randomchosenstate = input('The options are "Chew Gum" "Game" "Eat" and "Sleep": ')

    if randomchosenstate == "Chew Gum":
        randomoutput = "Chew Gum"
    elif randomchosenstate == "Game":
        randomoutput = "Game"
    elif randomchosenstate == "Eat":
        randomoutput = "Eat"
    elif randomchosenstate == "Sleep":
        randomoutput = "Sleep"
    else:
        print("ERRROR HAVOC HAS BEEN DRAWN")

elif oneortwochoice == "Random":

    randomthing = rd.randint(1,4)
    
    if randomthing == 1:
        randomoutput = "Eat"
    elif randomthing == 2:
        randomoutput = "Sleep"
    elif randomthing == 3:
        randomoutput = "Game"
    elif randomthing == 4:
        randomoutput = "Chew Gum"
    else:
        print("ERRROR HAVOC HAS BEEN DRAWN")

else:
    print("ERRROR HAVOC HAS BEEN DRAWN")
    
    
    
numberofdays = int(input("how many days do you want the markov chain to run through? "))
numberofdays = numberofdays - 1 

def forecast(days):
    
    activityToday = randomoutput
    print("the start activity is " + activityToday)

    actodaylist = [activityToday]

    
    i = 0
    prob = 1

    while i != days:
        if activityToday == "Sleep":
            ranchoice = np.random.choice(transitionName[1], replace=True,p=transitionMatrix[1])

            if ranchoice == "SS":
                prob = prob * 0.2
                actodaylist.append("Sleep")
                
            elif ranchoice == "SG":
                prob = prob * 0.0
                actodaylist.append("Game")
            
            elif ranchoice == "SE":
                prob = prob * 0.5
                actodaylist.append("Eat")
            
            elif ranchoice == "SC":
                prob = prob * 0.3
                actodaylist.append("Chew Gum")
            #////////////////////////////////////////////////////////////////   
        elif activityToday == "Game":
            ranchoice = np.random.choice(transitionName[2], replace=True,p=transitionMatrix[2])

            if ranchoice == "GS":
                prob = prob * 0.0
                actodaylist.append("Sleep")
                
            elif ranchoice == "GG":
                prob = prob * 0.3
                actodaylist.append("Game")
            
            elif ranchoice == "GE":
                prob = prob * 0.3
                actodaylist.append("Eat")
            
            elif ranchoice == "GC":
                prob = prob * 0.4
                actodaylist.append("Chew Gum")
            #////////////////////////////////////////////////////////////////
        
        elif activityToday == "Chew Gum":
            ranchoice = np.random.choice(transitionName[3], replace=True,p=transitionMatrix[3])
            
            if ranchoice == "CS":
                prob = prob * 0.2
                actodaylist.append("Sleep")
                
            elif ranchoice == "CG":
                prob = prob * 0.3
                actodaylist.append("Game")
            
            elif ranchoice == "CE":
                prob = prob * 0.2
                actodaylist.append("Eat")
            
            elif ranchoice == "CC":
                prob = prob * 0.3
                actodaylist.append("Chew Gum")
            #////////////////////////////////////////////////////////////////

        elif activityToday == "Eat":
            ranchoice = np.random.choice(transitionName[0], replace=True,p=transitionMatrix[0])
            
            if ranchoice == "ES":
                prob = prob * 0.1
                actodaylist.append("Sleep")
                
            elif ranchoice == "EG":
                prob = prob * 0.4
                actodaylist.append("Game")
            
            elif ranchoice == "EE":
                prob = prob * 0.2
                actodaylist.append("Eat")
            
            elif ranchoice == "EC":
                prob = prob * 0.3
                actodaylist.append("Chew Gum")
            #////////////////////////////////////////////////////////////////
        i += 1

    
    print("Choices are: " + str(actodaylist))
    print("End state after " + str(days + 1) + " days: " + actodaylist[numberofdays])
    print("probability of the possible sequence of states: " + str(prob))


forecast(numberofdays)

