# row = input()
# print(".", end='')
# for i in range(len(row)):
#     if row[i] == ">":
#         print(row[0], end='')
#     elif row[i] == "<":
#         print(row[0], end=' ')
#     elif row[i] == "V":
#         print(' ' * i, end=' ')
#         print(row[0])






step = int(input())
letter = input()
tox = ''
for i in range(len(letter)):
    if ord("A") <= ord(letter[i]) <= ord('Z'):
        text = chr((ord(letter[i]) - 65 + step) % 26 + 65)
    elif ord("a") <= ord(letter[i]) <= ord('z'):
        text = chr((ord(letter[i]) - 97 + step) % 26 + 97)
    else:
        text = letter[i]
    tox += text
print(tox)
# first = input()
# second = input()
# if first[-1] == "!":
#     if first[-2] == second[0]:
#         print('CORRECT')
#     else:
#         print('INCORRECT')
# else:
#     if first[-1] == second[0]:
#         print('CORRECT')
#     else:
#         print('INCORRECT')



# a = input()
# while a[0] == 'a' or a[0] == 'A':
#     a = input()







# a = input()
# if a[0] == 'a' or a[0] == 'A':
#     print('YES')
# else:
#     print('NO')

# word = input()
# for i in range(len(word)):
#     print(word[i] * 2, end='')



# text = input()
# num = int(input())
# if num == 1:
#     print(text[0])
#
# else:
#     num -= 1
#     if num > 0:
#         if len(text) > num:
#             print(text[num])
#         else:
#             print('ERROR')
#     elif num < 0:
#         print('ERROR')








# ord('tar')
# tiv


# chr(tiv)
# tar

# a = input()
# for _ in range(len(a) - 1):
#     print(ord(a[_]), end=', ')
# print(ord(a[-1]))

# print('\u2603')

# print(input()[-1])

# word = input()
# if len(word) < 5:
#     print('NO')
# else:
#     print(word[4])


# n = int(input())
# a = False
# if n < 1000000000:
#     while a != 1 and n < 1000000000:
#         a = int(str(n)[0])
#         n = n * a
#     print(n)



# text1 = input()
# text2 = text1[-1]
# while text1[-1] == text2[0]:
#     text1, text2 = text2, input()
# else:
#     print(text2)





# text = input()
# for i in range(len(text)):
#     print(text[i])







# text1 = input()
# text2 = text1[-1]
# while text1[-1] == text2[0]:
#     text1 = input()
#     text2 = input()
# else:
#     print(text2)
