import requests
from bs4 import BeautifulSoup as bs
import os
# from StringIO import StringIO
# from PIL import Image

def get_html(url):
	r = requests.get(url)
	return r.text

def get_data_mark(html):
	soup = bs(html,'lxml')
	body = soup.find_all('div',class_='col-xs-6')
	return body

def get_data_model(html):
	soup = bs(html,'lxml')
	models = soup.find('ul', class_='td-model').find_all('li')
	return models

def create_dir_mark(path,name):
	file_path = path + name 
	# directory = os.path.dirname(file_path)
	print('try to create dir')
	if not os.path.exists(file_path):
		os.makedirs(file_path)
		print('dir created')
	else:
		print('can\'t create dir')
		print(file_path)
	return file_path

def save_mark_img(url,path,name):
	file = path + '\\' + name + '.png'
	print(file)
	try:
		r =requests.get(url,timeout=1)
		if r.status_code == 200:
			with open(file,'wb') as f:
				f.write(r.content)
	except:
		print(file + ' !!!!!!!!!!!!!!!!!not downloaded\nNext-----------------')
		# continue



def main():
	page_url = 'https://mtcar.ru/catalog/to.html'
	root = 'https://mtcar.ru'
	path = 'd:\img\\'
	body = get_data_mark(get_html(page_url))
	count=0
	for mark in body:
		url_model = mark.find('a').get('href')
		name_mark = mark.find('div', class_='col-xs-12').text.strip()
		url_img_mark = mark.find('div', class_='text-center').get('style').split('\'')[1]
		# print(name_mark)
		# print(url_model)
		path_mark = create_dir_mark(path,name_mark)
		# print(path_model)
		# print(url_img_mark)
		save_mark_img(url_img_mark,path_mark,name_mark)
		# загружены все марки и картинки 
		# переходим к моделям
		models_li_list = get_data_model(get_html(url_model))
		for model in models_li_list:
			url_modif = root + model.find('a').get('href')
			model_name = model.find('div',class_='car-base-list-name').text.strip().replace('/', ' and ')
			url_img_model = model.find('div', class_='car-base-list-image-dis').get('style').split('\'')[1]
			print(model_name)
			print(url_modif)
			print(url_img_model)
			path_model = create_dir_mark(path_mark + '\\',model_name)  # path_mark + '\\' + model_name
			save_mark_img(url_img_model,path_model,model_name)








if __name__ == '__main__':
	main()




