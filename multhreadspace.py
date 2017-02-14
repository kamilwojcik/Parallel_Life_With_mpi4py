import numpy as np
from mpi4py import MPI
import space as sp

# Planes from different threads overlaps as follows:
#
#   m------------------------>
#   m/2+1 ---------->
# n [ x  x  x  x  g ]
# | [ x  x  x  x  g ]
# | [ x  x  x  x  g ] <-thread #0
# | [ x  x  x  x  g ]
# V [ x  x  x  x  g ]
#            [ g  x  x  x  x ]
#            [ g  x  x  x  x ]
# thread #1->[ g  x  x  x  x ]
#            [ g  x  x  x  x ]
#            [ g  x  x  x  x ]
#            <-----------m/2+1
#
# where g is 'ghost' column; corresponding x column is copied to g every step.
# As a sum of such planes we obtain n x m plane:
#
#   m------------------------>
# n [ x  x  x  x  x  x  x  x ]
# | [ x  x  x  x  x  x  x  x ]
# | [ x  x  x  x  x  x  x  x ]
# | [ x  x  x  x  x  x  x  x ]
# V [ x  x  x  x  x  x  x  x ]


thread0=0
thread1=1

class MultiThreadSpace(sp.Space):
	def __init__(self,n,m0, mpi_comm, rank):
		self.m=m0-m0%2  #m must be an even number
		sp.Space.__init__(self,n,self.m/2+1)
		self.shared_plane=np.full((n,self.m),False,np.bool)
		self.comm=mpi_comm
		self.rank=rank
	
	def ExchangeGhostData(self):
		if self.rank==0:
			self.comm.send(self.plane[:,-2], dest=thread1) #send column corresponding to ghost of other thread
			self.plane[:,-1]=self.comm.recv(source=thread1) #wait for data corresponding to this thread's ghost
		else:
			self.plane[:,0]=self.comm.recv(source=thread0) #wait for data
			self.comm.send(self.plane[:,1],dest=thread0) #send
	
	def Gather(self):
		if self.rank==0:
			self.shared_plane[:,:self.m/2]=self.plane[:,:-1]
			self.shared_plane[:,self.m/2:]=self.comm.recv(source=thread1)
		else:
			self.comm.send(self.plane[:,1:],dest=thread0)
		
	def MakeStep(self):
		sp.Space.MakeStep(self)
		self.ExchangeGhostData()
		self.Gather()
	