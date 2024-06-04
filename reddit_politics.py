# from apscheduler.schedulers.blocking import BlockingScheduler

import requests
# import pandas as pd
from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
#hello
# authenticate API
client_auth = requests.auth.HTTPBasicAuth(
    'rZmRewfww0-Fh9WJWV_W0g', 'DQ_JPxv6pfmVonP_e639CKqqPs14GQ')
data = {
    'grant_type': 'password',
    'username': 'CS515Tester',
    'password': 'admintest99'
}
headers = {'User-Agent': 'MyBot/0.0.'}
# send authentication request for OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=client_auth, data=data, headers=headers)
# extract token from response and format correctly
TOKEN = f"bearer {res.json()['access_token']}"
headers = {**headers, **{'Authorization': TOKEN}}

params = {'limit':1000}

subreddit_name = 'soccer'
print(subreddit_name)
hours = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}

def increment_count_according_to_date(datey, time):
    hour = time[1:3]
    file1 = open('myfile.txt', 'r')
    filelines = file1.read()
    file1.close()
    line_dict = json.loads(filelines)
    
    dict_dates = line_dict["counts"]

    #print(dict_dates,"Before")
    if datey in dict_dates:
        hour_dict = dict_dates[datey]
        if hour in hour_dict:
            hour_dict[hour] +=1
        else:
            hour_dict[hour] =1
    #print(dict_dates,"After")
    else:
        dict_dates[datey] = hours
        hour_dict = dict_dates[datey]
        if hour in hour_dict:
            hour_dict[hour] +=1
        else:
            hour_dict[hour] =1
    
    dict_dates[datey] = hour_dict

    line_dict["counts"]  = dict_dates
    file2 = file1 = open('C:/Users/Jwalant/Desktop/SocMedia/project2/myfile.txt', 'w')
    file2.write(json.dumps(line_dict))
    file2.close()

    

def open_file_and_return_uniqueness(post_id):
    file1 = open('C:/Users/Jwalant/Desktop/SocMedia/project2/myfile.txt', 'r')
    filelines = file1.read()
    file1.close()
    line_dict = json.loads(filelines)
    ID_list = line_dict["IDs"]
    if post_id in ID_list:
        return False
    else:
        ID_list.append(post_id)
        line_dict["IDs"] = ID_list
        file2 = open('myfile.txt', 'w')
        file2.write(json.dumps(line_dict))
        file2.close()
        return True

# params = {}
def df_from_response(res):
    reached_oct = False
    after_id = res.json()["data"]["after"]
    for post in res.json()['data']['children']:
        global count
        post = {
            'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'ups': post['data']['ups'],
            'downs': post['data']['downs'],
            'score': post['data']['score'],
            'link_flair_css_class': post['data']['link_flair_css_class'],
            'created_date': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%dT'),
            'created_time': datetime.fromtimestamp(post['data']['created_utc']).strftime('T%H:%M:%SZ'),
            'id': post['data']['id'],
            'kind': post['kind']
        }
        #print(post["created_date"],"\n")
        if((open_file_and_return_uniqueness(post["id"])) == True):
            print(post["id"])
            #look up date in doct and increment count for the vALue of tat particular date. If not already present, then add that date to the dict as a key.
            print(type(post["created_time"]))
            print(post["created_time"])
            increment_count_according_to_date(post["created_date"], post["created_time"])
            

        if "10-30" in post["created_date"]:
            print("DATE OUT")
            reached_oct = True
        
    if reached_oct:
        print("This is date when reached_oct is None: " + post["created_date"])
        return None
    else:
        return after_id

#def fetch_submissions():
#print(count)
res = requests.get("https://oauth.reddit.com/r/"+ subreddit_name+"/?t=month",
                       headers=headers,
                       params = params)

print(type(res))
#print(res.json()["data"]["children"])
after_id = df_from_response(res)
#print("Page 1 ends")
                    

def get_all_pages():
    while True:
        global after_id
        res = requests.get("https://oauth.reddit.com/r/"+ subreddit_name+"/?t=month&after="+after_id,
                       headers=headers,
                       params = params)
        after_id = df_from_response(res)
        if after_id == None:
            print("HITTTTT")
            break
        print("PAGE ENDSSSS\n")
        

get_all_pages()

file1 = open("myfile.txt", "r")
fileline = file1.read()
file1.close()
line_dict = json.loads(fileline)
dates = line_dict['counts']
print("Len of dates: ",dates)
for elem in dates:
    print (elem, len(dates[elem]))
    
#print(dates)
df = pd.DataFrame(dates)

df = df.sort_index(0,0)
#print(df)


#plt.show()
date = "2022-12-07T"
if date in dates:
    print(dates[date])
    plot_this_dict = dates[date]
else:
    print("NOPE")
listy = []
for i in sorted(plot_this_dict):
    listy.append(plot_this_dict[i])

print("This listy: \n", listy)


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# List of data points
data = listy
hours = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17",'18','19','20','21','22','23']
# Plot bar chart with data points
plt.bar(hours,data)

# Display the plot
plt.show()