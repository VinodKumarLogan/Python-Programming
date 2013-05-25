import orange

#data = orange.ExampleTable(r'C:\home\ananth\research\python\pesit\unit5\datasets\statewise_education_enrollment.tab')
data = orange.ExampleTable(r'C:\home\ananth\research\python\pesit\unit5\datasets\simulated.tab')
classifier = orange.BayesLearner(data)
#x = raw_input('enter a sentence with 6 words: ')
#words = x.split(' ')
#d = '\t'.join(words)
#c = classifier(orange.ExampleTable(d))
#print "classified as", c

data = orange.ExampleTable(r'C:\home\ananth\research\python\pesit\unit5\datasets\input.tab')

for i in range(len(data)):
#for i in range(30):
    print 'iteration = ', i
    c = classifier(data[i])
    print data[i], "classified as", c

print '-----------------------------------------------'
