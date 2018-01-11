import matplotlib.pyplot as plt

tags = ['#gohawks','#gopatriots','#nfl','#patriots','#sb49','#superbowl']

def get_vals(tag):
	f_name = 'twitter_data/original/'+tag+'.pickle'
    with open(f_name) as f:
        data = pickle.load(f)

    k_m = max(data.keys())
    all_vals = [0]*(k_m + 1)

    for i in range(k_m+1):
        if i in data:
            all_vals[i] = data[i][0]

    return all_vals

for tag in tags:
	vals = get_vals(tag)
	plt.figure()
	plt.bar(range(vals),vals)
	plt.ylabel('Number of Tweets')
	plt.xlabel('Day Number')
	st = 'Number of tweets for '+tag
	plt.title(st)
	plt.savefig(tag+'.png') 