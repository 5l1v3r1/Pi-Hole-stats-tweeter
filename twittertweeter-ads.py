#Send tweet when script is called

import tweepy
import datetime
import json
import urllib
from urllib.request import urlopen

# Retrieve data and load it into a dictionary
data = urlopen('path/to/admin/api.php').read() #bytes
body = data.decode('utf-8')
data = json.loads(body)

# Create tweet, adjust %.2f for amount of decimals you want
template_tweet = "\nAds Blocked: %s\nAds Percentage Today: %.2f\nDNS Queries Today: %s\nDomains Being Blocked: %s"
data = template_tweet % (data['ads_blocked_today'],
                          float (data['ads_percentage_today']),
                          data['dns_queries_today'],
                          data['domains_being_blocked']
                         )

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "VALUE",
    "consumer_secret"     : "VALUE",
    "access_token"        : "VALUE",
    "access_token_secret" : "VALUE" 
    }

  api = get_api(cfg)
  tweet = datetime.datetime.today().strftime("%Y-%m-%d") + " Daily Pi-Hole report\n " + data
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
