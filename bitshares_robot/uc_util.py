import math 

# pr:100% price:0.5
# pr:30% price:0.8
# pr:20% price:1.0
# pr:13% price:1.25
# pr:6%  price:1.5
# pr:1.5%  price:2.0
# pr:0.5%  price:2.5
# pr:-0.5%  price:3.0
# pr:-2.0%  price:4.0
def predict_bitCNY_CNY_pr(bitshares_price)
    if bitshares_price  < 0.5:
        raise Exception("bitshare is crash!")
    elif bitshares_price  >= 0.5 and bitshares_price < 0.8:
        return (1.0 + 0.3) 
    elif bitshares_price  >= 0.8 and bitshares_price < 1.0:
    elif bitshares_price  >= 1.0 and bitshares_price < 1.25:
    elif bitshares_price  >= 1.25 and bitshares_price < 1.5:
    elif bitshares_price  >= 1.5 and bitshares_price < 2.0:
    elif bitshares_price  >= 2.0 and bitshares_price < 2.5:
    elif bitshares_price  >= 3.0 and bitshares_price < 4.0:
    else:
    

# pr is short for premium rate
# dr is short for discount rate
# er is short for exchange rate

# CNY price for USD
USD_CNY_er
# bitCNY price for bitUSD
bitUSD_bitCNY_er_expectation
# bitUSD to bitCNY vs USD to CNY premium rate
bitUSD_bitCNY_pr = 0.1
# CNY price for bitCNY premium rate
bitCNY_CNY_pr = predict_bitCNY_CNY_pr()
# calc expectation exchange rate
bitUSD_bitCNY_er_expectation = USD_CNY_er*(1+bitUSD_bitCNY_pr)*(1-bitCNY_CNY_pr)


# bitUSD price with bitCNY
bitCNY_price
