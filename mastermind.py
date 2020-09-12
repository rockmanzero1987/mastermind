import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
num1 = 0
num2 = 0
num3 = 0
num4 = 0

def draw_num(draw):
	random.shuffle(list)
	draw = list[0]
	list.remove(list[0])
	return draw

num1 = draw_num(num1)
num2 = draw_num(num2)
num3 = draw_num(num3)
num4 = draw_num(num4)

number = [num1, num2, num3, num4]

def compare(a):
	if number[a] == int(num[a]):
		display.append(2)
	elif int(num[a]) in number:
		display.append(1)
	else:
		display.append(0)

while True:
	num = input('Input: ')
	if len(num) != 4:
		print('Error')
	else:
		display =[]
		compare(0)
		compare(1)
		compare(2)
		compare(3)
		if display == [2, 2, 2, 2]:
			print('Right!')
			break
		print(display)