import sys
import random

min_num = int(input("type the minimum number"))
max_num = int(input("type the max number"))


if(min_num >= max_num) : 
    print('minimum number has to be smaller than max number')
    sys.exit()

answer = random.randint(min_num, max_num)

for i in range(5): 
    guess = int(input('guess the number'))
    if(guess == answer) :
        print('Coreect!')
        break
    if(i ==  4):
        print("Game over! The answer is " + str(answer))
    else:
        print('Wrong number! Try again!')