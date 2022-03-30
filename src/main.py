

import sys

def main(arg):
    sides = arg.split(" ")
    check(sides)
    
    
def check(arg): 
    # check if argument length is correct
    if len(arg) != 6 : raise SystemExit(f"Usage: {arg[0:]} <input_number_of_sides_by_format> in arg_length: {len(arg)} ")
    # check individual input side input if correct
    for i in range(len(arg)):
        if len(arg[i]) != 8: raise SystemExit(f"Usage: {arg[0:]} <input_side_length_by_format> in arg[{i}]: \"{arg[i]}\"  ")
    
    # letters allowed for inputs
    set=list("browgy")
    numberOfLetters=[0,0,0,0,0,0]
    # check individual sides if all inputs are correct following Bf Rd Ou Wl Gb Yr format
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
    a,b="",""
    for i in range(len(numberOfLetters)): 
        if numberOfLetters[i] > 8: a=set[i]
        if numberOfLetters[i] < 8: b=set[i]
    raise SystemExit(f"Usage: <number_of_individual_letter_exceeded_limit> : letter \'{a}\' exceeded the limit, letter \'{b}\' did not reach the limit check input properly")             
if __name__ == '__main__':
	try:
		arg = sys.argv
		main(' '.join(arg[1:]))
	except Exception as e:
		raise SystemExit(e)
	