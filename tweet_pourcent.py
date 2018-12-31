"""
    Calculate the percentage we are in the year, and tweet it.
"""
from datetime import datetime, date
import tweepy
import emoji

PROGRESS_BAR_SIZE = 25

#Your Twitter API credentials
CONSUMER_KEY = '<consumer key>'
CONSUMER_SECRET = '<consumer secret>'
ACCESS_TOKEN = '<access token>'
ACCESS_TOKEN_SECRET = '<access token secret>'


def progress_bar(percentage: int, size: int):
    """
        Build and returns a progress bar.
    """
    proggress = " | "
    for i in range(size):
        if percentage * size / 100 >= i:
            proggress += "#"
        else:
            proggress += "-"
    proggress += " | "
    return proggress


def percentage_year():
    """
        Calculate and returns the current year percentage.
    """
    current_year = datetime.now().year
    start = date(current_year, 1, 1).toordinal()
    next_year = date(current_year + 1, 1, 1).toordinal()
    days_in_current_year = next_year - start
    now = date.today().toordinal()
    current_day_in_year = now - start
    return (current_day_in_year * 100) / days_in_current_year

def tweet_it(text: str):
    """
        Tweet a given text.
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(text)

def launch():
    """
        Starts the program. The beginning.
    """
    text_to_tweet = "Bonjour Twitter ! :hatching_chick: "
    text_to_tweet += "Nous sommes le  " + datetime.today().strftime('%d-%m-%Y') + " ! "
    text_to_tweet += "Nous sommes actuellement à " + progress_bar(
        int(percentage_year()), PROGRESS_BAR_SIZE) + str(
            int(percentage_year())) + "% de cette année "
    text_to_tweet += str(datetime.now().year) + " ! :fire: "
    text_to_tweet += "Bonne journée !"
    tweet_it(emoji.emojize(text_to_tweet))


if __name__ == "__main__":
    launch()
