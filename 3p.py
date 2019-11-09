

g = raw_input("Do you wanna check out Team Members[1] or Enemies[2]")
print g
import csv

noise_amp=[]         #an empty list to store the second column
with open('demo.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
      noise_amp.append(row[1])


noise_amp=[]         #an empty list to store the second column
with open('demo.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
      noise_amp.append(row[1])


      ask = raw_input("Do you wanna check out Team Members[1] or Enemies[2]")
print ask
int_ask = int(ask)
import csv

name = []  # an empty list to store the second column
eng_name = []
attack = []
a = 1
b = 2
with open('enemies.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        name.append(row[1])
        eng_name.append(row[2])
        attack.append(row[4])



if int_ask == 1: print name

if int_ask == 2: print eng_name

if int_ask == 4:
    attack.sort()
    print attack
 #works1
    with open('enemies.csv','r') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row: (row['attack']), reverse=False)
    pp = pprint.PrettyPrinter(depth=6)
   # pp.pprint(sortedlist[1])
    for row in sortedlist:
        print(row['player_name'],row['eng_name'])
    
#works2

with open('enemies.csv','r') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row: (row['attack']), reverse=False)

    reverselist= sorted(sortedlist, reverse=True)
   # pp = pprint.PrettyPrinter(depth=6)
   # pp.pprint(reverselist)
    if int_ask == 2:
        ask2 = raw_input("Do you wanna check out enemy list[a] or enemy listed by stats[b]")
        if ask2 == 'a':
            for row in sortedlist:
                print(row['player_name'])
        if ask2 == 'b':
            ask3 = raw_input("Do you want the strengths in ascending(i) or descending(ii) order?")
            if ask3 == 'i':
                for row in sortedlist:
                    print(row['player_name'], row['eng_name'])
            if ask3 == 'ii':
                for row in reverselist:
                    print(row['player_name'], row['eng_name'])

#works 3
with open('enemies.csv','r') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=",")
    sortedlist = sorted(spamreader, key=lambda row: (row['attack']), reverse=False)

    reverselist= sorted(sortedlist, reverse=True)
   # pp = pprint.PrettyPrinter(depth=6)
   # pp.pprint(reverselist)
    if int_ask == 2:
        ask2 = raw_input("Do you wanna check out enemy list[a], enemy listed by stats[b], or enemy listed by type[c]")
        if ask2 == 'a':
            for row in sortedlist:
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

#################

import csv
import pprint


i=0


while i == 0:

    ask = raw_input("Do you wanna check out Team Members[1] or Enemies[2] Press q to exit")
    if ask == "q":
        break
    int_ask = int(ask)


    with open('enemies.csv','r') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=",")
        sortedlist = sorted(spamreader, key=lambda row: (row['attack']), reverse=False)

        reverselist= sorted(sortedlist, reverse=True)

    with open('members.csv', 'r') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=",")
        memberlist = sorted(spamreader, key=lambda row: (row['Total']), reverse=False)

        reverselist = sorted(sortedlist, reverse=True)



        if int_ask == 1:
            ask2 = raw_input("Do you wanna check out team member list[a], output the members' profession[b], list total money[c], or list out transactions[d]")
            if ask2 == 'a':
                for row in memberlist:
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
                    if row['role'] == 'Programmer':
                        print(row['name'])
            if ask2 == 'c':
                for row in memberlist:
                    print(row['name'], row['Total'])


        if int_ask == 2:
            ask2 = raw_input("Do you wanna check out enemy list[a], enemy listed by stats[b], or enemy listed by type[c]")
            if ask2 == 'a':
                for row in sortedlist:
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