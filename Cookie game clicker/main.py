import time
from pricemanager import PriceManager

clicker = PriceManager()

def run():
    start = time.time()
    on = True
    while on:
        now = time.time()
        clicker.click()
        if now > start+5:
            on = False
    if on == False:
        clicker.checkupdate()
        run()


run()
