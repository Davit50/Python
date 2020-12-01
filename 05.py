# summa = int(input())
# while summa != 0:
#     a = int(input())
#     if a < summa and (a == 1 or a == 2 or a == 3):
#         summa = summa - a
#     print(summa)
# print('0')

#
# sa = int(input())
# sb = int(input())
# sc = int(input())
# while sa != 0 or sb != 0 or sc != 0:
#     aorborc = int(input())
#     if aorborc == 1:
#         a = int(input())
#         sa = sa - a
#     elif aorborc == 3:
#         c = int(input())
#         sc = sc - c
#     else:
#         b = int(input())
#         sb = sb - b
#     print(sa, sb, sc)
#
#

# sa = int(input())
# sb = int(input())
# while sa != 0 or sb != 0:
#     aorb = int(input())
#     if aorb == 1:
#         a = int(input())
#         sa = sa - a
#     else:
#         b = int(input())
#         sb = sb - b
#     print(sa, sb)







#n = int(input())
#count = 0
#while n != 1:
    #if n % 2 == 0:
        #n //= 2
    #else:
        #n -= 1
    #count += 1
#print(count)





#d = int(input())
#m = int(input())
#y = int(input())
#c = y // 100
#y = y % 100
#if m >= 3:
    #m = m - 2
#else:
    #m = m + 10
#f = d + ((13 * m - 1) // 5 ) + y + (y // 4 + c // 4 - 2 * c + 777)
#print(f % 7)






#a = int(input())
#while a > 0:
    #b = a % 4
    #if b == 0:
        #b = 2
    #print(b)
    #a = a - b
    #print(a)
    #if a == 0:
        #print('You lose')
    #else:
        #b = 0
        #while not (1 <= b <= 3 and b <= a):
            #b = int(input())
        #a = a - b
        #print(a)
        #if a == 0:
            #print('You win')








#summa = int(input())
#while summa != 0:
    #a = int(input())
    #if a < summa and (a == 1 or a == 2 or a == 3):
        #summa = summa - a
    #print(summa)

 






        #summa = int(input())
        #a = int(input())
        #while summa != 0:
            #if a < summa and (a == 1 or a == 2 or a == 3):
                #summa = summa - a
                #print(summa)
                #a = int(input())
            #else:
                #if summa - a != 0:
                    #print(summa)  
                    #a = int(input())
                #else:
                    #summa = 0
                    #print(summa)



#a = int(input())
#Input = int(input())
#while a > 0:
    #Output = a - Input
    #print(Output)
    #if (Input == 1 or Input == 2 or Input == 3) and Input > a:
        #Input = int(input())
        #a = Output
    #else:
        #print(a)












#summa = 10
#print(summa)
#PC = 8
#while summa != 0:
    #summa = PC
    #PC -= 4
    #print('Computer', summa)
    #sub = int(input())
    #if sub < summa and (sub == 1 or sub == 2 or sub == 3):
        #summa = summa - sub
        #print('You', summa)
    #else:
        #print(summa)
        #sub = int(input())
        #summa = summa - sub
        #print('You', summa)        

#print('You lose!!!')





#a = int(input())
#num1 = 1
#num2 = 1
#num = 1
#print(num)
#while a >= num2:
    ##num1, num2 = num2, num
    #print(num)
    #num = num1 + num2
    #num1 = num2
    #num2 = num

#print('Բարի գալուստ ինտերնետ-բանկինգ')
#print('Մեզ մոտ բացառիկ տոկոսադրույքներ են։')
#print('Մինչև 10 հազար ₽ ներառյալ ավանդների համար եկամուտը կկազմի 10%,')
#print('մինչև 100 հազար ներառյալ ավանդների համար՝ 20%,')
#print('100 հազարից ավել՝ 30%:')
#print('Ի՞նչ գումարի չափով եք ցանկանում ավանդ կատարել:')
#money = float(input())
#if money <= 10000:
    #money *= 1.1
#elif money <= 100000:
    #money *= 1.2    
#elif money > 100000:
    #money *= 1.3    
#print('Դուք ստանում եք', money, ' ₽, շնորհավորում ենք։')