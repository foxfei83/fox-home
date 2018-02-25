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

#testnet = BitShares(
#    "wss://node.testnet.bitshares.eu",
#    nobroadcast=True,
#    bundle=True,
#)

#chain = Blockchain()

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
        print("wif is already set")

    print("start auto trans usd:cny")
    lb = 6.40
    ub = 6.50
    fox = Account("zfpx-fdjl")
    while True:
        print(fox.balances)
        print(fox.openorders)
        my_usd = fox.balance("USD")
        my_cny = fox.balance("CNY")
        print("my USD:", my_usd, "my cny:", my_cny)
        # print(usd_cny_market.ticker())
        # get avg price 
        avg_price = update_market(usd_cny_market)[0]
        if avg_price < 6 or avg_price > 7:
            print("!!!!!!!!!!!!!!!!!!!!!!!!:avg price out of range:", avg_price)
            continue
        # set upper bound and lower bound
        # data = usd_cny_market.ticker()
        # change = data["percentChange"]

        lb = avg_price * (1-0.005)
        ub = avg_price * (1+0.005)

        # get top orders
        top_orders = usd_cny_market.orderbook();
        # print("top orders:", top_orders)
        # unlock fox wallet for usd:cny maket
        usd_cny_market.bitshares.wallet.unlock(pwd)
        # cancel all of the orders
        orders = usd_cny_market.accountopenorders(fox)
        for order in orders:
            print("try cancel ", order["id"], " :", order)
            usd_cny_market.cancel(order["id"], fox)
            time.sleep(1)

        # sell all  
        for bid in top_orders["bids"]:
            price = bid["price"]
            quote = bid["quote"]
            # print("bid:", price, "ub:", ub, "myusd:", my_usd)
            if price >= ub and my_usd > 0:
                # sell_usd = min(my_usd, quote)
                if my_usd["amount"] < quote["amount"]:
                    sell_usd = my_usd
                else:
                    sell_usd = quote
                left_usd = my_usd["amount"] - sell_usd["amount"]
                print("sell_usd:", sell_usd, "left_usd:", left_usd, "price:", price)
                try:
                    usd_cny_market.sell(price, sell_usd, 10, True, fox)
                except Exception as e:
                    print("on except:", e)
                my_usd["amount"] = left_usd
            # else:
            #    print("price:", price, " < ub:", ub)

        # buy all
        for ask in top_orders["asks"]:
            price = ask["price"]
            base = ask["base"]
            # quote = ask["quote"]
            # print("base asset:", base["asset"])
            # print("my cny asset:", my_cny["asset"])
            # print("ask:", price, "lb:", lb, "myusd:", my_cny)
            if price <= lb and my_cny > 0:
            # if change <= -0.3 and my_cny > 0:
                # buy_cny = min(base, my_cny)
                left_cny = my_cny["amount"] - base["amount"]
                if base["amount"] < my_cny["amount"]:
                    buy_cny = base["amount"]
                else:
                    buy_cny = my_cny["amount"]
                    buy_usd = buy_cny / price
                    left_cny = my_cny["amount"] - buy_cny
                    print("buy_usd:", buy_usd, "left_cny:", left_cny, "price:", price)
                    try:
                        usd_cny_market.buy(price, buy_usd, 10, True, fox)
                    except Exception as e:
                        print("on except:", e)
                    my_cny["amount"] = left_cny
            # else:
            #    print("price:", price, " > ub:", lb)

        usd_cny_market.bitshares.wallet.lock()
        time.sleep(10)

init()
