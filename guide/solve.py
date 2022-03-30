from move import specMove as smv
from move import Move as mv
from random import randrange as rand
from random import shuffle as sh

class Solve():
	def slv(cube):
		code=algo(cube)

		# a=['d', 'j', 'i', 'h', 'b', 'f', 'k', 'a', 'c', 'e', 'g']
		# print(a)
		# ans=alg(a)
		# print(ans)




def llll(a,z):
	b,out='a b c d e f g h i j k'.split(' '),''
	for i in range(10):
		if a[i]!='a' and a[i] not in z:
			a[0],a[i]=a[i],a[0]
			z.append(a[0])
			break
	for i in range(len(a)):
		if a[0]=='a':break
		index=b.index(a[0])
		a[0],a[index]=a[index],a[0]
		out+=a[0]
	return a,z+list(out)
def alg(a):
	t,v=[],[]
	for i in range(10):
		if t == 'a b c d e f g h i j k'.split(' '):break
		t,v=llll(a,v)
	return v


# u2 bP rP u lP f f b r2 b f r r f bP fP u f  :  o p h , a l t x s k a , d e , c i
# u d2 u2 b2 rP d2 b r2 r l2 u d dP d bP b b bP : g t v , a j r l k q , c s i


def algo(cube):
	a=cube
	w,y,b,g,r,o=a['w'],a['y'],a['b'],a['g'],a['r'],a['o']
	alphEdg={'A':[b[0][1],y[0][1],'b','y'],'B':[b[1][2],r[0][1],'b','r'],'C':[b[2][1],w[0][1],'b','w'],'D':[b[1][0],o[0][1],'b','o'],
		'I':[w[0][1],b[2][1],'w','b'],'J':[w[1][2],r[1][0],'w','r'],'K':[w[2][1],g[0][1],'w','g'],'L':[w[1][0],o[1][2],'w','o'],
		'E':[o[0][1],b[1][0],'o','b'],'F':[o[1][2],w[1][0],'o','w'],'G':[o[2][1],g[1][0],'o','g'],'H':[o[1][0],y[1][2],'o','y'],
		'M':[r[0][1],b[1][2],'r','b'],'N':[r[1][2],y[1][0],'r','y'],'O':[r[2][1],g[1][2],'r','g'],'P':[r[1][0],w[1][2],'r','w'],
		'Q':[y[0][1],b[0][1],'y','b'],'R':[y[1][2],o[1][0],'y','o'],'S':[y[2][1],g[2][1],'y','g'],'T':[y[1][0],r[1][2],'y','r'],
		'U':[g[0][1],w[2][1],'g','w'],'V':[g[1][2],r[2][1],'g','r'],'W':[g[2][1],y[2][1],'g','y'],'X':[g[1][0],o[2][1],'g','o']
		}
	
	alphCorn={'B':[b[0][2],r[0][2],y[0][0]],'A':[b[0][0],o[0][0],y[2][1]],'C':[b[2][2],r[0][0],w[0][2]],'D':[b[2][0],o[0][2],w[0][0]],
		'E':[w[0][0],o[0][2],b[2][0]],'F':[w[0][2],r[0][0],b[2][2]],'G':[w[2][2],r[2][0],g[0][2]],'H':[w[2][0],o[2][2],g[0][0]],
		'I':[o[0][0],y[0][2],b[0][0]],'J':[o[0][2],w[0][0],b[2][0]],'K':[o[2][2],w[2][0],g[0][0]],'L':[o[2][0],y[2][2],g[2][0]],
		'M':[r[0][0],w[0][2],b[2][2]],'N':[r[0][2],y[0][0],b[0][2]],'O':[r[2][2],y[2][0],g[2][2]],'P':[r[2][0],w[2][2],g[0][2]],
		'Q':[y[0][0],r[0][2],b[0][2]],'R':[y[0][2],o[0][0],b[0][0]],'S':[y[2][2],o[2][0],g[2][0]],'T':[y[2][0],r[2][2],g[2][2]],
		'U':[g[0][0],o[2][2],w[2][0]],'V':[g[0][2],r[2][0],w[2][2]],'W':[g[2][2],r[2][2],y[2][0]],'X':[g[2][0],o[2][0],y[2][2]]
		}
	edgeConn={'A':'Q','B':'M','C':'I','D':'E','E':'D','F':'L','G':'X','H':'R',
		'I':'C','J':'P','K':'U','L':'F','M':'B','N':'T','O':'V','P':'J',
		'Q':'A','R':'H','S':'W','T':'N','U':'K','V':'O','W':'S','X':'G'
		}
	
	allg(alphEdg,edgeConn)


def allg(a,b):
	s=list('ACDEFGHOJKLMNOPQRSTUVWX')
	buf=a['B']


	print(buf)



































patt1='r rP l lP u uP d dP f fP b bP r2 l2 u2 d2 f2 b2'.split(' ')
patt2=['l2', 'fP', 'u', 'f', 'r2', 'b', 'bP', 'b2', 'rP', 'uP', 'd2', 'dP', 'l', 'r', 'lP', 'd', 'u2', 'f2']
def toString(dict):
	seq,b,a=['w','b','g','o','r','y'],'',''
	for i in seq:
		for j in dict[i]:
			b+=''.join(j)
		b=list(b)
		b.pop(4)
		a,b=a+''.join(b)+' ',''
	a=list(a)
	a.pop(-1)
	return ''.join(a)

def mov(mvs,dic):
	if mvs == 'u':
		return (mv.u(dic))
	elif mvs=='d':
		return (mv.d(dic))
	elif mvs=='f':
		return (mv.f(dic))
	elif mvs=='r':
		return (mv.r(dic))
	elif mvs=='l':
		return (mv.l(dic))	
	elif mvs=='b':
		return (mv.b(dic))
	elif mvs == 'uP':
		return (mv.uP(dic))
	elif mvs=='dP':
		return (mv.dP(dic))
	elif mvs=='fP':
		return (mv.fP(dic))
	elif mvs=='rP':
		return (mv.rP(dic))
	elif mvs=='lP':
		return (mv.lP(dic))	
	elif mvs=='bP':
		return (mv.bP(dic))
	elif mvs=='u2':
		return (smv.u2(dic))
	elif mvs=='d2':
		return (smv.d2(dic))
	elif mvs=='l2':
		return (smv.l2(dic))
	elif mvs=='r2':
		return (smv.r2(dic))
	elif mvs=='f2':
		return (smv.f2(dic))
	elif mvs=='b2':
		return (smv.b2(dic))






# u2 bP rP u lP f f b r2 b f r r f bP fP u f  :  o p h , a l t x s k a , d e , c i
# u d2 u2 b2 rP d2 b r2 r l2 u d dP d bP b b bP : g t v , a j r l k q , c s i
# dP u2 uP uP d2 b r2 f2 u2 rP u2 dP u uP l2 u2 dP bP : 























	# # print(alphCorn['X'])
	# for i in list('ABCDEFGHIJKLMNOPQRSTUVWX'):
	# 	print(i,alphEdg[i],alphCorn[i])