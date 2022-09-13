import cryptocompare, time, os

while True:
    os.system('clear')
    priceBTC = cryptocompare.get_price('BTC', 'USD')
    priceETH = cryptocompare.get_price('ETH', 'USD')
    priceADA = cryptocompare.get_price('ADA', 'USD')
    priceSOL = cryptocompare.get_price('SOL', 'USD')
    priceDOT = cryptocompare.get_price('DOT', 'USD')
    
    prices = priceBTC, priceETH, priceADA, priceSOL, priceDOT
    
    for price in prices:
        print(price)
    
    time.sleep(5)