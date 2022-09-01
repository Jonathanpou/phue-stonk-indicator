import cryptocompare
import time

coin = "LUNC"

def get_price(coin):
    price = cryptocompare.get_price(coin, 'USD')
    return price

while True:
    print(get_price(coin))
    time.sleep(5)