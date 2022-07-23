import random

num_list = []
known_list = []

for i in range (0, 4):
	x = random.randint(0, 9)
	y = str(x)
	num_list.append(y)
	known_list.append("X ")

game = True

while game == True:
	
	input_1 = 0
	while input_1 % 1 != 0 or input_1 < 1 or input_1 > 9999:
		print("")
		input_1 = input(print("Enter a 4 digit  number. "))
		input_1 = float(input_1)
	user_num = int(input_1)

	user_num_list = convert(user_num)