import random

span = [i for i in range(10) if i % 2 != 0]
print(type(span))
# 集合
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
c = [5, 6, 7, 8, 9]
print(a - b)
my_str = "MyABCnameABCisABCliuyiling"
print(my_str.split("ABC"))

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# 元组操作
data = range(1, 11)
# tuple() 将列表转换为元组
tupleName = tuple(data)
# len()返回元组的长度
print(len(tupleName))
# min()返回元组中最小的值
print(min(tupleName))
# max()返回元组中最大的值
print(max(tupleName))

inv = {'name': 'liuyiling', 'age': 18}
inv.setdefault('number', 123456)
print(inv)


# 装饰器
def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator' + message)
        func()

    return wrapper


@my_decorator
def greet():
    print('hello world')


greet('刘易灵')


# 示例2
def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)

    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('刘易灵')


# 示例三
def outer(func):
    def inner(a1, a2):
        print("==== start =====")
        r = func(a1, a2)
        print("==== end ====")
        return r

    return inner


@outer
def faa(a1, a2):
    print("普通函数中的功能")


# ============= 执行结果 ================
faa("a", "b")

