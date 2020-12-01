# sa = 10
# sb = 20
# sc = 30
#
# # sa = int(input())
# # sb = int(input())
# # sc = int(input())
# aorborc = 3
# print(aorborc)
# print(sc)
# sc = 0
# print(sa, sb, sc)
#




# while sa != 0 or sb != 0 or sc != 0:
#
#     if sa == 0:
#         aorborc = 2
#         b = sb - 1
#         print(aorborc)
#         print(b)
#         sb = sb - b
#         print(sa, sb, sc)
#
#     else:
#         aorborc = 1
#         a = sa - 1
#         print(aorborc)
#         print(a)
#         sa = sa - a
#         print(sa, sb, sc)
#
#
#     if aorborc == 1:
#         a = int(input())
#         sa = sa - a
#         print(sa, sb, sc)
#     elif aorborc == 2:
#         b = int(input())
#         sb = sb - b
#         print(sa, sb, sc)






# max_ = int(input())
# number = int(input())
#
# for i in range(number):
#     row = input()
#     if len(row) <= max_:
#         print(row)
#     else:
#         print(row[:max_ - 3] + '...')


# n = int(input())
# chess = 'ABCDEFGHI'
# for i in range(n, 0, -1):
#     for j in range(n):
#         print(chess[j] + str(i), end=' ')
#     print()
#



# whitelist = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
# flag = False
# username = input()
# for letter in username:
#     if letter not in whitelist:
#         flag = True
#         break
#
# if not flag:
#     print('OK')
# else:
#     print(f'Invalid character:{letter}')

# a = int(input())
# for i in range(a):
#     b = input()
#     if "Don't" in b or "don't" in b:
#         if b[:6] == "Don't" or "don't":
#             print(b[6:])
#     else:
#         print(b)






# word = input()
# min_ = max_ = word
# while word != 'stop':
#     if len(word) < len(min_):
#         min_ = word
#     if len(word) > len(max_):
#         max_ = word
#     word = input()
# count = 0
# for letter in min_:
#     if letter in max_:
#         count += 1
# if count == len(min_):
#     print('YES')
# else:
#     print('NO')
#








# word1 = input()
# word2 = input()
# bulls = cows = 0
# for i in range(len(word1)):
#     if word1[i] == word2[i]:
#         bulls += 1
#     elif word1[i] in word2:
#         cows += 1
# print(bulls, cows)

# tiv = 1234567890
# tar = "abcdefghijklmnopqrstuvwxyz"
# num = int(input())
# for n in range(num):
#     word = input()
#     a = len(word)
#     for i in range(a + 1):
#         if word[i] == tar[i]:
#             print(1)
#



# a = int(input())
# for i in range(a + 1):
#     b = input()
#     if b[i:i + 5:1] == "Don't" or "don't":
#         b[i:i + 5:1] = ''
# print(b)




# num1 = input()
# num2 = input()
# set1 = set()
# set2 = set()
# c = 0
# for i in range(len(num1)):
#     if num1[i] == num2[i]:
#         c += 1
#     set1.add(num1[i])
#     set2.add(num2[i])
#
# print(c, len(set1) - len(set1 & set2))



# num = int(input())
# for n in range(num):
#     word = input()
#     a = len(word)
#     for i in range(a + 1):
#         if word[i:i + 3] == 'cat':
#             print(n + 1, i + 1)
#             break
#
#

# word = input()
# new_word = ''
# new_word1 = word[0::2]
# print(new_word1)
#
# word2 = 'abcd'
# print(word[:3])
