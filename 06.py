n = int(input())
len_ = 0
for i in range(1, n + 1):
    if(n % i == 0):
        len_ += 1
        print(i, end=' ')
print('')
if len_ == 2:
    print('PRIME')
else:
    print('NO')







#     *
#    ***
#   *****
#  *******
# *********
#
#
#
# num = int(input())
# for i in range(1, num + 1):
#     for j in range(1, num - i + 1):
#         j = '*'
#         print(' ', end="")
#     for j in range(i, 0, -1):
#         j = '*'
#         print(j, end="")
#     for j in range(2, i + 1):
#         j = '*'
#         print(j, end="")
#     print('')
#







# n = int(input())
# len_ = 0
# for i in range(1, n + 1):
#     if(n % i == 0):
#         len_ += 1
#         print(i, end=' ')
# print('\n')
# if len_ >= 2:
#     print('NO')
# else:
#     print('PRIME')
#
#
#
#



















#n = int(input())
#len_ = 0
#for i in range(1, n + 1):
    #if(n % i == 0):
        #len_ += 1
        #print(i, end=' ')
#print('\n')
#if len_ > 2:
    #print('NO')
#else:
    #print('PRIME')       




#n = int(input())
#res = 1
#for i in range(n, 0, -1):
    #res *= i
#print(res)





#c = float(input())
#count = 0
#while c < 22:
    #count += 1
    #c = float(input())
#count = count / 7
#print(int(count))
    



#p = 1
#for _ in range(6):
    #n = int(input())
    #if n != 0:
        #p *= n
#print(p)




#n = int(input())
#for i in range(n, -1, -1):
    #print('Seconds remaining:', i)
#print('start')



#n = int(input()) + 1
#for i in range(n):
    #print('Cube of number', i, 'is', i ** 3)




#text = input()
#n = int(input())
#for i in range(n):
    #print(text, sep='/n')
 








#n = int(input()) + 1
#for i in range(n):
    #print(i, end=' ')



#for i in range(10, 4, -2):
    #print('hello', i)





#print('a', 'b', 'c', sep='@', end='----')
#print('d', 'e', sep='\t')