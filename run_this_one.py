import alpaca_trade_api as tradeapi
from alpaca_trade_api.common import URL

api = tradeapi.REST('PKCQ9FP8ICADEN6GXVMV', 'FcDJHcD5lgvYUySh7tSC4TZkwdl9NpLPMhfp6E15', base_url=URL("https://paper-api.alpaca.markets"))

counter = 0
while True:
    try:
        api.submit_order('NVDA', 1, 'buy', 'market', 'day')
        counter = counter + 1
        print(counter, 'purchases processed')
    except:
        print('lmao error')
