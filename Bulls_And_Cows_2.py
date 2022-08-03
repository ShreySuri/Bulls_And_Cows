def unique(list_1):
    length = len(list_1)
    check = True
    for i in range (0, length):
        for j in range (0, length):
            if list_1[i] == list_1[j] and i != j:
                check = False
            else:
                toggle_1 = True
    return(check)
            

import random

num_list = [0, 0, 0, 0]
while unique(num_list) == False:
    x = random.randint(0, 9)
    num_list.append(x)
    num_list.pop(0)

game = True

while game == True:
    check = False
    while check == False:
        print("")
        user_num = input(print("Enter a 4-digit **unique** code. If you would like some examples, type 'example'. "))
        if user_num == "example" or user_num == "EXAMPLE":
            while unique(x_list
            if x < 10:
                print("000%s" % x)
            elif x < 100:
                print("00%s" % x)
            elif x < 1000:
                print("0%s" % x)
            else:
                print(x)
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

    for i in range (0, 4):
        for j in range (0, 4):
            if num_list[i] == user_list
        

    
