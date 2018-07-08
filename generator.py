from random import *


with open('MMW_train_data_large.txt', 'a') as FF:
	for i in xrange(55000):
		re = []
		k = range(8)
		shuffle(k)

		for i in k:
			#k = range(8)
			r = [0]*8
			r[i] = 1
			re.append(r)

		data = [[randint(1,90) for i in range(8)]for j in range(8)]

		for i in range(len(data)):
			m = max(data[i])
			data[i][k[i]] = m + randint(-3,3)

		FF.write( str(data))
		FF.write("\n")
		FF.write("\n")
		FF.write( str(re))
		FF.write("\n###\n")



#print re
