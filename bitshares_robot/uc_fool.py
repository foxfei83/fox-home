from bitshares import BitShares
from bitshares.blockchain import Blockchain
from bitshares.market import Market
from bitshares.account import Account
from bitshares.wallet import Wallet
import time
import sys
from mean_reversion import update_market
sys.path.append('/home/foxfei')
from secret import get_bitshare_private_key
from secret import get_bitshare_pwd
from uc_config import logger

def init():
    #try:
        auto_trans()
    #except:
    #    print("goto except handle")
    #    auto_trans()

def auto_trans():
    bitshares = BitShares()
    pwd = get_bitshare_pwd()
    private_key = get_bitshare_private_key()
    # create usd:cny market obj 
    usd_cny_market = Market("USD:CNY")
    # create fox wallet obj
    fox_wallet = Wallet()
    if not fox_wallet.created():
        fox_wallet.newWallet(pwd)
    # add private key, TODO:keep private key and pwd in safe place 
    usd_cny_market.bitshares.wallet.unlock(pwd)
    try:
        usd_cny_market.bitshares.wallet.addPrivateKey(private_key)
    except ValueError as ve:
        logger.info('wif is already set')

    logger.info('start auto trans usd:cny')
    lb = 6.40
    ub = 6.50
    fox = Account("zfpx-fdjl")
    while True:
        logger.info("my balance:%s", fox.balances)
        logger.info("my open orders:%s", fox.openorders)
        my_usd = fox.balance("USD")
        my_cny = fox.balance("CNY")
        logger.info("my USD:%s my CNY:%s", my_usd, my_cny)

        # get avg price
        avg_price = update_market(usd_cny_market)[0]
        if avg_price < 6 or avg_price > 7:
            logger.error("!!!!!!!!!!!!!!!!!!!!!!!!:avg price out of range:", avg_price)
            continue

        # set upper bound and lower bound
        lb = avg_price * (1-0.005)
        ub = avg_price * (1+0.005)

        # get top orders
        top_orders = usd_cny_market.orderbook();
        # unlock fox wallet for usd:cny maket
        usd_cny_market.bitshares.wallet.unlock(pwd)
        # cancel all of the orders
        orders = usd_cny_market.accountopenorders(fox)
        for order in orders:
            logger.info("try cancel %s : %s", order["id"], order)
            usd_cny_market.cancel(order["id"], fox)
            time.sleep(1)

        # sell all  
        for bid in top_orders["bids"]:
            price = bid["price"]
            quote = bid["quote"]
            if price >= ub and my_usd > 0:
                # sell_usd = min(my_usd, quote)
                if my_usd["amount"] < quote["amount"]:
                    sell_usd = my_usd
                else:
                    sell_usd = quote
                left_usd = my_usd["amount"] - sell_usd["amount"]
                logger.info("sell_usd:%s left_usd:%s price:%s", sell_usd, left_usd, price)
                try:
                    usd_cny_market.sell(price, sell_usd, 10, True, fox)
                except Exception as e:
                    logger.error("on except:%s", e)
                my_usd["amount"] = left_usd
            # else:
            #    print("price:", price, " < ub:", ub)

        # buy all
        for ask in top_orders["asks"]:
            price = ask["price"]
            base = ask["base"]
            if price <= lb and my_cny > 0:
                left_cny = my_cny["amount"] - base["amount"]
                if base["amount"] < my_cny["amount"]:
                    buy_cny = base["amount"]
                else:
                    buy_cny = my_cny["amount"]
                    buy_usd = buy_cny / price
                    left_cny = my_cny["amount"] - buy_cny
                    logger.info("buy_usd:%s left_cny:%s price:%s", buy_usd, left_cny, price)
                    try:
                        usd_cny_market.buy(price, buy_usd, 10, True, fox)
                    except Exception as e:
                        logger.error("on except:%s", e)
                    my_cny["amount"] = left_cny
            # else:
            #    print("price:", price, " > ub:", lb)

        usd_cny_market.bitshares.wallet.lock()
        time.sleep(10)

init()
