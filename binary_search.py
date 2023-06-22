import random
# element = int(input("Длина массива: "))
element = 10
my_list = sorted([num for num in random.sample(
    range(1, element*2 + 1), element)])
