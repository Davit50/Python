# M = int(input())
# N = int(input())
# asd = set()
# for i in range(M):
#     m = input()
#     asd.add(m)
# for j in range(N):
#     n = input()
#     if n in asd:
#         print('YES')
#     else:
#         print('NO')

#
# a = int(input())
# set1 = set()
# set2 = set()
# for i in range(a):
#     s = int(input())
#     for j in range(s):
#         d = input()
#         if d in set1:
#             set2.add(d)
#         else:
#             set1.add(d)
# for a in set2:
#     print(a)




# for_ = int(input())
# count = 0
# set1 = set()
# set2 = set()
# for _ in range(for_):
#     text = input()
#     if text in set1 and text in set2:
#         count += 1
#     elif text in set1 and text not in set2:
#         count += 2
#         set2.add(text)
#     else:
#         set1.add(text)
# print(count)






# n = int(input())
# all = set()
# length = 0
# for j in range(n):
#     N = input()
#     all.add(N)
#     for i in all:
#         print(i)
#     if N == all[j]:
#         length += 2
# print(length)

# Ivanov
# Petrov
# Sidorov
# Petrov
# Ivanov
# Petrov









# m = set()
# n = int(input())
# for _ in range(n):
#     m.add(input())
# n = input()
# if n in m:
#     print('TRY ANOTHER')
# else:
#     print('OK')
#










# eng, ger = int(input()), int(input())
# eng_set = set()
# ger_set = set()
# for i in range(eng):
#     eng_set.add(input())
# for j in range(ger):
#     ger_set.add(input())
# if eng_set ^ ger_set:
#     print(len(eng_set ^ ger_set))
# else:
#     print('NO')









# # my_set1 = set()
# # print(my_set1)
# #
# # my_set2 = {'a', 'b', 'c', 'd', 'e', 'f', 123, 4.5}
# # print(my_set2)
# #
# # for item in my_set2:
# #     print(item)
# #
# # my_set1.add('abc')
# # my_set1.add(12)
# # print(my_set1)
#
# # remove, discard, pop
#
# # my_set1.discard('abc')
# # my_set1.remove('abc')
# # print(my_set1)
# # a = my_set1.pop()
# # print(a)
#
#










# my_set1 = {'a', 'b', 'c', 'd', 'e', 'f', }
# my_set2 = {'a', 2, 1, 'd', }
# print(my_set1)
# print(my_set2)

# # 2-y irar het ktpe           miavorum
# # union = my_set1.union(my_set2)
# union = my_set1 | my_set2
#
# print(union)
#
# #yndhanury ktpe 2i migic        hatum
# # intersection = my_set1.intersection(my_set2)
# intersection = my_set1 & my_set2
#
# print(intersection)
#
# # hanum
# #diff = my_set1.difference(my_set2)
# diff = my_set1 - my_set2
#
# print(diff)
#
# # iranc gumaric hanac nmanutyuny
# #symm_diff = union - intersection
# #symm_diff = my_set1.symmetric_difference(my_set2)
#
# symm_diff = my_set1 ^ my_set2
# print(symm_diff)
#
# #entabazmutyan stugum
# print(my_set2 <= my_set1)
#
#
# my_set = {'a', 'b', 'c'}
# for elem in my_set:
#     print(elem)