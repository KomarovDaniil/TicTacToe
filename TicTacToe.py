board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']   #Board (Игровое поле)
win_chek = False
v = board[0]
x,o = 'X','O'
terner = True
counter_draw = 0
while win_chek == False: #Play cicle (Игровой цикл)
	if terner == True:  #Put figurse on board (Ставит фигуры на доску)
		idx = int(input(f'Ход {x}: '))
		board[idx] = x
		terner = False
	else:
		idx = int(input(f'Ход {o}: '))
		board[idx] = o
		terner = True
	koef = 0
	v = board[koef]
	if v !='':
		for i in range(3): #Check gorizontals (Проверка горизонталей)
			if v == board[koef+1] and v == board[koef+2]:
				win_chek = True
				if terner == False:
					print(f'WIN {x}')
				else:
					print(f'WIN {o}')
				break
		koef += 3
	for i in range(3): #Check verlicals (Проверка вертикалей)
		v = board[i]
		if v !='':
			if v == board[i+3] and v == board[i+6]:
				win_chek = True
				if terner == False:
					print(f'WIN {x}')
				else:
					print(f'WIN {o}')
				break
	if board[0] != '': #Check diagonal 1 (Проверка диагонали 1)
		if board[0] == board[4] and board == board[8]:
			win_chek = True
			if terner == False:
				print(f'WIN {x}')
			else:
				print(f'WIN {o}')
	if board[2] != '': #Check diagonal 2 (Проверка диагонали 2)
		if board[0] == board[4] and board == board[6]:
			win_chek = True
			if terner == False:
				print(f'WIN {x}')
			else:
				print(f'WIN {o}')
	if counter_draw == 9: #Check draw (Проверяет ничью)
		win_chek = True
	counter_draw += 1
	print(board[0],board[1],board[2]) #Show board (Выводит доску)
	print(board[3],board[4],board[5])
	print(board[6],board[7],board[8]) 

print('END')