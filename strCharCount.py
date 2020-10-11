# Нужно написать функцию, которая будет считать сколько раз символ встречается в строке.
# Например, в строке "Денис даёт нам классные задачки, которые помогут нам найти лучшую работу!" символ "е" встречается 3 раза.
# Вероятно, Вам поможет FOR

def stringcharcount(a, b):
    c = 0
    for number in b:
        if a in number:
            c += 1

    return c


x = input("Enter your string: ")
y = input("Enter your character: ")
z = stringcharcount(y, x)
print(z)
