from keywords import companies, social_media_giants, partnership_keywords, exchange_keywords


# users
brothaakhee = '211924001'
mcafee = '961445378'
data_dash = '892429154121068544'
vitalik = '295218901'
charlie_lee = '14338147'
cryptogrinders = '909505279275843584'


# coins
neo = '2592325530'
burst = '2937820937'
stellar_lumens = '2460502890'
request_network = '888343534083944448'
cardano = '825920479055671296'
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
hitbtc = '1364642054'


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
        'any': ['casper', 'raiden'] + partnership_keywords,
    },

    charlie_lee: {
        'all': [],
        'any': ['lightning', 'atomic'] + partnership_keywords,
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

    hitbtc: {
        'all': [],
        'any': exchange_keywords,
    },
}
