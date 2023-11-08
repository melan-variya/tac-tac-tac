
#from IPython.display import clear_output  
lis=[]
def validate():
	ans=True
	b=input("wanna start the game (Y or N) :")
	while ans:
		if b not in ['Y' , 'N']:
			b=input("I dont understant plz type Y or N :")
		if b in ['Y','N']:
			ans=False
			return b

li1f = [" ", " ", " "]
li2f = [" ", " ", " "]
li3f = [" ", " ", " "]
def update_board(i, no):
    
    if i % 2 == 1:
        if no <= 3:
            li1f[no - 1] = 'X'
        elif no <= 6:
            li2f[no - 4] = 'X'
        elif no <= 9:
            li3f[no - 7] = 'X'
    else:
        if no <= 3:
            li1f[no - 1] = 'O'
        elif no <= 6:
            li2f[no - 4] = 'O'
        elif no <= 9:
            li3f[no - 7] = 'O'
    #clear_output()
    print(li1f[0]+" | "+ li1f[1]+" | "+li1f[2])
    print(li2f[0]+" | "+ li2f[1]+" | "+li2f[2])
    print(li3f[0]+" | "+ li3f[1]+" | "+li3f[2])

def win_lose():
	if (li1f[0]==li1f[1]==li1f[2]==('X' or 'O')) :
		return ("{} win".format(li1f[0]))
	if (li2f[0]==li2f[1]==li2f[2]==('X' or 'O')) :
		return ("{} win".format(li2f[0]))
	if (li3f[0]==li3f[1]==li3f[2]==('X' or 'O')):
		return ("{} win".format(li3f[0]))
	if (li1f[0]==li2f[0]==li3f[0]==('X' or 'O')):
		return ("{} win".format(li3f[0]))
	if (li1f[1]==li2f[1]==li3f[1]==('X' or 'O')):
		return ("{} win".format(li3f[1]))
	if (li1f[2]==li2f[2]==li3f[2]==('X' or 'O')):
		return ("{} win".format(li3f[2]))
	if li1f[0]==li2f[1]==li3f[2]==('X' or 'O'):
		return ("{} win".format(li3f[2]))
	if li3f[0]==li2f[1]==li1f[2]==('X' or 'O'):
		return ("{} win".format(li3f[0]))
	else:
		return " "
	
	
def start_game(i):
    if i % 2 == 1:  
        cho1 = int(input('player 1 turn, choose (1-9) place for X: '))
        while cho1 not in range(1, 10):
            cho1 = int(input('It is not in range (1-9), try again: '))
        while cho1 in lis:
            cho1 = int(input("Number is already chosen, choose another: "))
        lis.append(cho1)
        return cho1

    if i % 2 == 0: 
        cho2 = int(input('player 2 turn, choose (1-9) place for O: '))
        while cho2 not in range(1, 10):
            cho2 = int(input('It is not in range (1-9), try again: '))
        while cho2 in lis:
            cho2 = int(input("Number is already chosen, choose another: "))
        lis.append(cho2)
        return cho2

			
	
print('■ Game Instruction:')
print('Enter number from (1-9) to chose place')
li1 =[	'  1  '  , '|' ,  '  2  ' ,  '|'  , '  3  ']
li2 =[	'  4  '  , '|' ,  '  5  ' ,  '|'  , '  6  ']
li3 =[	'  7  '  , '|'  , '  8  ' ,  '|' ,  '  9  ']
for i in li1:
	print(i, end=" ")
print()
for i in li2:
	print(i, end=" ")
print()
for i in li3:
	print(i, end=" ")
print()

name1=input('Player 1 Name (X) :')
name2=input('Player 2 Name (O) :')

res=" "
for i in range(1 , 10):
	re=start_game(i)
	update_board(i,re)
	res=win_lose()
	if res=="X win" or res=="O win":
		print(res+" (:")
		break
if res==" " :
	print("draw")