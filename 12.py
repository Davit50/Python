# line = input()
# n = int(line[:4])
# suma = int(line[4:])
# my_suma = 0
# wrong = list()
# for i in range(n):
#     line = input()
#     count = int(line[8:12])
#     cost = int(line[:7])
#     another_sum = int(line[13:])
#     if cost * count != another_sum:
#         wrong.append(i + 1)
#     my_suma += cost * count
# print(suma - my_suma)
# for i in wrong:
#     print(i, end=' ')
#
#
#
#
#
#
#
#



# j = int(input())
# list_ = list()
# set__ = set()
# finish = []
# for a in range(j):
#     row = input()
#     list_.append(row)
# n = int(input())
# for b in range(j):
#     row = input()
#     set__.add(row)
#     for afg in set__:
#         if afg[b] in list_[b]:
#             finish.append(list_[b])
# for end in finish:
#     print(end)
#
#



# n = int(input())
# a = b = c = 1
# list1 = []
# list1.append(a)
# list1.append(b)
# list1.append(c)
#
# for i in range(n):
#     a = a + b + c
#     list1.append(a)
#     b = a + b + c
#     list1.append(b)
#     c = a + b + c
#     list1.append(c)
# list2 = list1[:n]
# for asd in list2:
#     print(asd, end=' ')


# n = int(input())
# list1 = list()
# for i in range(n):
#     a = int(input())
#     list1.append(a)
#
# for d in list1:
#     print(d)
# print()
# for d2 in list1:
#     print(d2 * 3)




# n = int(input())
# list1 = list()
# for i in range(n):
#     row = input()
#     list1.append(row)
# N = int(input()) - 1
# for i in range(n):
#     if len(list1[i]) > N:
#         print(list1[i][N], end='')
























# list1 = list()
# list2 = []
# list3 = [1, 2, 3, 'a', [1, 2, 3]]
# list4 = [10, 11, 12]
#
#
# print(list3 + list4)
#
#
# for i in range(5):
#     list1.append(str(100 * i))
#
# print(list1)
#
# for item in list1:
#     print(item)
#
#
# for j in range(len(list1)):
#     print(list1[j])
#
# print(list3[-1])
# print(list1)
# print(list1[1:3])
#
#
# print(list('abcd'))
#
#
#
# print(list1)
# list1.extend('abcd') # "a", "b", "c", "d"
# print(list1)
# list1.append('abcd') # "abcd"
# print(list1)