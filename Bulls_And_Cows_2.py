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

def list_format(string):
    list_2 = list(string)
    if len(list_2) == 1:
        list_2.reverse()
        for i in range (0, 3):
            list
    

import random

x = [0, 0, 0, 0]
while unique(x) == False:
    x = random.randint(0, 9999)
    x = list_format(x)


print(num_list)
game = True

while game == True:
    check = False
    while check == False:
        print("")
        user_num = input(print("Enter a 4-digit **unique** code. If you would like some examples, type 'example'. "))
        if user_num == "example" or user_num == "EXAMPLE":
           for i in range (0, 10):
                ex_list = [0, 0, 0, 0]
                while unique(ex_list) == False:
                    x = random.randint(0, 9999)
                    x = list_format
        else:
            user_list = list(user_num)
            len_user_list = len(user_list)
            total_val = []
            counter = 0
            for i in range (0, 10):
                str_1 = str(i)
                total_val.append(str_1)
            for i in range (0, len_user_list):
                for j in range (0, 10):
                    if user_list[i] == total_val[j]:
                        total_val[j] == "placeholder"
                        counter = counter + 1
                    else:
                        toggle = False
            if counter == 4 and len_user_list == 4:
                check = True
            else:
                check = False


    
