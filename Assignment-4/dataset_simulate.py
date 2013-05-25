import random

positive_words = ['love', 'like', 'great', 'fantastic', 'awesome', 'beautiful', 'wow', 'superb', 'outstanding', 'elegant', 'special', 'joy', 'fun', 'good', 'better', 'best', 'delight']
negative_words = ['worry', 'sad', 'foul', 'disappointed', 'upset', 'hate', 'angry', 'bad', 'ugly',  'irritating', 'useless', 'waste',   'horrible', 'worse', 'worst', 'bizarre']

filename = r'C:\home\ananth\research\python\pesit\unit5\datasets\simulated.tab'
testfilename = r'C:\home\ananth\research\python\pesit\unit5\datasets\input.tab'

def create_test_dataset(fname, n, train):
    f = open(fname, 'w')
    atts = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'sentiment']
    types = ['d'] * 7
    types[6] = 'd'
    cls = [''] * 7
    cls[6] = 'class'
    
    f.write('\t'.join(atts) + '\n')
    f.write('\t'.join(types) + '\n')
    f.write('\t'.join(cls) + '\n')

    if (train):
        pos = 'positive'
        neg = 'negative'
    else:
        pos = ''
        neg = ''

    for i in range(n):
        line = 'Adobe\t' + 'product\t' + 'is\t' + positive_words[random.randrange(0, len(positive_words))] + '\t' + 'and\t' + positive_words[random.randrange(0, len(positive_words))] + '\t' + pos + '\n'
        f.write(line)

    for i in range(n):
        line = 'ABC\t' + 'product\t' + 'is\t' + negative_words[random.randrange(0, len(negative_words))] + '\t' + 'and\t' + negative_words[random.randrange(0, len(negative_words))] + '\t' + neg + '\n'
        f.write(line)

    f.close()


create_test_dataset(filename, 100, True)
create_test_dataset(testfilename, 100, False)
