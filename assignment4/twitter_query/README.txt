usage: twitter_query.py [-h] -u U [-n N]

get certain user twitters.

optional arguments:
  -h, --help  show this help message and exit
  -u U        handle of the user
  -n N        user's N most recent twitters


# Example:
python3 twitter_query.py -u LeoDiCaprio
python3 twitter_query.py -u LeoDiCaprio -n 5


# Explanation

## This script directly use the tweepy api to fetch latest N numbers of latest tweets from the customer's timeline
   and the date of the tweets.
## -u and -n is set to reburied parameters for easy reading of the command
## replies and retweets are counted as the customers tweets in this script
## images, emoji is not specially handled in this script
