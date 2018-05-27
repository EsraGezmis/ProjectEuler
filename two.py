xlist=[1,2]
s2=2
for i in xlist:
	s2=i+s2
	if s2<90:
		xlist.append(s2)
print(xlist)

def f(x):
	return x%2==0
result=list(filter(f,xlist))
print(result)
