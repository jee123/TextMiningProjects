import results
import pickle
import plot_prob as pp

tags = ['#gohawks','#gopatriots','#nfl','#patriots','#sb49','#superbowl']
with open('times.pickle') as f:
	res_time = pickle.load(f)

print 'Getting regression values'
for tag in tags:
	print '*'*80+'\n'
	print 'Currently working with '+tag
	results.get_pval(tag)

print 'Generating plots'
pp.generate_plots()

print 'Performing cross validation'
for tag in tags:
	print '*'*80+'\n'
	print 'Currently working with '+tag	
	results.cross_val(tag)

print 'Performing regression for different parts'
for tag in tags:
	print '*'*80+'\n'
	print 'Currently working with '+tag
	results.three_part_split(tag,res_time[tag])


