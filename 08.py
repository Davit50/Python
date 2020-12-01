# a = int(input())
# res = 0
# for i in range(a):
#     b = int(input())
#     if i % 2 != 0:
#         res = res - b
#     else:
#         res = res + b
# print(res)



# n = int(input())
# i = 1
# for line in range(1, n):
#     for _ in range(line):
#         print(i, end=' ')
#         i += 1
#         if i > n:
#             break
#     print()
#     if i > n:
#         break
# if i == 1:
#     print(1)
# if n == 2:
#     print(2)

# col = int(input()) + 1
# row = int(input()) + 1
# for i in range(1, row):
#     for j in range(1, col):
#         print(j / i, end='\t')
#     print()





# n = int(input())
# max_ = -1
# for road in range(n):
#     min_ = 1000000
#     m = int(input())
#     for tunnel in range(m):
#         hight = int(input())
#         if hight < min_:
#             min_ = hight
#     if min_ > max_:
#         max_ = min_
#         max_road = road + 1
#
#
# print(max_road, max_)










# summa = 0
# j = 220
# for i in range(1, 10000):
#     if j % i == 0:
#         summa += i
# print(summa - j)







# n = int(input())
# for num in range(1, n):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
#
#
#
#
#


#
#
# # col = int(input())
# # row = int(input())
# # s = input()
# # for i in range(row):
# #     for j in range(col):
# #         if i == 0 or j == 0 or i == row - 1 or j == col - 1:
# #             print(s, end='')
# #         else:
# #             print("", end=' ')
# #     print()
# #
#
#
#
#
#
#
#
#
#
#
# # row = int(input())
# # col = int(input())
# # s = input()
# # for i in range(row):
# #     for j in range(col):
# #         if i == 0 or j == 0 or i == row - 1 or j == col - 1:
# #             print(s, end='')
# #         else:
# #             print("", end=' ')
# #     print()
#
#
# # row = int(input())
# # col = int(input())
# # s = input()
# # for i in range(row):
# #     for j in range(col):
# #         if i == 0 or j == 0 or i == row - 1 or j == col - 1:
# #             print(s, end=' ')
# #         else:
# #             print(" ", end=' ')
# #     print()
#
#
#
# # n = int(input())
# # for i in range(n):
# #     a = int(input())
# #     for j in range(a):
# #         b = int(input())
# #
#
#
#
#
#
#
#
# # num = int(input()) + 1
# # for i in range(1, num):
# #     print(i, end=' ')
# #     for j in range(1, num):
# #
# #         print('')
#
#
#
#
#
#
# # n = int(input())
# #         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
# #             print(s, end=' ')
# #         else:
# #             print(" ", end=' ')
# #     print('')
#
#
#
# # n = int(input())
# # num = 1
# # for row in range(1, n + 1):
# #     for col in range(1, row + 1):
# #         print(num, end=' ')
# #         num += 1
# #     print('')
#
#
#
#
# # n = int(input()) + 1
# # for i in range(1, n, 1):
# #     for j in range(1, n, 1):
# #         print(i, '*', j, end =' ')
# #         print('=', i * j)
#
