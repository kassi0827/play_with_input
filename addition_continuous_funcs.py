import random as r

# 初期の変数宣言
min_num = 1
max_num = 100
continuous = False

# メッセージ
correct = 'correct'
incorrect = 'incorrect'
want_to_continue = 'Do you want to continue ? y/n .. '
yes = 'y'
thank_you = 'Thank you !'


# 足し算を実行する関数
def make_addition(num_one, num_two):

    num_first = r.randint(num_one, num_two)
    num_second = r.randint(num_one, num_two)

    input_disp = str(num_first) + '+' + str(num_second) + '='
    answer = input(input_disp)
    answer_num = int(answer)
    return num_first, num_second, answer_num


result = make_addition(min_num, max_num)

if result[2] == (result[0] + result[1]):
    print(correct)

    res = input(want_to_continue)

    if res == yes:

        while continuous == False:

            make_addition(min_num, max_num)
            if result[2] == (result[0] + result[1]):
                print(correct)
                res = input(want_to_continue)
                if res == yes:
                    continue
                else:
                    print(thank_you)
                    continuous = True
            else:
                print(incorrect)

    else:
        print(thank_you)

else:
    print(incorrect)
