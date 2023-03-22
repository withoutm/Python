# n = int(input("Введите число"))
# factorial = 1
# for i in range(2,n+1):
#      factorial *=i
# print(factorial)
# n = input("Введите число")
# even = 0
# odd = 0
# for i in n:
#     if int(i) %2 ==0:
#         even += 1
#     else:
#         odd += 1
# print (even, odd)
n =int(input("Введите число"))
a = 0
b = 1
c = 2
print(a, b)
for i in range(0,n-2):
    c = a + b
    print(c)
    a = b
    b = c


