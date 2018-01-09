import tweepy
import csv
import time
  
csv=open("graph.csv","w");

# Consumer keys and access tokens, used for OAuth
consumer_key        = '########'
consumer_secret     = '########'
access_token        = '########'
access_token_secret = '########'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Creation of the actual interface, using authentication
user_name='Peter'
user = api.get_user(user_name)

friendlist=[]

for friend in user.friends():
	friendlist.append(friend.screen_name)

for list in friendlist:
	csv.write(user_name+","+list+"\n")
for list in friendlist:
	user1=api.get_user(list)
	for friend2 in user1.friends():
		csv.write(list+","+friend2.screen_name+"\n")

for list in friendlist:
	user1=api.get_user(list)
	for friend2 in user1.followers():
		csv.write(friend2.screen_name+","+list+"\n")


