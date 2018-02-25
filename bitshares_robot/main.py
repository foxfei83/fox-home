from bitshares import BitShares
from bitshares.blockchain import Blockchain
from bitshares.market import Market

testnet = BitShares(
    "wss://node.testnet.bitshares.eu",
    nobroadcast=True,
    bundle=True,
)

bitshares = BitShares()
#print(bitshares.config.items())

chain = Blockchain()

mid_rate = 6.31
lower_bound_rate = mid_rate * 1.008
upper_bound_rate = lower_bound_rate * 1.035
print(lower_bound_rate, "|", upper_bound_rate)

lb = 6.40
ub = 6.50
usd_cny_market = Market("USD:CNY")
top_orders = usd_cny_market.orderbook(10);

# sell to bid
for bid in top_orders["bids"]:
	print("bid:", "base:", bid["base"], "quote:", bid["quote"], "price:", bid["price"])

# buy from ask
for ask in top_orders["asks"]:
	print("ask:", "base:", ask["base"], "quote:", ask["quote"], "price:", ask["price"])

#print(market.orderbook(2))
#print(usd_cny_market.ticker())

