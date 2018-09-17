# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	r.encoding = 'utf-8 '
	return r.text

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	h1 = soup.find('div',class_='wrapper_body').find('div',class_='cbm_wrap').find('h1')
	return h1

def main():
	url = 'http://www.autospar.ru/carbase'
	print(get_data(get_html(url)))
	print("Твой возраст в секундах:")






if __name__ == '__main__':
	main()