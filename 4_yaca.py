import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
	r = requests.get(url)
	if r.ok:  # 200  ### 403 404
		return r.text
	print(r.status_code)

def write_csv(data):
	with open('yaca.csv','a') as f:
 		writer = csv.writer(f)
 		pass

 def get_page_data(html):
 	soup = BeautifulSoup(html,'lxml')


		





def main():
	url = 'https://yandex.ru/yaca/cat/Entertainment/'
	
	get_page_data(get_html(url))

if __name__ == '__main__':
	main()