import random as r

min_num = 1
max_num = 100

num_first = r.randint(min_num, max_num)
num_second = r.randint(min_num, max_num)

input_disp = str(num_first) + '+' + str(num_second) + '='
answer = input(input_disp)
answer_num = int(answer)

if answer_num == (num_first + num_second):
    print('correct')
else:
    print('incorrect')
