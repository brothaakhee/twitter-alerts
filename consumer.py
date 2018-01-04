import os
import json
import boto3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

from accounts import KEYWORDS_MAP


twitter_credentials = {
    'consumer_key': os.getenv('TWITTER_CONSUMER_KEY'),
    'consumer_secret': os.getenv('TWITTER_CONSUMER_SECRET'),
    'access_token': os.getenv('TWITTER_ACCESS_TOKEN'),
    'access_token_secret': os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
}


aws_creds = {
    'key': os.getenv('AWS_APP_KEY'),
    'secret': os.getenv('AWS_APP_SECRET'),
    'topic_arn': os.getenv('AWS_TOPIC_ARN')
}


class TweetListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print('incoming data')
        try:
            list_data = json.loads(data)
            username = list_data['user']['screen_name']
            user_id = list_data['user']['id_str']
            tweet = list_data['text'].lower()
            print(username)
            print(tweet)
            tweet_url = 'https://twitter.com/{}/status/{}'.format(
                username,
                list_data['id_str']
            )

        except:
            print(list_data)
            print('Something went wrong with that tweet.')
            return

        user_keywords = KEYWORDS_MAP.get(user_id)

        if not user_keywords:
            print('dont have user for user id: ')
            print(user_id)
            return

        if (user_keywords['any'] and any(keyword.lower() in tweet for keyword in user_keywords['any'])) or \
                (user_keywords['all'] and all(keyword.lower() in tweet for keyword in user_keywords['all'])):
            client = boto3.client(
                "sns",
                aws_access_key_id=aws_creds['key'],
                aws_secret_access_key=aws_creds['secret'],
                region_name='us-east-1'
            )
            print('tweet matched keyword')
            msg = '{} tweeted: {} ---- {}'.format(
                username,
                tweet,
                tweet_url,
            )
            print('sending to sns to send text')
            client.publish(Message=msg, TopicArn=aws_creds['topic_arn'])

    def on_error(self, status):
        print('error: ')
        print(status)


if __name__ == '__main__':
    print(twitter_credentials)
    auth = OAuthHandler(
        twitter_credentials['consumer_key'],
        twitter_credentials['consumer_secret']
    )
    auth.set_access_token(
        twitter_credentials['access_token'],
        twitter_credentials['access_token_secret'],
    )

    listener = TweetListener()

    stream = Stream(auth=auth, listener=listener)
    print('authenticated')
    stream.filter(follow=KEYWORDS_MAP.keys())
