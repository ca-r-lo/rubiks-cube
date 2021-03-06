
import sys


# GOAL: Bf Rd Ou Wl Gb Yr format
#           ooo
#           oOo
#           ooo
#       www bbb yyy ggg
#       wWw bBb yYy gGg
#       www bbb yyy ggg
#           rrr
#           rRr
#           rrr
# TODO: gggyrwwg ggyrwwro boyywoow woybgrgo rbobybyb robwrrby sample 

class Cube:
    def __init__(self, arg):  
        self.arg = arg
        # Assign each color to a variable
        self.blue = list(arg[0])
        self.red = list(arg[1])
        self.orange = list(arg[2])
        self.white = list(arg[3])
        self.green = list(arg[4])
        self.yellow = list(arg[5])
        
        comp = [self.blue,self.red,self.orange,self.white,self.green,self.yellow]
        set=list("browgy")
        for i in range(len(comp)):
            comp[i].insert(4,set[i])
        b,r,o,w,g,y = comp[0],comp[1],comp[2],comp[3],comp[4],comp[5]
        comp[0]=[b[i:i + 3] for i in range(0, len(b), 3)]
        comp[1]=[r[i:i + 3] for i in range(0, len(r), 3)]
        comp[2]=[o[i:i + 3] for i in range(0, len(o), 3)]
        comp[3]=[w[i:i + 3] for i in range(0, len(w), 3)]
        comp[4]=[g[i:i + 3] for i in range(0, len(g), 3)]
        comp[5]=[y[i:i + 3] for i in range(0, len(y), 3)]
        self.theList = comp

    def move(self):
        comp = self.theList
        b,r,o,w,g,y = comp[0],comp[1],comp[2],comp[3],comp[4],comp[5]
        # set the sides: up,down,lef,right
        # print(y)
        blue_sides=[o[2],r[0],rotateL(w)[0],rotateR(y)[0]]
        green_sides= [o[0],r[2],rotateL(rotateL(y))[0],rotateR(rotateR(w))[0]]
        orange_sides=[rotateR(rotateR(g))[2],b[0],rotateL(w)[0],rotateR(y)[0]]
        red_sides=[b[2],g[0],w[2],y[2]]
        yellow_sides=[rotateL(o)[0],rotateL(b)[0],rotateL(r)[0],rotateL(g)[0]]
        white_sides=[o[2],r[2],g[2],b[2]]
        print(white_sides)
        # print(rotateL(g))
        # print(rotateL(o))

        # rotate(b)



    def show(self):
        comp = self.theList
        b,r,o,w,g,y = comp[0],comp[1],comp[2],comp[3],comp[4],comp[5]

        for i in o:
            print("          ",*i)
        for i in range(len([w,b,y,g])-1):
            print("  ",*w[i]," ",*b[i]," ",*y[i]," ",*g[i])
        for i in r:
            print("          ",*i)


def rotateR(lst):
    a,b=lst,[]
    # print(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            # b.append(calcRight([i,j]))
            x=calcRight([i,j])
            a[i][j],a[x[0]][x[1]+2]=a[x[0]][x[1]+2],a[i][j]
            a[0][1],a[2][1],a[0][2],a[2][0]=a[2][1],a[0][1],a[2][0],a[0][2]
    return a
def rotateL(lst):
    a,b=lst,[]
    # print(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            # b.append(calcRight([i,j]))
            x=calcLeft([i,j])
            a[i][j],a[x[0]+2][x[1]]=a[x[0]+2][x[1]],a[i][j]
            a[0][1],a[2][1],a[0][2],a[2][0]=a[2][1],a[0][1],a[2][0],a[0][2]
    return a

# turn right
def calcRight(vect):
    i_h,j_h,a=[0,-1],[1,0],vect 
    return i_h[0]*a[0]+j_h[0]*a[1],i_h[1]*a[0]+j_h[1]*a[1]
def calcLeft(vect):
    i_h,j_h,a=[0,1],[-1,0],vect 
    return i_h[0]*a[0]+j_h[0]*a[1],i_h[1]*a[0]+j_h[1]*a[1]


# TODO: main func
def main(arg):
    sides = arg.split(" ")
    check(sides)
    print(f"Splitting Input:{sides}")
    print("Constructing Cube")
    cube = Cube(sides)
    cube.show()
    cube.move()
    # cube.create()

    # ['gggyrwwg', 'ggyrwwro' ,'boyywoow', 'woybgrgo', 'rbobybyb', 'robwrrby']
def check(arg): 
    # check if argument length is correct
    if len(arg) != 6 : raise SystemExit(f"Usage: {arg[0:]} <input_number_of_sides_by_format> in arg_length: {len(arg)} ")
    # check individual input side input if correct
    for i in range(len(arg)):
        if len(arg[i]) != 8: raise SystemExit(f"Usage: {arg[0:]} <input_side_length_by_format> in arg[{i}]: \"{arg[i]}\"  ")
    
    # letters allowed for inputs
    set=list("browgy")
    numberOfLetters=[0,0,0,0,0,0]
    # TODO: check individual sides if all inputs are correct following Bf Rd Ou Wl Gb Yr format
    for i in range(len(arg)):
        for j in range(len(arg[i])):
            # print(arg[i][j])
            if arg[i][j] not in set: raise SystemExit(f"Usage: {arg[i]} <letter_not_recognized> at \"{arg[i][j]}\" in {arg[i][j]} ")
            
            # count number of letter and check if its == 6
            if arg[i][j] == 'b': numberOfLetters[0]+=1
            elif arg[i][j] == 'r':numberOfLetters[1]+=1
            elif arg[i][j] == 'o':numberOfLetters[2]+=1
            elif arg[i][j] == 'w':numberOfLetters[3]+=1
            elif arg[i][j] == 'g':numberOfLetters[4]+=1
            elif arg[i][j] == 'y':numberOfLetters[5]+=1

    # check if numberOfLetters is 6
    a,b,c="","",False
    for i in range(len(numberOfLetters)): 
        if numberOfLetters[i] > 8: 
            a=set[i]
            c=True
        if numberOfLetters[i] < 8: b=set[i]
    if c :raise SystemExit(f"Usage: <number_of_individual_letter_exceeded_limit> : letter \'{a}\' exceeded the limit, letter \'{b}\' did not reach the limit check input properly")             
    print("check done. ")
if __name__ == '__main__':
	try:
		arg = sys.argv
		main(' '.join(arg[1:]))
	except Exception as e:
		raise SystemExit(e)
	