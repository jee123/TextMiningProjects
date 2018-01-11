import pickle
import matplotlib.pyplot as plt
import math

tags = ['#gohawks','#gopatriots','#nfl','#patriots','#sb49','#superbowl']

def get_vals(tag,feat):
	f_name = tag+'_train_test.pickle'
	with open(f_name) as f:
		data = pickle.load(f)
	x = data['x'][:,feat]
	y = data['y']

	return x,y

def generate_plots():
	for tag in tags:
		for i in range(15):
			x,y = get_vals(tag,i)
			plt.figure()
			plt.scatter(x,y)
			
			plt.ylabel('Number of Tweets')
			plt.xlabel('Feature')

			plt.savefig('plots/q2/'+tag+'/'+tag[1:]+'_'+str(i)+'.png') 