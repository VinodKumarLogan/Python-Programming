import urllib2,re
req = urllib2.Request('http://en.wikipedia.org/wiki/List_of_Nobel_laureates', headers={'User-Agent' : "Firefox/13.0"})
resp = urllib2.urlopen(req)
data = resp.read()
yearPattern = '(<td align="center">([0-9]*)</td>)'
tdPattern1 = '(<td><span style="display:none;">(.*?)</span><span class="vcard"><span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></span></span></td>)'
tdPattern2 = '(<td><span style="display:none;">(.*?)</span><span class="vcard"><span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></span></span>)'
tablePattern = '(<span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</span>)'
tablePattern1 = '(<span style="display:none;">(.*?)</span><span class="vcard"><span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></span></span></td>)'
tablePattern2 = '(<span style="display:none;">(.*?)</span><span class="vcard"><span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></span></span>;<br />)'
#sampleData = "<table>this is hawkeye</table><table>aldfaerfwer</table>"
sampleData = '<td align="center">2000</td><td align="center">1992</td>'
#match = re.findall('<a href="(.*?)".*>(.*)</a>', data)
pattern = yearPattern+"|"+tdPattern1+"|"+tdPattern2+"|"+tablePattern2+"|"+tablePattern1
'''
if match:
    for link, title in match:
        print " %s -> %s" % (link, title)
'''
#matchedYears = re.findall(yearPattern,data)
count = 0
#matchedPeople = re.findall(tablePattern,data)
matched = re.findall(pattern,data)
nobel = {}
temp = 0
#for x in matched:
#	print x

for x in matched:
	try:
		nobel[int(x[1])] = []
		temp = int(x[1])
	except:
		if not not x[2]:
			nobel[temp].append([x[6]])
			cur = nobel[temp].index([x[6]])
		elif not not x[7]:
			nobel[temp].append([x[11]])
			cur = nobel[temp].index([x[11]])
		if not not x[12]:
			nobel[temp][cur].append(x[16])
		elif not not x[17]:
			nobel[temp][cur].append(x[21])
	count+=1
for key,items in nobel.items():
	print key," ",items

print count-(2012-1900)
#print matchedYears