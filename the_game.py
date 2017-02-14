import space as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import simple_animation as s_anim
import time
import multhreadspace as mts
from mpi4py import MPI


comm=MPI.COMM_WORLD
rank=comm.Get_rank()
print 'Thread ', rank, ' reporting'
size=comm.Get_size()

thread0=0
thread1=1


if (size>2):
	print 'Too many threads. The procedure is undefined for this case. Aborting.'
elif (size<2):
	print 'There is no procedure defined for only one thread. Aborting.'
else:

	print 'Initializing space for thread ',rank,'...'
	
	space=mts.MultiThreadSpace(85,105, comm,rank)

	space.ExchangeGhostData()
	space.Gather()
	print 'Thread ',rank,': space initialized.\n'

	t0=0
	t1=0
	
	if rank==0:
		t0=time.clock()
		list_of_arrays=[]
		list_of_arrays.append(space.shared_plane.copy())
		print 'Running the game of life...'

	for i in range(200):
		space.MakeStep()
		if rank==0:
			list_of_arrays.append(space.shared_plane.copy())

	if rank==0:
		t1=time.clock()
		print '...done in ', t1-t0, ' seconds.\n'

		print 'Creating animation'
		anim=s_anim.SimpleAnimation(list_of_arrays)
		anim.animate()
		anim.save('myLife.mp4', 6)