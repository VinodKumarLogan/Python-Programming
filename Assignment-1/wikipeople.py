import argparse,random,string

def id_generator(size=4, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for x in range(size))

def readFile(filename,database):
	f = open(filename,'r')
	for data in f:
		database.append(data.split("\n")[0].split(" "))
	return database

def gen_rand_data(datarange,database):
	i = 0
	while i<datarange:
		database.append([str(id_generator()),random.randrange(1990,2013),str(id_generator()),str(id_generator()),str(id_generator(1,"fm"))])
		i = i + 1
	return database

class queryParser:

	def parse_display(self,display):
		toBeDisplayed = []
		if display=="all":
			toBeDisplayed = ["Name","Year","Category","Achievement","Gender"]
		else:
			for val in display.split("\n")[0].split(","):
				val = val.lower()
				if val=="name":
					toBeDisplayed.append("Name")
				elif val=="year":
					toBeDisplayed.append("Year")
				elif val=="achievement":
					toBeDisplayed.append("Achievement")
				elif val=="category":
					toBeDisplayed.append("Category")
				elif val=="gender":
					toBeDisplayed.append("Gender")
		return toBeDisplayed

	def parse_name(self,name,result):
		name = name.strip().replace(" ","")
		name_not_in = []
		name_in = []
		if name[:2] == "!=":
			name_not_in = [x for x in name[2:].split(",")]
			result = [val for val in result if val[0] not in name_not_in]
		elif name[:1] == "=":
			name_in = [x for x in name[1:].split(",")]
			result = [val for val in result if val[0] in name_in]
		return result

	def parse_year(self,year,result):
		year = year.strip().replace(" ","")
		if year[:2] == "!=":
			year_not_in = [x for x in year[2:].split(",")]
			result = [val for val in result if val[1] not in year_not_in]
		elif year[:1] == "=":
			year_in = [x for x in year[1:].split(",")]
			result = [val for val in result if val[1] in year_in]
		elif year[:2] == '>=':
			y = int(year[2:])
			result = [val for val in result if int(val[1])>=y]
		elif year[:2] == '<=':
			y = int(year[2:])
			result = [val for val in result if int(val[1])<=y]
		elif year[:1] == '>':
			y = int(year[1:])
			result = [val for val in result if int(val[1])>y]
		elif year[:1] == '<':
			y = int(year[1:])
			result = [val for val in result if int(val[1])<y]
		return result

	def parse_gender(self,gender,result):
		gender = gender.strip().replace(" ","")
		if gender[:2] == "!=":
			gender_not_in = gender[2:]
			result = [val for val in result if val[4]!=gender_not_in]
		elif gender[:1] == "=":
			gender_in = gender[1:]
			result = [val for val in result if val[4]==gender_in]
		return result

	def parse_category(self,category,result):
		category = category.strip().replace(" ","")
		category_not_in = []
		category_in = []
		if category[:2] == "!=":
			category_not_in = [x for x in category[2:].split(",")]
			result = [val for val in result if val[2] not in category_not_in]
		elif category[:1] == "=":
			category_in = [x for x in category[1:].split(",")]
			result = [val for val in result if val[2] in category_in]
		return result

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--filename", help="Enter the filename",default=None)
	parser.add_argument("-r","--datarange", help="Enter the range of random inputs to be generated",default=10,type=int)
	parser.add_argument("-d","--display", help="Enter the parameters to be displayed",default="all")
	parser.add_argument("-n","--name", help="Enter the query for name",default=None)
	parser.add_argument("-y","--year", help="Enter the query for year",default=None)
	parser.add_argument("-c","--category", help="Enter the query for category",default=None)
	parser.add_argument("-a","--achievement", help="Enter the query for achievement",default=None)
	parser.add_argument("-g","--gender", help="Enter the query for gender",default=None)
	args = parser.parse_args()
	filename = args.filename
	datarange = args.datarange
	display = args.display
	name = args.name
	year = args.year
	category = args.category
	achievement = args.achievement
	gender = args.gender
	database = [["Name","Year","Category","Achievement","Gender"]]
	if filename:
		database = readFile(filename,database)
	else:
		database = gen_rand_data(datarange,database)
	qp = queryParser()
	for d in database:
		print d
	disp = qp.parse_display(display)
	print disp
	n = y = c = a = g = -1
	for atr in disp:
		q = atr.lower()
		if q=="name":
			n = disp.index("Name")
		if q=="year":
			y = disp.index("Year")
		if q=="category":
			c = disp.index("Category")
		if q=="achievement":
			a = disp.index("Achievement")
		if q=="gender":
			g = disp.index("Gender")
	global result
	result = database[1:]
	if name:
		result = qp.parse_name(name,result)
		print result
	if year:
		result = qp.parse_year(year,result)
		print result
	if gender:
		result = qp.parse_gender(gender,result)
		print result
	if category:
		result = qp.parse_category(category,result)
		print result
	t = ""
	for x in disp:
		t = t + str(x) + "\t"
	print t+"\n"
	for val in result:
		temp = [""]*5
		for data in val:
			if n!=-1:
				temp[n] = val[0]
			if y!=-1:
				temp[y] = val[1]
			if c!=-1:
				temp[c] = val[2]
			if a!=-1:
				temp[a] = val[3]
			if g!=-1:
				temp[g] = val[4]
		t = ""
		for x in temp:
			if x!="":
				t = t + str(x) + "\t"
		print t+"\n"

if __name__ == "__main__":
	main()