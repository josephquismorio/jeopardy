import os
import csv
import time
import random
from random import shuffle, choice
import fuzzywuzzy 
from fuzzywuzzy import fuzz

score = 0
bool = True
wager = 0

def read(d, db, c, v, q, co):
    global bool
    global wager
    if db != "yes" and co != " - ":
        print('(From', str(d).split(),') The category is', str(c), 'for $', int(v), '. \n')
        print(q, '\n')
    elif db != "yes" and co == " - ":
        print('(From', str(d).split(),') The category is', str(c), 'for $', int(v), '. \n')
        print(q, '\n')
        print(co, '\n')
    elif db == "yes" and co != " - ":
        print("You've got a daily double!\n")
        wager = input("Enter your wager: ")
        if wager == "!q":
            exit()
        else:
            while int(wager) > score or int(wager) < 0:
                wager = input("Enter a valid wager: ")
            if int(wager) == score:
                print("A true daily double.\n")
            print('(From', d,') The category is', c, 'for $', wager, '. \n')
            print(q, '\n')
    elif db == "yes" and co == " - ":
        print("You've got today's daily double!\n")
        wager = input("Enter your wager: ")
        if wager == "!q":
            exit()
        else:
            while int(wager) > score or int(wager) < 0:
                wager = input("Enter a valid wager: ")
            if int(wager) == score:
                print("A true daily double.\n")
            print('(From', d,') The category is', c, 'for $', wager, '. \n')
            print(q, '\n')
            print(co, '\n')

def ask():
    global score
    global bool
    global wager
    while bool == True:
        filesize = os.path.getsize('/your/dir/jeopardy.tsv')
        offset = random.randrange(filesize)

        f = open('/your/dir/jeopardy.tsv')
        f.seek(offset)
        f.readline()
        q = f.readline()
        categories = q.split("\t")

        value = categories[0]
        dbl = categories[1]
        category = categories[2]
        comments = categories[3]
        question = categories[4]
        answer = categories[5]
        date = categories[6]
        date.split()

        if len(q) == 0:
            f.seek(0)
            q = f.readline()
            categories = q.split("\t")
           
            value = categories[0]
            dbl = categories[1]
            category = categories[2]
            comments = categories[3]
            question = categories[4]
            answer = categories[5]
            date = categories[6]
            date.split()

        read(date, dbl, category, value, question, comments)

        t = 3
        while t > 0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        val = input("Enter an answer: ")
        ratio = fuzz.ratio(answer.lower(), val.lower())

        if 75 <= ratio <= 100:
            print("Correct! The answer was indeed:", answer, "\n")
            score+=int(value)
            score+=int(wager)
            print("Your score is: ", score)
        elif ratio < 75 and val != "!q":
            print("Wrong! The answer was: ", answer, "\n")
            score-=int(value)
            score-=int(wager)
            print("Your score is: ", score)
        elif val == "!q":
            print("Your final score was: ", score)
            bool = False
        

ask()
