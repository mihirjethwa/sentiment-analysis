# from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask import render_template
from flask import request
# import pandas as pd
from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
from reddit_per_day import get_data, get_date
from player_popularity import get_count,get_names,players
from football_player_popularity import get_fcount,get_fnames,fplayers

app = Flask(__name__ ,template_folder='templates')

@app.route('/home')  
def home():  
    return render_template('home.html');  

@app.route('/abusive_content')  
def abusive_content():  
    return render_template('abusive_words.html');  

@app.route("/reddit_per_day", methods =["GET", "POST"])
def reddit_per_day():
    
    hours = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    newDate = ""
    if request.method == "POST":
        newDate = request.form.get("dates")
        newSubreddit = request.form.get("sreddit")
        print("new: ",newSubreddit)
        print("nwe date: ", get_date(newDate,newSubreddit))
    values = get_data()
    return render_template('reddit_posts.html', values=values, labels=hours )


@app.route('/player_popularity', methods =["GET", "POST"])
def player_popularity():
    values = get_count()
    labels = get_names()

    if request.method == "POST":
        first_name = request.form.get("cname")
        count = players(first_name.lower())
        labels.append(first_name)
        values[0].append(count[0])
        values[1].append(count[1])
        values[2].append(count[2])

    return render_template('player_popularity.html', rvalues=values[0],tvalues=values[1],yvalues=values[2], labels=labels)

@app.route('/football_player_popularity', methods =["GET", "POST"])
def football_player_popularity():
    fvalues = get_fcount()
    flabels = get_fnames()

    if request.method == "POST":
        first_name = request.form.get("fname")
        count = fplayers(first_name.lower())
        flabels.append(first_name)
        fvalues[0].append(count[0])
        fvalues[1].append(count[1])
        fvalues[2].append(count[2])

    return render_template('football_player_popularity.html', rfvalues=fvalues[0],tfvalues=fvalues[1],yfvalues=fvalues[2], flabels=flabels)

if __name__ == "__main__":
    app.run(debug=True)

