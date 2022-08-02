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
for i in range (0, 4):
    x = random.randint(0, 9)
    num_list.append(x)


game = True

while game == True:
    counter = 0
    while counter != 4:
        print("")
        user_num = input(print("Enter a 4-digit code. If you would like an example, type 'example'."))
        if user_num == "example":
            print("")
            for i in range (0, 10):
                ex_list = []
                for i in range (0, 4):
                    x = random.randint(0, 9)
                    ex_list.append(x)
                print(ex_list)
        else:
            num_list = convert(float(user_num))
            counter = 0
            for i in range (0, 4):
                for j in range (0, 10):
                    if num_list[i] == j:
                        counter = counter + 1
                    else:
                        toggle = True
