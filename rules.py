import numpy as np
 
def rule4alive(neighbourhood):
	sum=neighbourhood.sum()
	if (sum==3 or sum==4):
		return True
	else:
		return False

def rule4dead(neighbourhood):
	sum=neighbourhood.sum()
	if (sum==3):
		return True
	else:
		return False

def applyrules(neighbourhood):
	if (neighbourhood[1][1]==True):
		return rule4alive(neighbourhood)
	else:
		return rule4dead(neighbourhood)