# while bu cheksiz sikl operatori
# while boolenlar bilan ishlaydi
# breake funksiyasi false
# a = True
# while a:
#     print("salom")
#     a = False
# a = 0
# while a != 10:
#     a += 1
#     print(a)
# count = 0
# while True:
#     continue
#     print('Salom')
# A ------------
# B -----------
# C ------

# 1
# A = 10
# B = 1
# C = 0
# while True:
#     if A > B:
#         C += 1
#     elif A == B:
#         print('Bo`sh joy yoq')
#     if C == B and B < A:
#         print('Bo`sh joy: ', A - B)
#     else:
#         continue
# 2

# a = 10
# b = 2
# c = 0
#
# while a >= b:
#     a -= b
#     c += 1
#     print(c)
# 3
# n = 10
# k = 3
# butun = 0
# qoldiq = n
#
# while qoldiq>=k:
#     qoldiq -= k
#     butun += 1
# print("butun",butun)
# print("qoldiq",qoldiq)
# 4
# n = int(input("Enter a number: "))
# c = 1
#
# while c < n:
#     tem = 0
#     for i in range(3):
#         tem += c
#     c = tem
#
# if c == n:
#     print("3 darajasi",c)
# else:
#     print("3 darajasi emas",c)
# 5


# n = 16
# k = 0
#
# while n > 1:
#     n = n // 2
#     k += 1
#     print(True)
#
# print("k =", k)
# 6
n = 10
res = 1
while n > 0:
    res *= n
    n-=2
print("n!! = ",res)
