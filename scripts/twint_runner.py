import twint
import pandas as pd
import time

def fixTime(string):
	curr_time = int(string[11:13]) + 8
	if curr_time > 23:
		curr_time -= 23
		curr_date = int(string[9]) + 1
		string = string[:9] + str(curr_date) + string[10:]
	if curr_time < 10:
		string = string[:11] + '0' + str(curr_time) + string[13:]
	else:
		string = string[:11] + str(curr_time) + string[13:]
	return string

print("here")
c = twint.Config()

c.Search = "Trump"
# c.Store_object = True
# c.Limit = 100
c.Store_csv = True
c.Output = ("Trump_Tweets_11_3_20_try4.csv")
c.Since = "2020-11-01"
c.Until = "2020-11-04"

c.Show_hashtags = True
c.Retweets = True
c.Popular_tweets = True
c.Lang = 'en'
c.Filter_retweets = True
c.Hide_output = True
# c.Stats = True
# c.Location = True 
keepGoing = True
while keepGoing:
	try:
		c.Until = fixTime(min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['date']) + ' ' + min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['time']))
		print(c.Until)
		t0 = time.time()
		twint.run.Search(c)
		t1 = time.time()

		total = t1-t0
		print(total)
		time.sleep(5)
	except KeyboardInterrupt:
		print("keyboard")
		print(min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['date']) + ' ' + min(pd.read_csv("Trump_Tweets_11_3_20_try4.csv")['time']))
		break
	except:
		print("error lol")
		t1 = time.time()

		total = t1-t0
		print(total)
		time.sleep(5)
# tweets_as_objects = twint.output.tweets_list
print(twint)
# for tweet in tweets_as_objects:
# 	print(tweet.name)
# print(len(tweets_as_objects))