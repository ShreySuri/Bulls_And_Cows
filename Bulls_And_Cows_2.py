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
                    x = random.randint(0, 9)
                    ex_list.append(x)
                    ex_list.pop(0)
                ex_str = ""
                for j in range (0, 4):
                    ex_str = "%s%s" % (ex_str, ex_list[j])
                print(ex_str)
        else:
            user_list = list(user_num)
            total_val = []
            for i in range (0, 10):
                str_1 = str(i)
                total_val.append(str_1)
            for i in range (0, 4):
                for j in range (0, 10):
                    if user_list[i] == total_val[j]:
                        total_val[j] == "placeholder"
                        counter = counter + 1
                    else:
                        toggle = False

    for i in range (0, 4):
        for j in range (0, 4):
            if num_list[i] == user_list
        

    
