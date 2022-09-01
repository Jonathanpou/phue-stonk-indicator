from phue import Bridge
#from yahoo_fin import stock_info as si
import time
import cryptocompare

b = Bridge('192.168.8.110') # Bridge IP

b.connect()

red = [0.7350000508904126, 0.24174193816705097]
green = [0.11500021676131911, 0.8155333283841992]


def set_light(color):
        b.set_light(4, 'bri', 254)
        b.set_light(4, 'xy', color)

stock = "NEL.OL"

coin = "LUNC"


last_price = 0
last_state = None

while True:
        #get price og the stock in real time
	price = si.get_live_price(coin)
	#reducing the decimals from like a 100 to max 3
	redu = str(round(price, 3))
	state = None
        #printing the formated stock price 
	print(coin + ": {} ".format(redu))
	#waits 10 sec before printing the next price not to strees the connection to Yahoo Finance
	time.sleep(10)

	
#Light controller
	if price >= last_price:
		state = True
		set_light(green)
	else:
		state = False
		set_light(red)


	last_price = price
	last_state = state
