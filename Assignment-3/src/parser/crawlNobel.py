import urllib2,re

req = urllib2.Request('http://en.wikipedia.org/wiki/List_of_Nobel_laureates', headers={'User-Agent' : "Firefox/13.0"})
resp = urllib2.urlopen(req)
data = resp.read()
yearPattern1 = '(<td>([0-9]+)</td>)'
yearPattern2 = '(<td rowspan="[0-9]+">([0-9]+)</td>)'

tdPattern1 = '''
<tr>
<td>([0-9]+)</td>
<td><a href="/wiki/(.*?)" class="image"><img alt="(.*?)" src="(.*?)" width="([0-9]+)" height="([0-9]+)" srcset="(.*?)" />(.*?)</a></td>
<td><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></td>
<td><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></td>
<td>(.*?)</td>
</tr>
'''
tdPattern2 = '''
<tr>
<td rowspan="([0-9]+)">([0-9]+)</td>
<td><a href="/wiki/(.*?)" class="image"><img alt="(.*?)" src="(.*?)" width="([0-9]+)" height="([0-9]+)" srcset="(.*?)" />(.*?)</a></td>
<td><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></td>
<td><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></td>
<td>(.*?)</td>
</tr>
'''
tdPattern3 = '''
<tr>
<td><a href="/wiki/(.*?)" class="image"><img alt="(.*?)" src="(.*?)" width="([0-9]+)" height="([0-9]+)" srcset="(.*?)" />(.*?)</a></td>
<td><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></td>
<td><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></td>
<td>(.*?)</td>
</tr>
'''
tdPattern4 = '''
<tr>
<td><a href="/wiki/(.*?)" class="image"><img alt="(.*?)" src="(.*?)" width="([0-9]+)" height="([0-9]+)" srcset="(.*?)" />(.*?)</a></td>
<td><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></td>
<td>(.*?)</td>
</tr>
'''
tablePattern = '(<span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</span>)'
tablePattern1 = '(<span style="display:none;">(.*?)</span><span class="vcard"><span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></span></span></td>)'
tablePattern2 = '(<span style="display:none;">(.*?)</span><span class="vcard"><span class="fn"><a href="/wiki/(.*?)" title="(.*?)">(.*?)</a></span></span>;<br />)'
#sampleData = "<table>this is hawkeye</table><table>aldfaerfwer</table>"
sampleData = '<td align="center">2000</td><td align="center">1992</td>'
#match = re.findall('<a href="(.*?)".*>(.*)</a>', data)
#p = '<tr>(.*?)</tr>'
pattern = yearPattern2+"|"+yearPattern1+"|"+tablePattern+"|"+tablePattern2+"|"+tablePattern
#pattern = p
#matchedYears = re.findall(yearPattern,data)
count = 0
#matchedPeople = re.findall(tablePattern,data)
matched = re.findall(pattern,data)
for r in matched:
	print r,"\n"
print len(matched)
