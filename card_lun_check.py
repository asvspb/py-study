card = 4790043056261726


def card_checker(x):
    card_arr = [int(i) for i in str(card)]
    sum_a = []
    for _i, _v in enumerate(card_arr):
        if int(_i) % 2 == 0:
            if (int(_v) * 2) < 10:
                sum_a.append(int(_v) * 2)
            else:
                sum_a.append(sum(int(_v) for _v in str(int(_v) * 2)))
        else:
            sum_a.append(int(_v))
    if sum(sum_a) % 10 == 0:
        print(f'Номер карты действителен: {card}')
    else:
        print(f'Номер карты не действителен: {card}')


card_checker(card)
