# 次回は重複している部分を関数にする
import random as r

min_num = 1
max_num = 100
continuous = False

num_first = r.randint(min_num, max_num)
num_second = r.randint(min_num, max_num)

input_disp = str(num_first) + '+' + str(num_second) + '='
answer = input(input_disp)
answer_num = int(answer)

if answer_num == (num_first + num_second):
    print('correct')

    res = input('Do you want to continue ? y/n ')

    if res == 'y':

        while continuous == False:

            num_first = r.randint(min_num, max_num)
            num_second = r.randint(min_num, max_num)
            input_disp = str(num_first) + '+' + str(num_second) + '='
            answer = input(input_disp)
            answer_num = int(answer)
            if answer_num == (num_first + num_second):
                print('correct')
                res = input('Do you want to continue ? y/n ')
                if res == 'y':
                    continue
                else:
                    print('Thank you !')
                    continuous = True
            else:
                print('incorrect')

    else:
        print('Thank you !')

else:
    print('incorrect')
