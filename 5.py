import csv



def write_csv(data):
	with open('name.csv','a') as file:
		writer = csv.writer(file)
		writer.writerow((data['name'],data['surname'],data['age']))

def write_csv2(data):
	with open('names.csv','a') as file:
		order = ['name','surname','age']
		writer = csv.DictWriter(file, fieldnames=order)
		writer.writerow(data)

# def read_csv()

def main():
	d = {'name': 'Petr','surname':'Ivanov','age': 21}
	d1 = {'name': 'Ivan','surname':'Ivanov','age': 18}
	d2 = {'name': 'Ksu','surname':'Petrova','age': 32}
	l = [d,d1,d2]
	fieldnames = ['name','url','price']
	with open('temp.csv') as file:
		reader = csv.DictReader(file, fieldnames=fieldnames)
		ind = 0
		for row in reader:
			ind += 1
			print(type(row))
			print(dir(row))
			print( row.get )



	# for i in l:
	# 	print(i)
	# 	write_csv2(i)

if __name__ == '__main__':
	main()