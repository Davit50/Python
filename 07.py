# line = input()
# count = 0
# first_cat_number = -1
# number_of_cats = 0
# while line != 'STOP':
#     count += 1
#     if 'cat' in line or 'Cat' in line:
#         number_of_cats += 1
#         if first_cat_number == -1:
#             first_cat_number = count
#     line = input()
# print(number_of_cats, first_cat_number)

n = int(input())
for num in range(1, n):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)





# cat = 0
# flag = False
# text = input()
# count = 1
# while text != 'STOP':
#     if ('cat' in text or 'Cat' in text) and not flag:
#         cat = count
#         flag = True
#     text = input()
#     count += 1
# if flag:
#     print(cat)
# else:
#     print(-1)






# compass = 'north'
# count = -1
# command = ''
# end = 'false'
# x = int(input())
# y = int(input())
# x1 = 0
# y1 = 0
# while command != 'stop':
#     command = input()
#     if end == 'false':
#         count += 1
#         if x == x1 and y1 == y and end == 'false':
#             end = 'true'
#         else:
#             if command == 'forward':
#                 go = int(input())
#                 if compass == 'north':
#                     y1 += go
#                 elif compass == 'south':
#                     y1 -= go
#                 elif compass == 'east':
#                     x1 += go
#                 elif compass == 'west':
#                     x1 -= go
#             elif command == 'turn':
#                 if compass == 'north':
#                     compass == 'south'
#                 elif compass == 'south':
#                     compass == 'north'
#                 elif compass == 'east':
#                     compass == 'west'
#                 elif compass == 'west':
#                     compass == 'east'
#             elif command == 'right':
#                 if compass == 'north':
#                     compass == 'east'
#                 elif compass == 'south':
#                     compass == 'west'
#                 elif compass == 'east':
#                     compass == 'south'
#                 elif compass == 'west':
#                     compass == 'north'
#             elif command == 'left':
#                 if compass == 'north':
#                     compass == 'west'
#                 elif compass == 'south':
#                     compass == 'east'
#                 elif compass == 'east':
#                     compass == 'north'
#                 elif compass == 'west':
#                     compass == 'south'
# print(count)
# print(compass)



# -2
# 9
# forward
# 9
# left
# forward
# 2
# turn
# forward
# 17
# stop


# num = 0
# line_with_cat = -1
# text = input()
# while text != 'STOP':
#     num += 1
#     if ('cat' in text or 'Cat' in text) and line_with_cat == -1:
#         line_with_cat = num
#     text = input()
#
# print(line_with_cat)




# friend = 'Eastasia'
# enemy = 'Eurasia'
# n = int(input())
# for _ in range(n):
#     question = input()
#     if question == 'Who is the enemy?':
#         print(enemy)
#     elif question == 'Who is a friend?':
#         print(friend)
#     elif question == 'Change':
#         friend, enemy = enemy, friend
#
#




# x0, y0 = int(input()), int(input())
# x = y = 0
# command = input()
# direction = 'north'
# while x != x0 and y != y0 and command != 'stop':
#     if command == 'left':
#         direction = (direction - 1) % 4
#     elif command == 'turn':
#         direction = (direction + 2) % 4
#     elif command == 'right':
#         direction = (direction + 1) % 4
#     elif command == 'forward':
#         steps = int(input())
#     if direction == 0:
#         y += steps
#     elif direction == 1:
#         x += steps
#     elif direction == 2:
#         y -= steps
#     elif direction == 3:
#         x -= steps






# a = int(input())
# count = 0
# while a != count:
#     count += 1
#     cat = input()
#     if 'cat' in cat or 'Cat' in cat:
#         flag = True
#     if 'dog' in cat or 'Dog' in cat:
#         flag = False
# if flag:
#     print('MEOW')
# if not flag:
#     print('NO')












# a = input()
# count = 1
# c = -1
# row = 0
# while a != 'STOP':
#     a = input()
#     count += 1
#     if 'cat' in a or 'Cat' in a:
#         c = count
#         row += 1
#         break
# print(row, end=' ')
# print(c)
#
#
#
#





# a = int(input())
# summa = 0
# flag = 0
# while summa != a:
#     summa += 1
#     while flag == 0:
#         question = input()
#         if question == 'Change':
#             question = input()
#             flag = 1
#             break
#         elif question == 'Who is the enemy?':
#             print('Eurasia')
#         elif question == 'Who is a friend?':
#             print('Eastasia')
#     while flag == 1:
#         question = input()
#         if question == 'Change':
#             flag = 0
#             question = input()
#             break
#         elif question == 'Who is the enemy?':
#             print('Eastasia')
#         elif question == 'Who is a friend?':
#             print('Eurasia')
#
#





# summa = int(input())
# a = int(input())
# while summa != 0:
#     if a < summa:
#         summa = summa - a
#         print(summa)
#         a = int(input())
#     else:
#         if summa - a != 0:
#             print(summa)
#             a = int(input())
#         else:
#             summa = 0
#             print(summa)
#


# count = 0
# flag = True
# summa = 0
# while summa != 10:
#     a = int(input())
#     summa += a
#     count += 1
#
# print(count)


# a = int(input())
# b = int(input())
# for i in range(a, b + 1, 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)







# a = int(input())
# c = False
# for i in range(0, a, 1):
#     b = input()
#     if 'Cat' in b or 'cat' in b:
#         c = True
#         break
# if c:
#     print('MEOW')
# else:
#     print('NO')
#
