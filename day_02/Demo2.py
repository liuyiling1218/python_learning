
# 第一题

import random


def foo(spam):
    spam = ', '.join(spam[:-1]) + ', and ' + spam[-1]
    print(spam)
    return spam


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    foo(spam)

# 第二题
lst = []
for i in range(10):
    span = random.randint(0, 1)
    spam = str(span)
    if spam == "0":
        spam1 = spam.replace(spam, "T")
        lst.append(spam1)
    else:
        spam2 = spam.replace(spam, "H")
        lst.append(spam2)
print(lst)

# N = 100 * 10000
# number_of_streaks = 0
# same_count = 0
# prev = random.randit(0, 1)
# for i in range(1, N):
#     cur = random.randint(0, 1)
#     if prev == cur:
#         sanme_count += 1
#     else:
#         prev = cur
#         sanme_count = 0
#     if same_count == 5:
#         number_of_streaks += 1
#         sanme_count = 0


# 第三题

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# for i in grid:
#     for j in i:
#         print(j,end=" ")
#     print()
#
for o in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][o],end='  ')
    print()


