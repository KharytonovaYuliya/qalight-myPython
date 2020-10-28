def elementarno(a):
    c = 0
    for number in a:
        c += int(number)
        print(int(number))

    return print("Result is " + str(c))


elementarno(input("Enter a number: "))