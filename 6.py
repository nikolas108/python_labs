from bs4 import BeautifulSoup
import re
# .find
# .find_all
# .parent
# .find_parent
# .parents
# .find_parents

# .find_next_sibling()
# .find_previous_sibling()

# -----------REGEX-----------
# pattern = r'\d{1,4}'
# re.search(pattern,string).group()
# ^ - начало строки
# $ - конец строки
# . - любой символ
# +  - неограниченное количество вхождений
# \d - digit
# \w - буквы цифры и _


def get_copywriter(tag):
	whois = tag.find('div',id='whois').text.strip()
	if 'Copywriter' in whois:
		return tag
	return None


copywriters = []

def get_salary(s):
	pattern = r'\d{1,9}'
	salary = re.search(pattern,s).group()
	return salary

def main():
	file = open('index.html').read()
	soup = BeautifulSoup(file,'lxml')
	# salary = soup.find_all('div',{'data-set':'salary'})
	salary = soup.find_all('div',text=re.compile('\d{1,9}'))
	for i in salary:
		# print(get_salary(i.text.strip()))
		print(get_salary(i.text))

	# persons = soup.find_all('div',class_='row')
	
	# for person in persons:
	# 	cw = get_copywriter(person)
	# 	if cw:
	# 		copywriters.append(cw)
	# print(copywriters)
	# # row = soup.find('div',{'data-set':'salary'})
	# print(row)
	# alena = soup.find('div',text='Alena').find_parent(class_='row')

	# print(alena)





if __name__ == '__main__':
	main()