import os
import csv
from posixpath import split
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
    print(f"Your earnings cash in at {score}$. \n")
    if db != "yes" and co != " - ":
        print(f'(From {str(d).split()[0]}) The category is {c} for ${v}. \n')
        print(q, '\n')
    elif db != "yes" and co == " - ":
        print(f'(From {str(d).split()[0]}) The category is {c} for ${v}. \n')
        print(q, '\n')
        print(co, '\n')
    elif db == "yes" and co != " - ":
        print("You've got a daily double!\n")
        wager = input("Enter your wager: ")
        if wager == "!q":
            exit()
        elif score > 999:
            while int(wager) > score or int(wager) < 0:
                wager = input("Enter a valid wager: ")
                if wager == "!q":
                    exit()
            if int(wager) == score:
                print("A true daily double.\n")
            print(f'(From {str(d).split()[0]}) The category is {c} for ${wager}. \n')
            print(q, '\n')
        elif score <= 999:
            while int(wager) > 1000 or int(wager) < 0:
                wager = input("Enter a valid wager: ")
                if wager == "!q":
                    exit()
            if int(wager) == score:
                print("A true daily double.\n")
            print(f'(From {str(d).split()[0]}) The category is {c} for ${wager}. \n')
            print(q, '\n')

    elif db == "yes" and co == " - ":
        print("You've got today's daily double!\n")
        wager = input("Enter your wager: ")
        if wager == "!q":
            exit()
        elif score > 999:
            while int(wager) > score or int(wager) < 0:
                wager = input("Enter a valid wager: ")
                if wager == "!q":
                    print(f"Your total earnings were {score}$.")
                    exit()
            if int(wager) == score:
                print("A true daily double.\n")
            print(f'(From {str(d).split()[0]}) The category is {c} for ${wager}. \n')
            print(q, '\n')
            print(co, '\n')
        elif score <= 999:
            while int(wager) > 1000 or int(wager) < 0:
                wager = input("Enter a valid wager: ")
                if wager == "!q":
                    print(f"Your total earnings were {score}$.")
                    exit()
            if int(wager) == score:
                print("A true daily double.\n")
            print(f'(From {str(d).split()[0]}) The category is {c} for ${wager}. \n')
            print(q, '\n')

def ask():
    global score
    global bool
    global wager
    while bool == True:
        filesize = os.path.getsize('/your/directory/jeopardy.tsv')
        offset = random.randrange(filesize)

        f = open('/your/directory/jeopardy.tsv')
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

        read(date, dbl, category, value, question, comments)

        t = 3
        while t > 0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

        val = input("Enter an answer: ")
        print("\n")
        while val == "":
            val = input("Are you sure? Enter something: ")
        ratio = fuzz.ratio(str(answer.lower().split()[0]), str(val.lower().split()[0]))

        if 70 <= ratio <= 100:
            print(f"Correct! The answer was indeed: {answer} \n")
            score+=int(value)
            score+=int(wager)
        elif ratio < 75 and val != "!q" and val != "!c":
            print(f"Wrong! The answer was: {answer} \n")
            score-=int(value)
            score-=int(wager)
        elif val == "!q":
            print(f"The answer was: {answer} \n")
            print(f"Your total earnings were {score}$.")
            bool = False
        elif val == "!c":
            score = 0
            print("Cleared score.")

ask()
