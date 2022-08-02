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
        user_num = input(print("Enter a 4-digit code. If you would like some examples, type 'example'. "))
        if user_num == "example" or user_num == "EXAMPLE":
            print("")
            for i in range (0, 10):
                ex_list = []
                for i in range (0, 4):
                    x = random.randint(0, 9)
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

        
        

    
