from flask import Flask
from flask import render_template
# from app import new_player
import requests
from matplotlib import pyplot as plt
import numpy as np

word1 = "suryakumar" 
word2 = "rizwan"
word3 = "conway"
word4 = "babar"
word5 = "jadeja"
word6 = "afridi"
word7 = "rahul"
word8 = "shakib"
word9 = "starc"
word10 = "curran"

labels = [ ]
pname = ""
pcount = []
def players(name):
    print("in player_popularity: ",name)
    global pname, pcount
    pname = name
    pcount = [0,0,0]
    with open("reddit_cricket.csv",encoding='UTF-8') as f2:
        for line in f2:
            words = line.lower().split()
            for i in words:
                if (i==pname):
                    pcount[0] += 1
    with open("twitter_cricket.csv",encoding='UTF-8') as f:
        for line in f:
            words = line.lower().split()
            for i in words:
                if (i==pname):
                        pcount[1] += 1
    with open("youtube_cricket.csv",encoding='UTF-8') as f3:
        for line in f3:
            words = line.lower().split()
            for i in words:
                if (i==pname):
                        pcount[2] += 1
    return pcount

rcount = [0,0,0,0,0,0,0,0,0,0]
with open("reddit_cricket.csv",encoding='UTF-8') as f2:
    
    for line in f2:
        words = line.lower().split()
        for i in words:
            if(i==word1):
                rcount[0]+=1
            if (i==word2):
                rcount[1]+=1
            if (i==word3):
                rcount[2]+=1
            if (i==word4):
                rcount[3]+=1
            if (i==word5):
                rcount[4]+=1
            if (i==word6):
                rcount[5]+=1
            if (i==word7):
                rcount[6]+=1
            if (i==word8):
                rcount[7]+=1
            if (i==word9):
                rcount[8]+=1
            if (i==word10):
                rcount[9]+=1
reddit=[rcount[0],rcount[1],rcount[2],rcount[3],rcount[4],rcount[5],rcount[6],rcount[7],rcount[8],rcount[9]]

tcount = [0,0,0,0,0,0,0,0,0,0]
with open("twitter_cricket.csv",encoding='UTF-8') as f:
    for line in f:
        words = line.lower().split()
        for i in words:
            if(i==word1):
                tcount[0]+=1
            if (i==word2):
                tcount[1]+=1
            if (i==word3):
                tcount[2]+=1
            if (i==word4):
                tcount[3]+=1
            if (i==word5):
                tcount[4]+=1
            if (i==word6):
                tcount[5]+=1
            if (i==word7):
                tcount[6]+=1
            if (i==word8):
                tcount[7]+=1
            if (i==word9):
                tcount[8]+=1
            if (i==word10):
                tcount[9]+=1
twitter=[tcount[0],tcount[1],tcount[2],tcount[3],tcount[4],tcount[5],tcount[6],tcount[7],tcount[8],tcount[9]]

ycount = [0,0,0,0,0,0,0,0,0,0]
with open("youtube_cricket.csv",encoding='UTF-8') as f3:
    for line in f3:
        words = line.lower().split()
        for i in words:
            if(i==word1):
                ycount[0]+=1
            if (i==word2):
                ycount[1]+=1
            if (i==word3):
                ycount[2]+=1
            if (i==word4):
                ycount[3]+=1
            if (i==word5):
                ycount[4]+=1
            if (i==word6):
                ycount[5]+=1
            if (i==word7):
                ycount[6]+=1
            if (i==word8):
                ycount[7]+=1
            if (i==word9):
                ycount[8]+=1
            if (i==word10):
                ycount[9]+=1
youtube=[ycount[0],ycount[1],ycount[2],ycount[3],ycount[4],ycount[5],ycount[6],ycount[7],ycount[8],ycount[9]]

labels.append(word1)
labels.append(word2)
labels.append(word3)
labels.append(word4)
labels.append(word5)
labels.append(word6)
labels.append(word7)
labels.append(word8)
labels.append(word9)
labels.append(word10)

y_Axis = [reddit, twitter, youtube]
x_Axis = labels

def get_names():
    return x_Axis

def get_count():
    return y_Axis