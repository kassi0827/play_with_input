word_one = input('しりとりゲーム.. ひらがなで単語を入力して下さい.. ')

if word_one[-1] == 'ん':
    word_one = input('「ん」から始まらない単語を入力して下さい.. ')


print('あなたが入力した言葉は', word_one)

word_two = input('しりとりゲーム.. 「' + word_one + '」続きをお願いします..')

if word_two[-1] == 'ん':
    print('「ん」で終わってしまっています')
elif word_two[0] == word_one[-1]:
    # 色付き文字の関数化を検討
    print('\033[31m' + word_one + '\033[0m', '\033[32m' +
          word_two + '\033[0m', 'OKです.. 次行きましょう..')
elif word_two[0] != word_one[-1]:
    print('しりとりになっていません')
