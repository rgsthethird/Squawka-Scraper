import requests, unicodedata, time, xlsxwriter

def setLeague(input,startDate):
    print "Getting league....\n"
    if input == "English":
        if startDate[-4:] == "2014":
            return '126'
        elif startDate[-4:] == "2015":
            return '165'
        elif startDate[-4:] == "2016": 
            return '641'
        elif startDate[-4:] == "2017":    
            return '819'
    elif input == "Italian":
        if startDate[-4:] == "2014":
            return '137'
        elif startDate[-4:] == "2015":
            return '177'
        elif startDate[-4:] == "2016": 
            return '717'
        elif startDate[-4:] == "2017":    
            return '869'
    elif input == "German":
        if startDate[-4:] == "2014":
            return '129'
        elif startDate[-4:] == "2015":
            return '169'
        elif startDate[-4:] == "2016": 
            return '682'
        elif startDate[-4:] == "2017":    
            return '846'
    elif input == "Spanish":
        if startDate[-4:] == "2014":
            return '136'
        elif startDate[-4:] == "2015":
            return '176'
        elif startDate[-4:] == "2016": 
            return '712'
        elif startDate[-4:] == "2017":    
            return '862'
    elif input == "French":
        if startDate[-4:] == "2014":
            return '118'
        elif startDate[-4:] == "2015":
            return '167'
        elif startDate[-4:] == "2016": 
            return '629'
        elif startDate[-4:] == "2017":    
            return '822'
    '''elif input == "Champions":
        return '727'
    elif input == "Europa":
        return '728'''

def go(startDate,endDate,league,txtName):
    print ""
    params = {
        'type': 'Player Stats',
        'filter': '2', #we will assume they are in passes info
        'league': setLeague(league,startDate),
        'team': setTeams(league,startDate), #setTeams(league,startDate),
        'played': 'All matches',
        'position': 'All Player Positions', #Goalkeeper',
        'agestart': '16',
        'ageend': '39',
        'noofmatch': '0',
        'seasonstart': startDate,
        'seasonend': endDate,
        'by': 'season',
        'timestart': '0',
        'timeend': '90',
        'showtype': 'total',
    }
    print "Getting data....\n"
    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        params=params,
    )
    data = response.json()
    with open("SampleData2.txt", "w") as text_file:
        text_file.write("%s" % data)
    playerList = ''
    first = True
    for x in data["result"]:
        if x != 'sort':
            item = data["result"][x]["info"]["name"]
            newItem = unicodedata.normalize('NFD', item).encode("ascii", "ignore")
            #print newItem
            playerNum = data["result"][x]["info"]["player_id"]
            #print playerNum
            oldClub = data["result"][x]["info"]["club"]
            club = unicodedata.normalize('NFD', oldClub).encode("ascii", "ignore")

            if(club == "Amiens"):
                club = 569
            elif(club == "Angers"):
                club = 517
            elif(club == "Bordeaux"):
                club = 53
            elif(club == "Caen"):
                club = 130
            elif(club == "Dijon"):
                club = 548
            elif(club == "Guingamp"):
                club = 144
            elif(club == "Lille"):
                club = 56   
            elif(club == "Lyon"):
                club = 58   
            elif(club == "Marseille"):
                club = 59    
            elif(club == "Metz"):
                club = 133   
            elif(club == "Monaco"):
                club = 134    
            elif(club == "Montpellier"):
                club = 60   
            elif(club == "Nantes"):
                club = 135   
            elif(club == "Nice"):
                club = 62  
            elif(club == "PSG"):
                club = 63   
            elif(club == "Rennes"):
                club = 65   
            elif(club == "St Etienne"):
                club = 67
            elif(club == "Strasbourg"):
                club = 136
            elif(club == "Toulouse"):
                club = 68
            elif(club == "Troyes"):
                club = 69   

            569,517,53,130,548,144,56,58,59,133,134,60,135,62,63,65,67,136,68,69
            #print club
# to print a list of players' names, parsed by commas            
            #if first:
            #  playerList+= str(newItem)
            #   first = False
            #else:
                #playerList+= ", "+str(newItem)
# to print a list of players in playerInformation's format in SquawkaFinal
            playerList+='"'+str(newItem)+'":{"player_id":"'+str(playerNum)+'","team_id":"'+str(club)+'","league_id":"'+setLeague(league,startDate)+'"},'
    with open(str(txtName)+".txt", "w") as text_file:
        text_file.write("%s" % playerList)
    print "\033[93mDone!\033[0m"
    print ""
''' print "Looking for [%s]" % player
    for x in data["result"]:
        if isinstance(data["result"][x], list):
            continue
        if player in unicodedata.normalize('NFD', data["result"][str(x)]["info"]["name"]).encode("ascii", "ignore"):
            return (unicodedata.normalize('NFD', data["result"][str(x)]["info"]["name"]).encode("ascii", "ignore"), x)'''

def setTeams(input,startDate):

    print "Getting team....\n"

    if input == "English":
        if startDate[-4:] == "2014":
            return '31,32,302,33,169,34,170,315,36,37,38,39,41,43,44,45,46,47,48,49'
        elif startDate[-4:] == "2015":
            return '31,32,299,33,169,34,315,36,37,38,39,40,43,44,45,46,47,323,48,49'
        elif startDate[-4:] == "2016":  
            return '31,299,302,33,169,34,170,315,36,37,38,317,43,44,45,46,47,323,48,49'
        elif startDate[-4:] == "2017":  
            return '31,299,301,302,33,169,34,309,315,36,37,38,39,43,44,46,47,323,48,49'

    elif input == "Italian":
        if startDate[-4:] == "2014":
            return '109,111,461,113,462,114,115,116,117,118,119,120,121,122,124,125,231,127,128,143'
        elif startDate[-4:] == "2015":
            return '109,110,527,113,462,114,528,115,116,117,118,119,120,121,124,125,231,127,128,143'
        elif startDate[-4:] == "2016":  
            return '109,110,111,113,554,462,114,115,116,117,118,119,120,121,123,124,125,231,127,128'
        elif startDate[-4:] == "2017":  
            return '109,572,110,111,113,554,114,115,116,117,118,119,120,124,125,231,573,127,128,143'
    
    elif input == "German":
        if startDate[-4:] == "2014":
            return '452,92,94,95,96,97,98,99,100,102,103,172,453,104,108,93,106,107'
        elif startDate[-4:] == "2015":
            return '452,92,94,95,96,97,98,99,520,100,102,103,172,521,108,93,106,107'
        elif startDate[-4:] == "2016":  
            return '452,92,94,95,96,97,98,99,520,100,102,172,551,104,521,108,93,107'
        elif startDate[-4:] == "2017":  
            return '452,92,94,95,96,97,98,99,100,102,103,172,551,104,108,93,106,107'    
    
    elif input == "Spanish":
        if startDate[-4:] == "2014":
            return '173,71,72,73,74,459,75,460,174,76,77,78,79,80,83,85,86,89,90,175'
        elif startDate[-4:] == "2015":
            return '71,72,73,74,75,460,76,77,78,525,79,80,83,84,85,86,89,526,90,175'
        elif startDate[-4:] == "2016":  
            return '549,71,72,73,74,75,460,76,78,525,550,80,82,84,85,86,89,526,90,175'
        elif startDate[-4:] == "2017":  
            return '549,71,72,73,74,75,460,76,77,571,525,550,79,80,84,85,86,89,90,175'    
    
    elif input == "French":
        if startDate[-4:] == "2014":
            return '52,53,130,55,144,132,56,57,58,59,133,134,60,135,62,63,64,65,67,68'
        elif startDate[-4:] == "2015":
            return '517,52,53,130,518,144,56,57,58,59,134,60,135,62,63,64,65,67,68,69'
        elif startDate[-4:] == "2016":  
            return '517,52,53,130,548,144,56,57,58,59,133,134,60,61,135,62,63,65,67,68'
        elif startDate[-4:] == "2017":  
            return '569,517,53,130,548,144,56,58,59,133,134,60,135,62,63,65,67,136,68,69'    

url = 'http://www.squawka.com/wp-content/themes/squawka_web/leaderboard_process-v2.php'
headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-us',
}

filters = [(2,'Performance Score'),(3,'Goals Scored'),(4,'Shot Accuracy'),(7,'Pass Accuracy'),(9,'Duels Won'),(10,'Defensive Actions'),(12,'Discipline')]
keeperFilters = [(2, 'Performance Score'),(19, 'Saves'),(20,'Goals Conceded'),(18,'Clean Sheets'),(22, 'Claims')]
excelHeaders = ["Player","League","Goal","RC","Assist","YC","Suffered","Committed","SOG","Blocked","Clear","Interception","KPass","Pass","Tackle","TakeOn","Save","Goal","Clean","Claim","Failed","Games","Minutes"]
txtName = raw_input(".txt file for output: ")
startDate = raw_input("Start date [dd/mm/yyyy]: ")
endDate = raw_input("End date [dd/mm/yyyy]: ")
league = raw_input("Which league? [\033[91mEnglish, Spanish, German, Italian, French\033[0m]\n")
go(startDate,endDate,league,txtName)
