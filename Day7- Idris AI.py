def strange(begin, end, interval=1):
	strange_list= [i for i in list(range(begin,end,interval))]
	return strange_list
	
def blist(function):
	return list(function)
	
def some(function2):
	return sum(function2)

print(some(blist(strange(3,20))))