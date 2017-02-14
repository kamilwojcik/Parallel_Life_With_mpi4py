import numpy as np
import rules as rls
import matplotlib.pyplot as pp
import init_state as inst

class Space:
	def __init__(self, n, m):
	    self.plane=np.full((n,m),False,np.bool)
	    self.plane=inst.random_state(self.plane.shape)
	    self.plane_next_step=np.full((n,m),False,np.bool)
	    
	    
	def GetNeighbourhood(self,i,j):
		return self.plane[i-1:i+2,j-1:j+2]
	
			
	def RefreshPlane(self):
		self.plane=self.plane_next_step.copy()
	
	
	def CalculateNextStep(self):
		for i in range(1,self.plane.shape[0]-1):
			for j in range(1,self.plane.shape[1]-1):
				self.plane_next_step[i][j]=rls.applyrules(self.GetNeighbourhood(i,j))


	def MakeStep(self):
		self.CalculateNextStep()
		self.RefreshPlane()

