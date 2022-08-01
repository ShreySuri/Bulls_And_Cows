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

def listToString(s):
    str1 = "" 
    for i in s:
          str1 += i 
    return(str1)

def repeat(list_1):
    x = len(list_1) - 1
    counter = 0
    for i in range (0, x):
          for j in range (i, x):
              if list_1[i] == list_1[j + 1]:
                   counter = counter + 1
              else:
                   counter = counter + 0
    return(counter)
               

import random

num_list = [0, 0, 0, 0]
repeat_count = repeat(num_list)

while repeat_count > 1:
     for i in range (0, 4):
          x = random.randint(0, 9)
          num_list.append(x)
          num_list.pop(0)
     repeat_count = repeat(num_list)

print(num_list)

game = True
turns = 0

while game == True:
     
     input_1 = 0
     while input_1 % 1 != 0 or input_1 < 1 or input_1 > 9999:
          print("")
          input_1 = input(print("Enter an integer from 0 to 9999 inclusive. "))
          input_1 = float(input_1)
     user_num = int(input_1)

     user_num_list = convert(user_num)
     length = len(user_num_list)
     if length < 4:
          length = 4 - length
          user_num_list.reverse()
          for i in range (0, length):
               user_num_list.append(0)
          user_num_list.reverse()
     else:
          toggle = False

     cows = 0
     bulls = 0

     for i in range (0, 4):
          for j in range (0, 4):
               if user_num_list[i] == num_list[j]:
                    cows = cows + 1
               else:
                    toggle = True

     for k in range (0, 4):
          if user_num_list[k] == num_list[k]:
                bulls = bulls + 1
          else:
                bulls = bulls + 0

     cows = cows - bulls - repeat_count

     if bulls == 4:
          game = False
     else:
          toggle = False

     turns = turns + 1

     print("")
     print("%s Bulls, %s Cows" % (bulls, cows))

print("")
print("You won! It took you %s guesses. " % turns)
