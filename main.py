# Made by @Khedoe > Arief Khedoe | Nederland

# import modules 

# If needed install tweepy > pip install tweepy
import tweepy


# Login API (Twitter)

consumer_key = "enter between quotes"
consumer_secret = "enter between quotes"
access_token = "enter between quotes"
access_token_secret = "enter between quotes"

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()
api = tweepy.API(oauth)

# Post

message = "Type your message/Tweet"

api.update_status(message)

# If posted:
print("Your Tweet has been posted")