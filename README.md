# Tweet Analysis 2020
### Trevor Carpenter, under advisement of Dr. Setareh Rafatirad

## Introduction
The idea behind this project is to perform a Knowledge Extraction on twitter data throughout 2020, specifically correlated to major events. Our primary question is simply having to do with what trends we can find in the data set. Our secondary questions are more malleable based on what we find, however specifically we want to look at political parties, sentiment analysis, and the polarization of sentiment throughout the year. If we are able to achieve all of these, our hypothesis is that we will observe the sentiment of tweets from each political party getting more and more extreme over time.

## Important Tools
- **tweepy**: python library for mining tweets directly from twitter
- **twint**: python library built around tweepy without rate limits. Better for long term scraping
- **requests** and **bs4**: python libraries for web scraping on news websites to find important dates

## Initial Process Idea (rough)
1. Mine dates to find out important events throughout the year
2. Find out trending hashtags/people and mine the tweets regarding the event
3. Identify political placement for each user based on their tweets. Maybe use a rolling scale of -1 to 1, -1 being liberal and 1 being conservative. (this will be a heavy action, using NLP, RNN and a classifier that could take a bulk of the project)
4. Perform sentiment analysis on the tweets. Understand how strong their feelings are toward the subject.
5. Look for correlations between political placement and sentiment for each topic.
6. Map how all of these visuals and relationships for each topic individually act throughout the year as a whole.

## Progress So Far:
1. First I was able to mine important dates to get an idea of when to look at various events. From this, I know that I want to start any large analysis for the year on March 13 2020, the date when Trump first announced the state of emergency as a result of the Coronavirus.
2. Mining old tweets proved to be very difficult, so I opted to mine recent tweets to practice various methods that I then planned to utilize at a later date with old tweets. Gained approximately 400K Tweets at time of Biden Inauguration in 2021 that would correctly.
3. Created first visuals of the data using values such as place location.
4. Was able to implement a CNN to identify Bots in data with ~90% accuracy using github at https://github.com/marcopoli/Identification-of-Twitter-bots-using-CNN. Primary file for bots is found in  `BotClassification/findBots.py`. I would like to continue to edit this file to speed up the process since the bot classification is relatively slow(recently have found information on using threading in keras that could be very useful)
5. Found and made first use of `twint`, the library I plan to use for actually mining older tweets. This has no rate limits but may be a little harder to use. I have also found so far that having massive amounts of data is good, but for actual calculations such as analyzing bot percentages, it might make sense time-wise to use a random sample of that data.

## Next Steps:
1. Write abstract to submit.
2. Get a sample of the inauguration data, apply ML techniques, and make visuals.
3. Mine tweets from March 13th timeline and see if there are differences in twint's method of mining.
