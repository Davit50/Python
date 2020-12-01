


# a = int(input())
# res = 0
# for i in range(a):
#     h1 = int(input())
#     h2 = int(input())
#     res = h1 / h2 + res
# print(res)
#
#
# m = int(input('m = '))
# n = int(input('n = '))
#
#
# while n != 0:
#     r = m % n
#     m, n = n, r
# print(m)
#







# a = int(input())
# res = 1
# n = 1
# for i in range(a):
#     m1 = int(input('/ = '))
#     m = int(input('m = '))
#     n1 = int(input('/ = '))
#     n = int(input('n = '))
#
#     r = m % n
#     m, n = n, r
#     res = m / n
#     print((m1 + n1) / res)





# a = float(input())
# if abs(a) < 1 / 1000000 or a == 0:
#     print(1000000)
# else:
#     print(1 / a)



#
# names = set()
# old_names = set()
# for i in range(int(input())):
#     for j in range(int(input())):
#         name = input()
#         names.add(name)
#     if old_names == set():
#         old_names = names
#     old_names = old_names & names
#     names.clear()
# for qwe in old_names:
#     print(qwe)




#a = 999999
#b = 142857
#x = a - b
#print(x)




#a = input()
#b = len(a) * 40
#c = b // 100
#d = (b - c * 100) % 100
#print(c, 'dollars', d, 'cent')


#a = int(input())
#b = a // 100
#ba = a // 10
#bb = ba % 10
#bbb = a % 10    
#if b + bbb == 2 * bb:
    #print('Beautiful number')
#else:
    #print('Usual number')



#a = input()
#b = len(a) * 2 + 3
#print(b)





#a = int(input())
#b = a // 100
#ba = a // 10
#bb = ba % 10
#bbb = a % 10    
#if (b == bb or b == bbb or bb == bbb) and not (b == bb == bbb):
    #print('There are two identical digits in the number')
#elif b == bb == bbb:
    #print('There are all identical digits in the number')
#else:
    #print('OK')










#a = float(input())
#if abs(a) > 1000000 or a == 0:
    #print(1000000)
#else:
    #print(1 / a)


#a = int(input())
#b = a // 100
#ba = a // 10
#bb = ba % 10
#bbb = a % 10
#a1 = b + bb
#a2 = bb + bbb
#if a2 > a1:
    #a1, a2 = a2, a1
#print(str(a1) + str(a2))


#a = float(input())
#if abs(1 / a) > 1 / 1000000 or a == 0:
    #print(1000000)
#else:
    #print(1 / a)

#a = input()
#b = input()
#if (a == 'Tula' and b != 'Tula' and b != 'Penza')\
   #or (a != 'Tula' and a != 'Penza') and b == 'Penza':
    #print('YES')
#else:
    #print('NO')



 
#a = float(input())
#b = float(input())
#c = input()
#if not(c == '+' or c == '-' or c == '*' or c == '/'):
    #print('888888') 
#else:
    #if c == '+':
        #print(a + b)
    #elif c == '-':
        #print(a - b)
    #elif c == '*':
        #print(a * b)
    #elif c == '/' and b == 0:
        #print('888888')
    #else:
        #print(a / b)
                

#a = input()
#print('The word ' + a + ' has a length of ' + str(len(a)))

#days_per_year = 365
#hours_per_day = 24
#minutes_per_hour = 60
#a = days_per_year * hours_per_day * minutes_per_hour
#print(a)




#a = 1400 / 2
#b = 3
#c = a // b
#d = a % b
#print(int(c) + int(d))






#a = int(input())
#b = int(input())
#print(a + b)
  

#a = 12 #int
#b = 12.5 #float
#c = 'asdfghjgfd' #str
#a = (4 < 0) #bool
#value1 = True
#value2 = False





#a = float(input())
#if a == 0:
  #print('0')
#elif a < 0:
  #print('-')
#elif a > 0:
  #print('+')
  
  
#a = float(input())
#if a == 0:
    #print('0')
#elif a < 0:
    #print('-')
#elif a > 0:
    #print('+')
    
    
    
  #a = input()
  #b = input()
  #if a == b:
      #print('NO')
  #else:
      #print('YES')
    
    #a = 1
    #for x in range(1, 10):
        #a = a * x
    #if(True):
        #print(a)              

#a = int(input())
#b = int(input())
#c = int(input())
#abc = (a, b, c)
#x = sorted(abc)
#print(x[2])
#print(x[1])
#print(x[0])


#a = input()
#b = input()
#c = input()
#if c == '+' or c == '-' or c == '*' or c == '/': 
    #print(a, c, b)
#elif b == '0' or not(c == '+' or c == '-' or c == '*' or c == '/'):
    #print ('888888')
    
    
#a = int(input())
#if (a % 4 == 0 and not(a % 100 == 0)) or a % 400 == 0:
    #print('Leap year')
#else:
    #print('Non leap year')
    
  #a = int(input())
  #if a % 2 == 0:
      #print('even')
  #else:
      #print('odd')  


      
    #a = float(input())
    #b = float(input())
    #c = input()
    #if not(c == '+' or c == '-' or c == '*' or c == '/'):
        #print('888888') 
    #else:
        #if c == '+':
            #print(a + b)
        #elif c == '-':
            #print(a - b)
        #elif c == '*':
            #print(a * b)
          
        #elif c == '/':
            #if(b == '0'):
                #print('888888')
            #else:
                #print(a / b)
        

