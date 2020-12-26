import alpaca_trade_api as tradeapi
from alpaca_trade_api.common import URL

api = tradeapi.REST('PKVNZDANZST7PX694RTM', 'UJ2xz01YwtLlRbBBrNaN0jnqlb6gVBXDVBiNBPhh', base_url=URL("https://paper-api.alpaca.markets"))

counter = 0
while True:
    try:
        api.submit_order('NVDA', 1, 'buy', 'market', 'day')
        counter = counter + 1
        print(counter, 'purchases processed')
    except:
        print('lmao error')