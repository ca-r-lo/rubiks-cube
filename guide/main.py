
#  starting a new prject again. 



from cube import Cube
from solve import Solve as sv
from solve import mov,toString
from random import randrange as rr
import sys


def m(arg):
	a=Cube('wwwwwwww bbbbbbbb gggggggg oooooooo rrrrrrrr yyyyyyyy')
	for i in arg.split(' '):
		a=Cube(toString(mov(i,a.cube)))
	# a.show()
	sv.slv(a.cube)
	# print(a.cube)
def col(arg):
	a=Cube(arg)
	sv.slv(a.cube)
def ssss():
	patt1=['l2', 'fP', 'u', 'f', 'r2', 'b', 'bP', 'b2', 'rP', 'uP', 'd2', 'dP', 'l', 'r', 'lP', 'd', 'u2', 'f2']
	for i in range(len(patt1)):
	    print(patt1[rr(len(patt1))],end=' ')


	# # print(arg)
	# a=Cube(arg)
	# a.show()
	# print()
	# a=Cube(toString(mov('fP',a.cube)))
	# a.show()
# r u rP l2 d2 f u f bP

def main(arg):
	b=arg.split(' ')
	if b[0]=='-m':m(' '.join(b[1:]))
	elif b[0]=='-c':col(' '.join(b[1:]))
	elif b[0]=='-s':ssss()	
	else: print('duh')

if __name__ == '__main__':
	try:
		arg = sys.argv
		main(' '.join(arg[1:]))
	except IndexError as e:
		raise SystemExit(f"Usage: {sys.argv[0]} <cube_colors_by_format>")
	