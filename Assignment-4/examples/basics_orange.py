import orange

#data = orange.ExampleTable(r'C:\home\ananth\research\python\pesit\unit5\datasets\statewise_education_enrollment.tab')
data = orange.ExampleTable(r'C:\home\ananth\research\python\pesit\unit5\datasets\simulated.tab')

print data.domain.attributes

for i in range(5):
    print data[i]

# report on number of classes and attributes
print "Classes:", len(data.domain.classVar.values)
print "Attributes:", len(data.domain.attributes), ",",

# count number of continuous and discrete attributes
ncont=0
ndisc=0
for a in data.domain.attributes:
    if a.varType == orange.VarTypes.Discrete:
        ndisc = ndisc + 1
    else:
        ncont = ncont + 1
print ncont, "continuous,", ndisc, "discrete"

# obtain class distribution
c = [0] * len(data.domain.classVar.values)
for e in data:
    c[int(e.getclass())] += 1
print "Instances: ", len(data), "total",
for i in range(len(data.domain.classVar.values)):
    print ",", c[i], "with class", data.domain.classVar.values[i],
print

print "Continuous attributes:"
for a in range(len(data.domain.attributes)):
    if data.domain.attributes[a].varType == orange.VarTypes.Continuous:
        d = 0.; n = 0
        for e in data:
            if not e[a].isSpecial():
                d += e[a]
                n += 1
        print "  %s, mean=%3.2f" % (data.domain.attributes[a].name, d/n)

print "\nNominal attributes (contingency matrix for classes:", data.domain.classVar.values, ")"
cont = orange.DomainContingency(data)
for a in data.domain.attributes:
    if a.varType == orange.VarTypes.Discrete:
        print "  %s:" % a.name
        for v in range(len(a.values)):
            sum = 0
            for cv in cont[a][v]:
                sum += cv
            print "    %s, total %d, %s" % (a.values[v], sum, cont[a][v])
        print
