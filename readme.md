# Twitter Liker

1. Create a file accesskeys.py with the following structure

The API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_SECRET can be accessed from https://developer.twitter.com/en/apps

```
API_KEY = ''
API_KEY_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
```

2. Change example.py line 11 with your hashtag

3. Run docker command 
```
docker build -t myusername/twitterliker .; docker run --rm -it --network host --name twitterliker myusername/twitterliker
```
