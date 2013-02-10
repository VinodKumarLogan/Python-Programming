import argparse,random,string

def id_generator(size=4, chars=string.ascii_lowercase):
	'''Generates random strings'''
	return ''.join(random.choice(chars) for x in range(size))

def readFile(filename,database):
	'''Reads from a file and stores it in a database'''
	f = open(filename,'r')
	data = f.read().split(";")
	for val in data:
		e = {}
		d = val.split(",")
		for r in d:
			c = r.split("=")
			if c[0]=="name":
				e['name'] = c[1]
			elif c[0]=="year":
				e['year'] = int(c[1])
			elif c[0]=="category":
				e['category'] = c[1]
			elif c[0]=="achievement":
				e['achievement'] = c[1]
			elif c[0]=="gender":
				e['gender'] = c[1]
			elif c[0]=="country":
				e['country'] = c[1]
		database.append(e)
	return database[:-1]

def gen_rand_data(datarange,database):
	'''Generates random entries for the database'''
	i = 0
	f = open("database.in",'a')
	while i<datarange:
		e = {}
		name = str(id_generator())
		year = random.randrange(1990,2013)
		category = str(id_generator())
		achievement = str(id_generator())
		gender = str(id_generator(1,"fm"))
		country = str(id_generator())
		e['name'] = name
		e['year'] = year
		e['category'] = category
		e['achievement'] = achievement
		e['gender'] = gender
		e['country'] = country
		f.write("name="+name+",year="+str(year)+",category="+category+",achievement="+achievement+",gender="+gender+",country="+country+";")
		database.append(e)
		#database.append([name,year,category,achievement,gender,country])
		i = i + 1
	return database

class queryParser:

	def parse_display(self,display):
		'''Parses the data to be displayed'''
		toBeDisplayed = []
		if display=="all":
			toBeDisplayed = ["Name","Year","Category","Achievement","Gender","Country"]
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
				elif val=="country":
					toBeDisplayed.append("Country")
		return toBeDisplayed

	def parse_name(self,name,result):
		'''Parses the queries for attribute name'''
		name = name.strip().replace(" ","")
		name_not_in = []
		name_in = []
		temp = []
		if name[:2] == "!=":
			name_not_in = [x for x in name[2:].split(",")]
			for val in result:
				if val['name'] not in name_not_in:
					temp.append(val)
		elif name[:1] == "=":
			name_in = [x for x in name[1:].split(",")]
			for val in result:
				if val['name'] in name_in:
					temp.append(val)
		return temp

	def parse_year(self,year,result):
		'''Parses the queries for attribute year'''
		year = year.strip().replace(" ","")
		temp = []
		if year[:2] == "!=":
			year_not_in = [x for x in year[2:].split(",")]
			for val in result:
				if str(val['year']) not in year_not_in:
					temp.append(val)
		elif year[:1] == "=":
			year_in = [x for x in year[1:].split(",")]
			for val in result:
				if str(val['year']) in year_in:
					temp.append(val)
		elif year[:2] == '>=':
			y = int(year[2:])
			for val in result:
				if val['year'] >= y:
					temp.append(val)
		elif year[:2] == '<=':
			y = int(year[2:])
			for val in result:
				if val['year'] <= y:
					temp.append(val)
		elif year[:1] == '>':
			y = int(year[1:])
			for val in result:
				if val['year'] > y:
					temp.append(val)
		elif year[:1] == '<':
			y = int(year[1:])
			for val in result:
				if val['year'] < y:
					temp.append(val)
		return temp

	def parse_gender(self,gender,result):
		'''Parses the queries for attribute gender'''
		gender = gender.strip().replace(" ","")
		gender_not_in = []
		gender_in = []
		temp = []
		if gender[:2] == "!=":
			gender_not_in = [x for x in gender[2:].split(",")]
			for val in result:
				if val['gender'] not in gender_not_in:
					temp.append(val)
		elif gender[:1] == "=":
			gender_in = [x for x in gender[1:].split(",")]
			for val in result:
				if val['gender'] in gender_in:
					temp.append(val)
		return temp

	def parse_category(self,category,result):
		'''Parses the queries for attribute category'''
		category = category.strip().replace(" ","")
		category_not_in = []
		category_in = []
		temp = []
		if category[:2] == "!=":
			category_not_in = [x for x in category[2:].split(",")]
			for val in result:
				if val['category'] not in category_not_in:
					temp.append(val)
		elif category[:1] == "=":
			category_in = [x for x in category[1:].split(",")]
			for val in result:
				if val['category'] in category_in:
					temp.append(val)
		return temp

	def parse_country(self,country,result):
		'''Parses the queries for attribute country'''
		country = country.strip().replace(" ","")
		country_not_in = []
		country_in = []
		temp = []
		if country[:2] == "!=":
			country_not_in = [x for x in country[2:].split(",")]
			for val in result:
				if val['country'] not in country_not_in:
					temp.append(val)
		elif country[:1] == "=":
			country_in = [x for x in country[1:].split(",")]
			for val in result:
				if val['country'] in country_in:
					temp.append(val)
		return temp

	def parse_achievement(self,achievement,result):
		'''Parses the queries for attribute achievement'''
		achievement = achievement.strip().replace(" ","")
		achievement_not_in = []
		achievement_in = []
		temp = []
		if achievement[:2] == "!=":
			achievement_not_in = [x for x in achievement[2:].split(",")]
			for val in result:
				if val['achievement'] not in achievement_not_in:
					temp.append(val)
		elif achievement[:1] == "=":
			achievement_in = [x for x in achievement[1:].split(",")]
			for val in result:
				if val['achievement'] in achievement_in:
					temp.append(val)
		return temp



def main():
	'''This is where the program starts its execution'''
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--filename", help="Enter the filename",default=None)
	parser.add_argument("-r","--datarange", help="Enter the range of random inputs to be generated",default=10,type=int)
	parser.add_argument("-d","--display", help="Enter the parameters to be displayed",default="all")
	parser.add_argument("-n","--name", help="Enter the query for name",default=None)
	parser.add_argument("-y","--year", help="Enter the query for year",default=None)
	parser.add_argument("-c","--category", help="Enter the query for category",default=None)
	parser.add_argument("-a","--achievement", help="Enter the query for achievement",default=None)
	parser.add_argument("-g","--gender", help="Enter the query for gender",default=None)
	parser.add_argument("-t","--country", help="Enter the query for country",default=None)
	args = parser.parse_args()
	filename = args.filename
	datarange = args.datarange
	display = args.display
	name = args.name
	year = args.year
	category = args.category
	achievement = args.achievement
	gender = args.gender
	country = args.country
	database = [["Name","Year","Category","Achievement","Gender","Country"]]
	if filename:
		database = readFile(filename,database)
	else:
		database = gen_rand_data(datarange,database)
	qp = queryParser()
	for d in database:
		print d
	disp = qp.parse_display(display)
	print disp
	n = y = ca = a = g = co = -1
	for atr in disp:
		q = atr.lower()
		if q=="name":
			n = disp.index("Name")
		if q=="year":
			y = disp.index("Year")
		if q=="category":
			ca = disp.index("Category")
		if q=="achievement":
			a = disp.index("Achievement")
		if q=="gender":
			g = disp.index("Gender")
		if q=="country":
			co = disp.index("Country")
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
	if country:
		result = qp.parse_country(country,result)
		print result
	t = "|"
	for x in disp:
		t = t + str(x) + "\t|"
	print t+"\n"
	for val in result:
		temp = [""]*6
		for data in val:
			if n!=-1:
				temp[n] = val['name']
			if y!=-1:
				temp[y] = val['year']
			if ca!=-1:
				temp[ca] = val['category']
			if a!=-1:
				temp[a] = val['achievement']
			if g!=-1:
				temp[g] = val['gender']
			if co!=-1:
				temp[co] = val['country']
		t = "|"
		for x in temp:
			if x!="":
				t = t + str(x) + "\t|"
		print t+"\n"

if __name__ == "__main__":
	main()