import random

num_list = []
for i in range (0, 4):
    x = random.randint(0, 9)
    num_list.append(x)


game = True

while game == True:
    user_list_len = 0
    while user_list_len != 4:
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
            num_list = 
