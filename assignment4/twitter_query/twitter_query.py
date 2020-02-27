import argparse
import tweepy

parser = argparse.ArgumentParser(description='get certain user twitters.')

parser.add_argument('-u', required=True, type=str, help='handle of the user')

parser.add_argument('-n', required=False, type=int, default=1, help='user\'s N most recent twitters ')

args = parser.parse_args()

if args.u:
    user = args.u
if args.n:
    number = args.n


consumer_key = "enX88ZwYrs6j06zyX1fQvIDmU"
consumer_secret = "PLYNUXdqfU39NSkDTAC0qCnjeiXJM3qnlfP7YzcbyWX8O1EhvU"
access_token = "1229723138461749248-xifzp6qXZqhXVixQ4a9HpNHteFGtXu"
access_token_secret = "ADtZTGfEqQCRX9dTWn42xWaiINktBseLTi4kvfPwnanUi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline(user, count=number)

for tweet in public_tweets[:]:
    print(tweet.created_at, tweet.text)




