def convert(int_1):
	power = 1
	list_1 = []
	while int_1 >= 10 ** power:
		power = power + 1
	while power > 0:
		power = power - 1
		divisor = 10 ** power
		rem = int_1 % divisor
		quotient = int((int_1 - rem)/divisor)
		list_1.append(quotient)
		int_1 = rem
	return(list_1)


import random

num_list = []
known_list = []

for i in range (0, 4):
	x = random.randint(0, 9)
	num_list.append(x)
	known_list.append("X ")

game = True
turn_count = 0

while game == True:
	
	input_1 = 0
	while input_1 % 1 != 0 or input_1 < 1 or input_1 > 9999:
		print("")
		input_1 = input(print("Enter a 4 digit  number. "))
		input_1 = float(input_1)
	user_num = int(input_1)

	user_num_list = convert(user_num)

	counter = 0
	for i in range (0, 4):
		if num_list[i] == user_num_list[i]:
			x = num_list[i]
			string_1 = "%s " % x
			counter = counter + 1
		else:
			toggle = True

	print(known_list)
	turn_count = turn_count + 1

	if counter == 4:
		game = False
	else:
		toggle = False

