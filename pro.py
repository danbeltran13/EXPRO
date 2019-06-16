
import matplotlib.dates as dates
import matplotlib.pyplot as pyplot
import tkinter
from numpy import interp

FILE = 'ex3.csv'
file = open(FILE,'r')




# CREATED DICTIONARIES OF EACH DAY SO THAT EXCERCISES CAN BE ADDED
DAYS = []

# SAVES FIRST COLUMN
INFO = []

# SAVES ALL EXCERCISES
EXLIST = ['DATES','TIME','WEIGHT','BODY FAT']

# FOLLOWING LINE CREATES AN ARRAY OF DATES
DATES = file.readline().rstrip("\n").split(',')

INFO.append(DATES[0])
DATES.remove(DATES[0])
CurrentEx = []
for i in range (0,len(DATES)):
    # CREATES A DICTIONARY WITH FIRST VALUE OF DATE
    DAYS.append({'DATE':DATES[i]})

    #CREATE A LIST OF THE TOTAL LENGHT OF DATA
    CurrentEx.append('')
i = 0


for line in file:
    # PREPARES LINE TO BE READABLE
    DATA = line.rstrip('\n').split(',')

    # SAVES THE  THE FIRST COLUMN
    INFO.append(DATA[0])


    if (DATA[0]) == 'TIME':

        for j in range(1,len(DATA)):
            DAYS[j-1].update({'TIME': DATA[j]})

    if DATA[0] == 'WEIGHT':
        for j in range(1,len(DATA)):
            DAYS[j-1].update({'WEIGHT': DATA[j]})
    if DATA[0] == 'BODY FAT':
        for j in range(1,len(DATA)):
            DAYS[j-1].update({'BODY FAT': DATA[j]})



    if DATA[0] == 'EX':
        # if CURRENTEX IS LESS THAN DATA
        for j in range(1,len(DATA)):


            # UPDATES CURRENT EX EVEN IF EMPTY
            CurrentEx[j-1] = DATA[j]
            if ((CurrentEx[j-1].strip() not in  EXLIST ) and (CurrentEx[j-1].strip() != '')):
                EXLIST.append(CurrentEx[j-1].strip())

            if DATA[j] != '':
                DAYS[j-1].update({DATA[j]:[]})

    if (DATA[0][0:3] == 'SET') or (DATA[0] == 'WU'):
        for j in range(1,len(DATA)):
            if DATA[j] != '':

                DAYS[j-1][CurrentEx[j-1]].append(DATA[j])
    i += 1

def convertTime(String):
    time = String.split(' ')

    time[0] = time[0].replace(':','')
    if time[1] == 'PM' and time[0][0:2] !='12':
        time[0] = int(time[0])+1200
    elif time[0]=='1200' and time[1] == 'AM':
        time[0] = 0
    elif time[0][0:2]=='12' and time[1]== 'PM':
        time[0]= int(time[0])
    else:
        time[0] = int(time[0])
    return time[0]

def calculateBF(String):
    me = String.split('/')
    ave = 0
    for i in range(0,len(me)):
        ave  += float((me[i]))
    ave /= len(me)

    if ave < (1/4):
        return interp(ave,[0,(1/4)],[5,8])  # PROBLEM NEARING 0 PINCH
    if ave <(1/2):
        return interp(ave, [(1/4), (1 / 2)], [9, 13])
    if ave<(3/4):
        return interp(ave, [(1/2), (3/4)], [14, 18])
    if ave < (1):
        return interp(ave, [(3/4), (1)], [19, 22])
    if ave<(3/2):
        return interp(ave, [(1), (3/2)], [23, 27])
    if ave < (2):
        return interp(ave, [(3/2), (2)], [28, 32])
    if ave <(5/2):
        return interp(ave, [2, (5/2)], [33, 40])







# VOLUME IS USED TO AS A MEASUE TO CALCULATE PROGRESS
def returnList (String, Volume = True, MAX = False):

    # IF DATES IS REQUESTED THEN RETURNS LIST USED IN PROGRAM
    if String == 'DATES':
        return DATES


    # THIS IS USED FOR ALL OTHER REQUESTS
    else:
        # RETURN LIST
        t = []
        # LOOPS THOURGHOUT ALL DAYS IN ORDER TO RETRIEVE DATA
        for i in range(0,len(DAYS)):

            # IF THE DAY HAS THE REQUESTED EXRECISE
            if String in DAYS[i]:

                # VOLUME IS USED TO MEASURE PROGRESS OF AN EXRECISE, WILL BE THE DEFAULT, FOUND BY MULTIPYLING SETS BY REPS

                if Volume:

                    # FINDS THE VOLUME OF THE FIRST SET IF NOT EMPTY, APPENDS A VALUE IN ANY CASE SO THAT
                    #  CAN BE USED WITH OTHER ARRAYS
                    # DAYS[i] - PICKS A DAY, [String] - PICKS EXCERCISE IN DICTIONARY, [int] - SET OF AN EXCERCISE (A STRING)
                    if DAYS[i][String] != '':

                        # WE ARE ONLY FINDING THE VOLUME OF THE FIRST SET
                        totalVolume = 0
                        max = 0
                        for j in range(0,len(DAYS[i][String])):
                            w = DAYS[i][String][j].split('/')
                            print(w)
                            # LOOPS THOUGH 2 THINGS
                            for k in range(0, len(w)):
                                w[k] = float(w[k])

                            if max < w[0]:
                                max = w[0]

                            s = 1
                            for m in w:
                                s *= m
                            totalVolume += s

                        if MAX == True:
                            t.append(MAX)
                        else:
                            t.append(totalVolume)


                    # SAVES AN EMPTY SPACE IF SET IS EMPTY
                    else:

                        t.append(DAYS[i][String])
                else:
                    if String == 'WEIGHT':
                        if DAYS[i][String] != '':
                            t.append(float(DAYS[i][String]))
                        else:
                            t.append(DAYS[i][String])
                    if String == 'TIME':
                        if DAYS[i][String] != '':

                            t.append((convertTime((DAYS[i][String]))))

                        else:
                            t.append(DAYS[i][String])
                    if String == 'BODY FAT':
                        if DAYS[i][String] != '':

                            print(DAYS[i][String],2)
                            t.append(calculateBF(DAYS[i][String]))
                        else:
                            t.append(DAYS[i][String])

            else:
                t.append('')

        return t


# THIS METHOD WILL MAKE SURE LISTS HAVE SAME LENGHT
def fixLenght(arrayone, arraytwo,number = 1):
    # REMOVES DATE WHEN EXCERSICE IS NOT PRESENT
    loopcounter = 0
    while loopcounter < len(arrayone):

        # REMOVES
        if arraytwo[loopcounter] == '':
            arraytwo.remove(arraytwo[loopcounter])
            arrayone.remove(arrayone[loopcounter])
            loopcounter -= 1
        loopcounter += 1
        if number == 1:
            fixLenght(arraytwo,arrayone,number = 2)


def ExList():
    return EXLIST




