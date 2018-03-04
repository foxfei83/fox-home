from bitshares import BitShares
from bitshares.blockchain import Blockchain
from bitshares.market import Market
from bitshares.account import Account
from bitshares.wallet import Wallet 
import time
from uc_config import logger

#testnet = BitShares(
#    "wss://node.testnet.bitshares.eu",
#    nobroadcast=True,
#    bundle=True,
#)

# return param1:5min avg price param2:last price
def update_market(market):
    global is_init_stat
    global last_m_point
    global last_ts
    global last_market_snapshot
    global _m_avg_price
    global last_price

    try:
        data = market.ticker()
        # print("market ticker:", data)
        _24h_avg_price = data["quoteVolume"] / data["baseVolume"]
        print("24h avg price:", _24h_avg_price, "latest price:", data["latest"], "change:", data["percentChange"])
        return [_24h_avg_price, data["latest"]]
    except Exception as e:
        logger.error("on except:%s", e)
        return [0, 0]
        # log_bt()


    now = time.time()
    _m_point = now // 1800 

    if not "is_init_stat" in globals():
        last_m_point = _m_point
        last_ts = now
        last_market_snapshot = market.ticker()
        is_init_stat = True
        print("inited")
        return [0,0]

    print("mp:", _m_point, "lmp:", last_m_point)
    if _m_point > last_m_point:
        # time_diff = now - last_ts
        # last_ts = now
        last_m_point = _m_point
        data = market.ticker()
        base_volume_diff = data["baseVolume"] - last_market_snapshot["baseVolume"]
        quote_volume_diff = data["quoteVolume"] - last_market_snapshot["quoteVolume"]
        _m_avg_price = quote_volume_diff / base_volume_diff
        print("basev:", data["baseVolume"])
        print("quotev:", data["quoteVolume"])
        last_market_snapshot = data
        last_price = data["latest"]

    if "_m_avg_price" in globals():
        return [_m_avg_price, last_price]
    return [0,0]

# usd_cny_market = Market("USD:CNY")
# while True:
#    data = update_market(usd_cny_market)
#    time.sleep(1)
#    print("min avg price:", data, "now:", time.time())

