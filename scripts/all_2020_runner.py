import twint
import pandas as pd
import time

# def fixTime(string):
# 	curr_time = int(string[11:13]) + 8
# 	if curr_time > 23:
# 		curr_time -= 23
# 		curr_date = int(string[9]) + 1
# 		string = string[:9] + str(curr_date) + string[10:]
# 	if curr_time < 10:
# 		string = string[:11] + '0' + str(curr_time) + string[13:]
# 	else:
# 		string = string[:11] + str(curr_time) + string[13:]
# 	return string

# print("here")
c = twint.Config()

c.Limit = 1000
c.Search = "Trump OR Biden OR COVID"
c.Store_csv = True
c.Output = ("All_Tweets.csv")
# c.Until = "2020-12-31 21:00:00"

c.Show_hashtags = True
c.Retweets = True
c.Popular_tweets = True
c.Filter_retweets = True
c.Hide_output = True
# 
allMonths = {"01": "31", "02": "29", "03": "31", "04": "30", "05": "31", "06": "30", "07": "31", "08": "31", "09": "30", "10": "31", "11": "30", "12": "31"}

current = "2020-12-32 21:00:00"

def previousDay(string):
	curr_date = int(string[8:10]) -1
	curr_month = string[5:7]
	if curr_date == 0:
		curr_month = int(curr_month) - 1
		if curr_month < 10:
			curr_month = "0" + str(curr_month)
		else:
			curr_month = str(curr_month)
		curr_date = allMonths[curr_month]
	elif curr_date < 10:
		curr_date = "0" + str(curr_date)
	else:
		curr_date = str(curr_date)
	return string[:5] + curr_month + string[7] + curr_date + string[10:]

while current != "2020-01-01 21:00:00":
	current = previousDay(current)
	c.Until = current
	t0 = time.time()
	twint.run.Search(c)
	t1 = time.time()
	total = t1-t0
	print(total)
	print(current)

# while keepGoing:
# 	try:
# 		c.Until = fixTime(min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['date']) + ' ' + min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['time']))
# 		print(c.Until)
# 		t0 = time.time()
# 		twint.run.Search(c)
# 		t1 = time.time()

# 		total = t1-t0
# 		print(total)
# 		time.sleep(5)
# 	except KeyboardInterrupt:
# 		print("keyboard")
# 		print(min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['date']) + ' ' + min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['time']))
# 		break
# 	except:
# 		print("error lol")
# 		t1 = time.time()

# 		total = t1-t0
# 		print(total)
# 		time.sleep(5)