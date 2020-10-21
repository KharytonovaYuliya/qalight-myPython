import random

def twolists():
    list1 = list([random.randint(0, 20) for i in range(5)])
    print(list1)
    list2 = list([random.randint(0, 20) for i in range(5)])
    print(list2)
    list3 = list()
    for number1 in list1:
        for number2 in list2:
            if number1 == number2:
                list3.append(number1)
    print(list3)


twolists()
