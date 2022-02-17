import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
def data_return(acct):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # print('')
    # acct = input('Enter Twitter Account:')
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct})
    # print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    # print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    # print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        # print(u['screen_name'])
        if 'status' not in u:
            # print('   * No status found')
            continue
        s = u['status']['text']
        # print('  ', s[:50])
    return js

with open("twitter2.json", "w") as file:
    json.dump(data_return("CyberMavka"), file, indent = 4)