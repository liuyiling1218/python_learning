def collatz(number: int):
    if number % 2 == 0:
        integer = number // 2
    else:
        integer = 3 * number + 1
    print(integer)
    return integer


def foo():
    try:
        number = int(input("Enter number:"))
        while True:
            if number != 1:
                number = collatz(number)
    except ValueError:
        print("输入错误，请输入一个整数。")


print(foo())
