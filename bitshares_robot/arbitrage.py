# [100,101]
# [100,101]
from time import time

def is_expire(t1,t2):
    if abs(t1 - t2) > 10: return True
    return False

global orders
# TB is short for top_buy 
# BS is short for button_sell
# unit: ETH
"""
orders = {
    'binace' : {
            'EOS' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'BTC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'ETC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        }
    },
    'bitshares' : {
            'EOS' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'BTC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'ETC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        }
    },
    'okex' : { 
            'EOS' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'BTC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'ETC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        }
    },
    'huobi' : {
            'EOS' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'BTC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        },
            'ETC' : {
            'TB_price'  : 0.01     ,
            'TB_amount' : 100      ,
            'BS_price'  : 0.02     ,
            'BS_amount' : 101      ,
        }
    }
}
"""

# t for time
# m for market
# o for order
def up_best_order(m, o, t=0):
    if t == 0: 
        now = time()
    

exchange_route = ['BTC', 'ETH', 'BIS']

class currency
    amount
    def exchange_with(other):
         
