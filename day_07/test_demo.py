# map函数
def double(bonus):
    return bonus * 2


bonuses = [100, 200, 300]
iterator = map(double, bonuses)
print(list(iterator))
# 匿名函数
sync = map(lambda x: x * 2, [100, 200, 300])
print(list(sync))

## 匿名函数 示例2
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]

TAX = 0.1
carts = map(lambda x: [x[0], x[1] * 2], carts)
# 装饰器,示例1
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('='*20)
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)
greet('hello world')
# 装饰器，示例2
def outer(func):
    def inner(*args,**kwargs):
        print  ("=" * 20)
        print ("装饰器 start")
        func(*args,**kwargs)
        print ("装饰器，end")

    return inner

@outer
def fun1(a1):
    print ("fun1 一个参数")

@outer
def fun2(a1,a2):
    print ("fun2 两个参数")

@outer
def fun3(*args,**kwargs):
    print (args)
    print (kwargs)

ret1 = fun1("f1_a1")
ret2 = fun2("f2_a1","f2_a2")
ret3 = fun3("f3_a1","f3_a3",k1="k1",k2="k2")

#装饰器 示例3(添加多个装饰器)
def outer(func):
    def inner(*args,**kwargs):
        print ("="*20)
        print ("装饰器outer start")
        r = func(*args,**kwargs)
        print ("装饰器outer end")
        return r
    return inner

def outer_1(func):
    def inner(*args,**kwargs):
        print ('='*20)
        print ("装饰器outer_1 start")
        r = func(*args,**kwargs)
        print ("装饰器outer_1 end")
        return r
    return inner

@outer
@outer_1
def fun1(a1):
    print ("fun1")
fun1("多个装饰器")




