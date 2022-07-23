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

num = 19921830913280
x = convert(num)
print(x)
