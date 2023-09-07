birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + 'is the birthday' + name)

    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
# 字典学习
# 第一题
# spam = {
#     '1h': 'bking',
#     '6c': 'wqueen',
#     '2g': 'bbishop',
#     '5h': 'bqueen',
#     '3e': 'wking'}
#
# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# for i in myCat.items():
#     print(i)
# print(myCat.get("color",0))
# myCat.setdefault("name","liu")
# print(myCat)

# 输出每个字符出现的个数
# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for i in message:
#     count.setdefault(i, 0)
#     count[i] += 1
# pprint.pprint(count)


# list=["A","b","A","c","A","b","d","e","c"]
# list1=[]
# count={}
# for i in list:
#     count.setdefault(i,0)
#     count[i]+=1

# 格式化字符串
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end="\t")
#     print()

# 1、格式的字符串（即%s）与被格式化的字符串（即传入的值）必须按照位置一一对应
# ps：当需格式化的字符串过多时，位置极容易搞混
print('%s asked %s to do something' %
      ('lsj', 'lili'))  # lsj asked lili to do something
print('%s asked %s to do something' %
      ('lili', 'lsj'))  # lili asked lsj to do something

# 2、可以通过字典方式格式化，打破了位置带来的限制与困扰
print('我的名字是 %(name)s, 我的年龄是 %(age)s.' % {'name': 'lsj', 'age': 18})

kwargs = {'name': '刘易灵', 'age': 18}
print('我的名字是 %(name)s, 我的年龄是 %(age)s.' % kwargs)
# format
# lsj asked lili to do something
print('{} asked {} to do something'.format('lsj', 'lili'))
print('{} asked {} to do something'.format('lili', 'lsj'))

# 使用索引
# 使用索引取对应位置的值
print('{0}{0}{1}{0}'.format('x', 'y'))  # xxyx

# 使用关键字参数
print('我的名字是 {name}, 我的年龄是 {age}.'.format(age=18, name='lsj'))

kwargs = {'name': 'lsj', 'age': 18}
print('我的名字是 {name}, 我的年龄是 {age}.'.format(**kwargs))  # 使用**进行解包操作

spam = {'name': 'limiting', 'age': 30}

print('我的名字是 %(name)s,我的年龄是 %(age)d' % spam)




