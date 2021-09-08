class Cube(object):
	"""docstring for Cube"""
	def __init__(self, arg):
		super(Cube, self).__init__()
		self.arg,self.cube=setup(arg)
	def show(self):
		a=self.arg
		leg={'w':0,'y':5,'b':1,'g':2,'r':4,'o':3}
		seq=['b',' ','g','o','w','r','y']
		for i in range(3):
			if i==1:
				for j in range(3):
					print("    ",end="")
					for k in range(1,5):
						for l in range(3):
							print(" [",a[leg[seq[k-1+3]]][j][l],end="]")
					print()
			else:
				for j in range(3):
					print("           	   ",end="")
					for k in range(3):
						print(" [",a[leg[seq[i]]][j][k],end="]")
					print('')
			print()
def setup(arg):
		a,b,form=[list(i) for i in arg.split(" ")],{},['W','B','G','O','R','Y']
		[a[i].insert(4,form[i].lower()) for i in range(len(a))]
		[a[i].insert(3,' ') for i in range(len(a))]
		[a[i].insert(7,' ') for i in range(len(a))]
		for i in range(len(a)):
			a[i]=[list(i) for i in ''.join(a[i]).split(" ")]
			b[form[i].lower()]=a[i]
		return a,b



"""
			b b b
			b U b
			b b b
	  o o o	w w w r r r y y y
	  o L o	w F w r R r y B y
	  o o o	w w w r r r y y y
			g g g
			g D g
			g g g
	
	format: F U D L R B
	color:  w b g o r y
"""