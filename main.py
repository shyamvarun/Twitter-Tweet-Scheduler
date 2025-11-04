import tweepy
import os
from datetime import datetime, timedelta

# Load Twitter API credentials from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def days_until_birthday(month=10, day=23):
    now = datetime.now()
    current_year = now.year
    birthday_this_year = datetime(current_year, month, day)
    # If birthday has passed this year, use next year
    if now >= birthday_this_year:
        birthday_next = datetime(current_year + 1, month, day)
    else:
        birthday_next = birthday_this_year
    delta = birthday_next - now
    return delta.days

def main():
    days = days_until_birthday()
    if days == 0:
        msg = "Happy Birthday Prabhas"
    else:
        msg = f"{days}"
    api.update_status(msg)
    print(f"Tweet posted: {msg}")

if __name__ == "__main__":
    main()
