import os, time, requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://coinmarketcap.com')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

coinboard = soup.find('table', { 'class': 'h7vnx2-2 czTsgW cmc-table' })
tbody = coinboard.find('tbody')
tr = tbody.find_all('tr')

BTC = 'Bitcoin1'
ETH = 'Ethereum2'
ADA = 'Cardano'
SOL = 'Solana'
DOT = 'Polkadot'

def get_data():
	for tr in tbody:
		name = tr.find_all('td')[2].text.strip()
		price = tr.find_all('td')[3].text.strip()
		if BTC in name:
			print('BTC: ', price)
		if ETH in name:
			print('ETH: ', price)
		if ADA in name:
			print('ADA: ', price)
		if SOL in name:
			print('SOL: ', price)
		if DOT in name:
			print('DOT: ', price)
	
	time.sleep(5)

while True:
    os.system('clear')
    get_data()