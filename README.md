# twitter-alerts
Scan tweets for keywords and alert

Uses Python3.6

Create a virtual environment

`virtualenv -p /path/to/python3 .env`

Install requirements

`pip install -r requirements.txt`

Use `python3 consumer.py` to start streaming listener, or use supervisor to keep the process running.
You will have to set up environment variables with your twitter and aws credentials.

```
TWITTER_CONSUMER_KEY=''
TWITTER_CONSUMER_SECRET=''
TWITTER_ACCESS_TOKEN=''
TWITTER_ACCESS_TOKEN_SECRET=''

AWS_APP_KEY=''
AWS_APP_SECRET=''
AWS_TOPIC_ARN=''
```

Each account you want to follow should be added to `consumer.py` through its ID. The ID should be a string.
Use an online tool to look up a twitter handle's ID, and then map that to a variable with the name of the handle.

`brothaakhee = '123456'`

That variable should then be mapped to the keywords you want to alert on through a dict.

```
{
    brothaakhee: {
        'all': ['keywords', 'that', 'should', 'all', 'be', 'present'],
        'any': ['keywords', 'that', 'will alert', 'even if', 'one is present']
    }
}
```
