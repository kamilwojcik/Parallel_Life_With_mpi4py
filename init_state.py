import numpy as np

def random_state(shape):
     arr=(np.random.random_integers(2,size=shape)-1).astype(bool)
     return arr
	