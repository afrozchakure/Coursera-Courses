import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})  # It includes login information of URL
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    # urllib eats the headers, there we use ".getheaders()" to get the headers
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])  # It prints how many more requests twitter is going to allow before they shut you down

    js = json.loads(data)  # Dumps the file in a json format
    print(json.dumps(js, indent=4)) # Prints the file with indent = 4

    for u in js['users']:  # js is an array, so we look through each element of array
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])
