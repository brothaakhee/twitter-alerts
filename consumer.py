import os
import json
import boto3

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

from keywords import companies, social_media_giants, partnership_keywords, exchange_keywords


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

# users
brothaakhee = '211924001'
mcafee = '961445378'
data_dash = '892429154121068544'
vitalik = '295218901'
charlie_lee = '14338147'

# coins
neo = '2592325530'
burst = '2937820937'
stellar_lumens = '2460502890'
request_network = '888343534083944448'
cardano = '825920479055671296'
cryptogrinders = '909505279275843584'
ethos = '862007728956485632'
substratum = '888794609509433347'
waves = '707515829798182912'
quantstamp = '06057790707216384'
trustwallet = '911011433147654144'
kybernetwork = '865963965649571840'
pivx = '4020178512'
navcoin = '2532881881'
lisk = '4736263474'
ethereum = '2312333412'
stratis = '734688391942524928'
dash = '2338506822'
monero = '2478439963'
quantum = '773009781644677120'
civic = '4711101020'
tenx = '4585412124'
omisego = '831847934534746114'

# exchanges
coinbase = '574032254'
gdax = '720487892670410753'
poloniex = '2288889440'
binance = '877807935493033984'
bittrex = '2309637680'

global_any_terms = []
global_all_terms = []

KEYWORDS_MAP = {
    # users
    brothaakhee: {
        'all': ['testing', 'blahblah'],
        'any': ['wildcard', 'fake'],
    },

    mcafee: {
        'all': ['coin', 'day'],
        'any': [],
    },

    data_dash: {
        'all': [],
        'any': ['interview', 'review'],
    },

    cryptogrinders: {
        'all': [],
        'any': ['interview', 'review'],
    },

    vitalik: {
        'all': [],
        'any': ['casper', 'raiden'],
    },

    charlie_lee: {
        'all': [],
        'any': ['lightning', 'atomic'],
    },

    # coins
    neo: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    burst: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    stellar_lumens: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    request_network: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    cardano: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    ethos: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    substratum: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    waves: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    quantstamp: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    trustwallet: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    kybernetwork: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    pivx: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    navcoin: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    lisk: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    ethereum: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    stratis: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    dash: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    monero: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    quantum: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    civic: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    tenx: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    omisego: {
        'all': [],
        'any': partnership_keywords + companies + social_media_giants,
    },

    # exchanges
    coinbase: {
        'all': [],
        'any': exchange_keywords,
    },

    gdax: {
        'all': [],
        'any': exchange_keywords,
    },

    poloniex: {
        'all': [],
        'any': exchange_keywords,
    },

    binance: {
        'all': [],
        'any': exchange_keywords,
    },

    bittrex: {
        'all': [],
        'any': exchange_keywords,
    },
}


class TweetListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print('incoming data')
        try:
            list_data = json.loads(data)
            print(list_data)
            username = list_data['user']['screen_name']
            user_id = list_data['user']['id_str']
            tweet = list_data['text'].lower()
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
