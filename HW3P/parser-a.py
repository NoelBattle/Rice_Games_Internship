
import csv
i=0
while i == 0:       #starts loop
    ask = raw_input("Do you wanna check out Team Members[1] or Enemies[2] Press q to exit")
    if ask == "q":  #breaks loop if q is entered
        break
    int_ask = int(ask)

    # Opens the CSV files
    with open('enemies.csv','r') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=",") #reads the csv file
        sortedlist = sorted(spamreader, key=lambda row: (row['attack']), reverse=False) #sorts rows in the members.csv by ascending attack
        reverselist= sorted(sortedlist, reverse=True) #sorts rows in the members.csv by descending attack

    with open('members.csv', 'r') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=",")
        memberlist = sorted(spamreader, key=lambda row: (row['Total']), reverse=False) #sorts rows in the members.csv by Total

    #Questions
    if int_ask == 1: #option 1
        ask2 = raw_input("Do you wanna check out team member list[a], output the members' profession[b], list total money[c], or list out transactions[d]")
        if ask2 == 'a':
            for row in memberlist: #iterates through the rows in the list
                print(row['name'])
        if ask2 == 'b':
            ask3 = raw_input("Which profession programming[i], art[ii], or music[iii]")
            if ask3 == 'i':
                for row in memberlist:
                    if row['role'] == 'Composer':
                        print(row['name'])
            if ask3 == 'ii':
                for row in memberlist:
                    if row['role'] == 'Artist':
                        print(row['name'])
            if ask3 == 'iii':
                for row in memberlist:
                    if row['role'] == 'Programmer':
                        print(row['name'])
        if ask2 == 'c':
            for row in memberlist:
                print(row['name'], row['Total'])

    if int_ask == 2: #option 2
        ask2 = raw_input("Do you wanna check out enemy list[a], enemy listed by stats[b], or enemy listed by type[c]")
        if ask2 == 'a':
            for row in sortedlist: #iterates through the rows in the list
                print(row['player_name'])
        if ask2 == 'b':
            ask3 = raw_input("Do you want the strengths in ascending(i) or descending(ii) order?")
            if ask3 == 'i':
                for row in sortedlist:
                    print(row['player_name'], row['eng_name'])
            if ask3 == 'ii':
                for row in reverselist:
                    print(row['player_name'], row['eng_name'])
        if ask2 == 'c':
            print("ZAKO")
            for row in sortedlist:
                int_hp = int(row['hp'])
                if int_hp < 10:
                    print(row['player_name'])
            print("BOSS")
            for row in sortedlist:
                int_hp = int(row['hp'])
                if int_hp > 10:
                    print(row['player_name'])








