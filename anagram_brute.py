s = raw_input("Enter the base string : ")
x = raw_input("Enter the test input : ")
s = s.replace(" ","")
x = x.replace(" ","")
print x,s
for q in s:
     try:
        i = x.index(q)
        del x[i]

if not x:
    print x," is an anagram of ",s
else:
    print x," is not an anagram of ",s
