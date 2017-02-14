import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

class SimpleAnimation:
	def __init__(self, nparrays):
		self.arrays=nparrays
		self.fig, self.sbplt=plt.subplots()
		self.curr_index=0
		self.img=self.sbplt.matshow(self.arrays[self.curr_index])
		self.anim=0
	
	def next_image(self, sth):
		self.img.set_data(self.arrays[self.curr_index])
		self.curr_index+=1
		return self.img

	def animate(self):
		print 'Preparing animation...'
		self.anim=animation.FuncAnimation(self.fig, self.next_image, interval=50, frames=range(len(self.arrays)-1))
		print '...done.'
	
	def save(self, out_file_name, fps):
		print 'Saving animation...'
		self.anim.save(out_file_name, fps=fps, extra_args=['-vcodec', 'libx264'])
		print '...done.'