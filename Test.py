from yahoo_fin import stock_info as si
import time


stock = "PLUG"



while True:
        #get price og the stock in real time
	price = si.get_live_price(stock)
	#reducing the decimals from like a 100 to max 3
	redu = str(round(price, 3))
	state = None
        #printing the formated stock price 
	print(stock + ": {} ".format(redu))
	time.sleep(5)
