

import random

num_list = []
for i in range (0, 4):
    x = random.randint(0, 9)
    num_list.append(x)


game = True

while game == True:
    check = False
    while check = False:
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
            len_user_list = len(user_list)
            counter = 0
            for i in range (0, len_user_list):
                for j in range (0, 10):
                    if user_list[i] == j:
                        counter = counter + 1
                    else:
                        toggle = True
            if counter == 4 and len_user_list == 4:
                check = True
            else:
                toggle = False
