card = 4790043056261726


def card_checker(x):
    card_arr = [int(i) for i in str(card)]  # ['1','3','5','7','9']...
    sum_a = []  # переменная с суммой
    for _i, _v in enumerate(card_arr):  # цикл перебора элементов списка для суммы
        if int(_i) % 2 == 0:  # проверка на четность
            if (int(_v) * 2) < 10:  # поиск число*2 меньше 10
                # добавляем его в переменную для суммирования
                sum_a.append(int(_v) * 2)
            else:
                # если число*2 больше 10, складываем его
                sum_a.append(sum(int(_v) for _v in str(int(_v) * 2)))
        else:
            # если число не четное, то добавляем его сразу
            sum_a.append(int(_v))
    if sum(sum_a) % 10 == 0:  # суммирование и проверка значений
        print(f'Номер карты действителен: {card}')
    else:
        print(f'Номер карты не действителен: {card}')


card_checker(card)
