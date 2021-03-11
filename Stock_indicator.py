from phue import Bridge
from yahoo_fin import stock_info as si
import time

b = Bridge('192.168.8.110') # Bridge IP

b.connect()

red = [0.7350000508904126, 0.24174193816705097]
green = [0.11500021676131911, 0.8155333283841992]


def set_light(color):
        b.set_light(6, 'bri', 254)
        b.set_light(6, 'xy', color)


last_price = 0
last_state = None

while True:
	price = si.get_live_price("XELA")
	redu = str(round(price, 3))
	state = None

	print("XELA: {} ".format(redu))

	if price >= last_price:
		state = True
		set_light(green)
	else:
		state = False
		set_light(red)


	last_price = price
	last_state = state
