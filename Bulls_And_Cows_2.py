

import random

num_list = []
for i in range (0, 4):
    x = random.randint(0, 9)
    num_list.append(x)


game = True

while game == True:
    user_num = 0.5
    while user_num % 1 != 0 or user_num < 0 or user_num > 9999:
        print("")
        user_num = input(print("Enter a 4-digit code. If you would like some examples, type 'example'. "))
        if user_num == "example":
            print("")
            for i in range (0, 10):
                ex_list = []
                for i in range (0, 4):
                    x = random.randint(0, 9):
                    ex_list.append(x)
                print(ex_list)
        else:
            user_list = list(user_num)
