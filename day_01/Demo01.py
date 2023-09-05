def collatz(number: int):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


def foo():
    try:
        number = int(input("Enter number:"))
        while True:
            if number != 1:
                number = collatz(number)
    except ValueError:
        print("输入错误，请输入一个整数。")


if __name__ == '__main__':
    foo()
