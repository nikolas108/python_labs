import requests
from bs4 import BeautifulSoup as bs
import os
import csv
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

def get_data_modif(html,model_name):
	soup = bs(html, 'lxml')
	try:
		modifs = soup.find('table', class_='catalog-table').find_all('tr')
	except:
		print('no modifs catalog for model: ', model_name)
		return []
	else:
		return modifs

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

def create_dir_mark_test(path,name):
	file_path = path + name 
	# directory = os.path.dirname(file_path)
	print('try to create dir')
	print(file_path)
	return file_path


def save_img_mark(url,path,name):
	file = path + '/' + name + '.png'
	print(file)
	try:
		r =requests.get(url,timeout=1)
		if r.status_code == 200:
			with open(file,'wb') as f:
				f.write(r.content)
	except:
		print(file + ' !!!!!!!!!!!!!!!!!not downloaded\nNext-----------------')
		write_error(file + ' !!!!!!!!!!!!!!!!!not downloaded\nNext-----------------' + url )
		# continue

def save_img_model(url,path,name):
	file = path + '/' + name + '.jpg'
	print(file)
	try:
		r =requests.get(url,timeout=3)
		if r.status_code == 200:
			with open(file,'wb') as f:
				f.write(r.content)
	except:
		print(file + ' !!!!!!!!!!!!!!!!!not downloaded\nNext-----------------')
		write_error(file + ' !!!!!!!!!!!!!!!!!not downloaded\nNext-----------------' + url )

def write_csv2(data,model_name):
	with open(model_name,'a') as file:
		order = ['model_modif' , 'period' , 'engine' , 'engine_model','fuel', 'power' , 'drive_type']
		writer = csv.DictWriter(file, fieldnames=order)
		writer.writerow(data)	

def write_csv(data,model_name):
    with open('models.csv' ,'a') as f:
        writer = csv.writer(f)
        writer.writerow([model_modif['model_modif'], model_modif['period'], model_modif['engine'], model_modif['engine_model'], model_modif['fuel'], model_modif['power'],model_modif['drive_type']])

def write_error(data):
    with open('error.log' ,'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def main():
	# mark_name
	# model_name
	page_url = 'https://mtcar.ru/catalog/to.html'
	root = 'https://mtcar.ru'
	path = './root/'
	body = get_data_mark(get_html(page_url))
	count=0
	for mark in body:
		# count += 1
		url_model = mark.find('a').get('href')			#   HTML MODEL
		mark_name = mark.find('div', class_='col-xs-12').text.strip()		#   MARK  NAME
		url_img_mark = mark.find('div', class_='text-center').get('style').split('\'')[1]    #  URL  IMG   MARK
		print(mark_name)
		print(url_model)
		path_mark = create_dir_mark(path,mark_name)  #  TEST
		# print(path_model)
		print(url_img_mark)
		save_img_mark(url_img_mark,path_mark,mark_name)  # TEST
		# загружены все марки и картинки 
		# переходим к моделям
		models_li_list = get_data_model(get_html(url_model))
		# if count > 5:
			# break
		for model in models_li_list:
			url_modif = root + model.find('a').get('href')  		#  HTML   MODIF
			model_name = model.find('div',class_='car-base-list-name').text.strip().replace('/', ' and ')		#  MODEL NAME
			url_img_model = model.find('div', class_='car-base-list-image-dis').get('style').split('\'')[1]		# URL IMG MODEL
			print(model_name)
			print(url_modif)
			print(url_img_model)
			path_model = create_dir_mark(path_mark + '/',model_name)  # path_mark + '\\' + model_name   # test
			save_img_model(url_img_model,path_model,model_name)   # test
			print(mark_name,model_name)
			modifs = get_data_modif(get_html(url_modif),model_name)
			if len(modifs) == 0: continue;write_error(model_name + ' no modification')
			for modif in modifs:
				count += 1
				tds = modif.find_all('td')
				# try:
				if len(tds) == 0: continue
				model_modif = {'model_modif' : tds[0].text.strip() , 
					'period' : tds[1].text, 'engine' : tds[2].text,
					 'engine_model' : tds[3].text,'fuel' : tds[4].text, 
					 'power' : tds[5].text, 'drive_type' : tds[6].text }
				# except:	
					# print('no modification for!!!!!!!! : ' , model_name,)
				# else:
				print('Модификация модели: ', model_modif['model_modif'],' период выпуска: ', model_modif['period'], ' двигатель : ', model_modif['engine'],
					' модель двигателя: ', model_modif['engine_model'], ' топливо: ', model_modif['fuel'], ' мощность: ', model_modif['power'], ' тип привода: ',
					model_modif['drive_type'])
				print(count , model_name + '.csv'	)
				write_csv2(model_modif,path_model + '/' + model_name + '.csv')

if __name__ == '__main__':
	main()




