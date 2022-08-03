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
            list_2.append("0")
        list_2.reverse()
        return(list_2)
    elif len(list_2) == 2:
        list_2.reverse()
        for i in range (0, 2):
            list_2.append("0")
        list_2.reverse()
        return(list_2)
    elif len(list_2) == 3:
        list_2.reverse()
        for i in range (0, 1):
            list_2.append("0")
        list_2.reverse()
        return(list_2)
    elif len(list_2) == 4:
        return(list_2)
    else:
        return(None)

import random

num_list = [0, 0, 0, 0]
while unique(num_list) == False:
    x = random.randint(0, 9999)
    x = str(x)
    num_list = list_format(x)


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
                    x = str(x)
                    ex_list = list_format(x)
                str_1 = ""
                for i in range (0, 4):
                    str_1 = "%s%s" % (str_1, ex_list[i])
                print(str_1)
        else:
            user_list = list_format(user_num)
            if user_list == None:
                check = False
            elif unique(user_list) == False:
                check = False
            else:
                check = True


    
