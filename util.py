import random

def weighted_choice(choices):
	"""
	Takes a dict of {choice: weight}
	"""
	total = sum([weight for weight in choices.values()])
	rand = random.uniform(0, total)
	upto = 0
	for choice, weight in choices.items():
	    if upto + weight > rand:
	        return choice
	    upto += weight
	return -1 # not sure what to do if there's not enough time left