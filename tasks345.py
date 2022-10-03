# 3 Напишите функцию to_dict(lst), которая принимает аргумент
# в виде списка и возвращает словарь, в котором каждый
# элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут
# соответствовать правилам задания ключей в словарях.


from random import *
some_list = [1, 5, 7, 9, 3]


def to_dict(lst):
    return {x: x for x in lst}


print(to_dict(some_list))

#########################################################################################

# 4. Иван решил создать самый большой словарь в мире.
#  Для этого он придумал функцию biggest_dict(**kwargs),
#  которая принимает неограниченное количество параметров
# «ключ: значение» и обновляет созданный им словарь my_dict,
#  состоящий всего из одного элемента «first_one» со значением
#  «we can do it». Воссоздайте эту функцию.

myDict = {"first_one": "we can do it"}


def biggest_dict(**kwargs):
    for i in kwargs.keys():
        myDict[i] = kwargs[i]


biggest_dict(file="ind.txt", name="Alex", fix="fix")  # .....)


print(myDict)

###############################################################################################

# 5. Дана строка в виде случайной последовательности чисел от 0 до 9.

# Требуется создать словарь, который в качестве ключей будет принимать данные числа
# (т. е. ключи будут типом int), а в качестве значений – количество этих
# чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.


someStr = ""
n = 10

for i in range(100):
    someStr += str(randint(0, n-1))


def count_it(sequence):
    fullDict = {}
    for i in range(n):
        fullDict[i] = 0
    for i in sequence:
        fullDict[int(i)] += 1
    print(fullDict)
    resultDict = {}
    for i in range(3):
        keyMax = 0
        for j in fullDict.keys():
            # get на случай, если fullDict[0] уже не будет существовать
            if fullDict.get(keyMax, 0) < fullDict[j]:
                keyMax = j
        resultDict[keyMax] = fullDict[keyMax]
        fullDict.pop(keyMax)
    return resultDict


print(count_it(someStr))
