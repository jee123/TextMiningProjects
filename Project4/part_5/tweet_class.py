import numpy as np

class ts_data(object):
	def __init__(self, counts):
		self.shifted_c = np.array([0] + counts[:-1])
		self.c = np.array(counts)
		self.d = self.c - self.shifted_c

	def moving_average(self,k, mean = True,d = False):
		if d:
			arr = self.d
		else:
			arr = self.c
		n = len(arr)

		res = [0]*n
		for i in range(n):
			if i >= k-1:
				temp = arr[i-k+1:i+1]
			else:
				temp = arr[:i+1]
			if mean:
				res[i] = np.mean(temp)
			else:
				res[i] = np.std(temp)
		return res

	def get_d(self):
		return self.d

# if __name__ = 'main'
# a = [1,2,3,4,5]
# b = ts_data(a)
# print b.moving_average(3)
# print b.moving_average(1,True)
# print b.moving_average(3,False,False)
	
