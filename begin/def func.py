# def funksiya_nomi():
#     pass
#
#
# def son_qoshib_ber(a, b):
#     daraja2(a=a + b)
#
# # rekursiv funksiyalar bular o`zini o`zi ishlatuvchi funksiyalar
# def daraja2(a):
#     return a ** 2
#
#
# son_qoshib_ber(4, 5)
# ikkinchi = daraja2(9)# # 1
# def PowerA3(a):
#     return a**3
#
# A = 1.8
# B = -3.0
# C = -2.1
#
# D = -2
# E = 4
# A3 = PowerA3(A)
# B3 = PowerA3(B)
# C3 = PowerA3(C)
# D3 = PowerA3(D)
# E3 = PowerA3(E)
#
# print(f"""
# A ning 3 darajasi {A3}
# B ning 3 darajasi {B3}
# C ning 3 darajasi {C3}
# D ning 3 darajasi {D3}
# E ning 3 darajasi {E3}
# """)

# 2

# def PowerA234(a):
#     a2 = a ** 2
#     a3 = a ** 3
#     a4 = a ** 4
#     return a2, a3, a4
#
#
# A = 1.5
# B = -2.0
# C = 3.0
#
# A2, A3, A4 = PowerA234(A)
# B2, B3, B4 = PowerA234(B)
# C2, C3, C4 = PowerA234(C)
#
# print(f"A ning 2-darajasi: {A2}, 3-darajasi: {A3}, 4-darajasi: {A4}")
# print(f"B ning 2-darajasi: {B2}, 3-darajasi: {B3}, 4-darajasi: {B4}")
# print(f"C ning 2-darajasi: {C2}, 3-darajasi: {C3}, 4-darajasi: {C4}")
#
# import math
#
#
# def MEAN(x, y):
#     arifmetik_mean = (x + y) / 2
#     geometrik_mean = math.sqrt(x * y)
#     return arifmetik_mean, geometrik_mean
#
#
# A = 4
# B = 16
# C = 9
# D = 25
#
# AB_arifmetik, AB_geometrik = MEAN(A, B)
# AC_arifmetik, AC_geometrik = MEAN(A, C)
# AD_arifmetik, AD_geometrik = MEAN(A, D)
#
# print(f"A va B arifmetik: {AB_arifmetik}, geometrik: {AB_geometrik}")
# print(f"A va C arifmetik: {AC_arifmetik}, geometrik: {AC_geometrik}")
# print(f"A va D arifmetik: {AD_arifmetik}, geometrik: {AD_geometrik}")
#
#
# def salom():
#     print("Salom")
#     salom()
# salom()
# def test(a=4, b='Salom'):
#     return str(a) + b
# async def salom(a):
#     print(a)
#
#
# def Triangle(a, b, c):
#     if a == b and b == c and c == a:
#         return a + b + c
#     else:
#         print("Uchburchak teng emas")
#     # return perimetr
#
#
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# print(Triangle(a, b, c))
#
# def DigitCountSum(a,b,c):
#     return a+b+c
#
# count = (DigitCountSum())
#
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# print(DigitCountSum(a,b,c))
#
#
# def InvertDigit(n):
#     return int(str(n)[::-1])
#
# a = 123
# b = 456
# c = 789
# print(InvertDigit(a))
# print(InvertDigit(b))
# print(InvertDigit(c))
#
# def Swap(x,y):
#     change = x[0]
#     x[0] = y[0]
#     y[0] = change
#
# A = [13]
# B = [15]
# C = [18]
# D = [20]
#
# Swap(B,A)
# Swap(D,C)
#
# print("A = ",A[0],"B = ",B[0])
# print("C = ",C[0],"D = ",D[0])
#
# def Minmax(x, y):
#     if x > y:
#         x, y = y, x
#     return x, y
#
#
# a = 10
# b = 20
# c = 30
# d = 40
#
# a, b = Minmax(a, b)
# c, d = Minmax(c, d)
#
# minimal_son = min([a, b, c, d])
# maximal_son = max([a, b, c, d])
#
# print("Eng kotta son: ", maximal_son)
# print("Eng kichik son: ", minimal_son)
#
#
# def  Sorting(A,B,C):
#     if A>B:
#         A,B = B,A
#     if B>C:
#         C,B = B,C
#     if A>B:
#         A,B = B,A
#     return A,B,C
# A1 = 10
# B1 = 12
# C1 = 13
#
# A2 = 9
# B2 = 17
# C2 = 5
#
# A1,B1,C1 = Sorting(A1,B1,C1)
# A2,B2,C2 = Sorting(A2,B2,C2)
# print(A1,B1,C1)
# print(A2,B2,C2)
#
#
# def SortDec(A,B,C):
#     if B>A:
#         A,B=B,A
#     if C<B:
#         C,B=B,C
#     if B>A:
#         A,B=B,A
#
#     return A,B,C
#
# A1 = 3
# B1 = 5
# C1 = 7
#
# A2 = 4
# B2 = 6
# C2 = 8
#
# A1,B1,C1 = SortDec(A1,B1,C1)
# A2,B2,C2 = SortDec(A2,B2,C2)
#
#
# print(A1,B1,C1)
# print(A2,B2,C2)
#
# def ShiftRight(A, B, C):
#     return A, B, C
#
#
# A1, B1, C1 = 2, 4, 6
# A2, B2, C2 = 3, 5, 7
#
# sortA, sortB, sortC = ShiftRight(A1, B1, C1)
# sortA2, sortB2, sortC2 = ShiftRight(A2, B2, C2)
#
# print(sortA, sortB, sortC)
# print(sortA2, sortB2, sortC2)
#
#
# def ShiftLeft2(A, B, C):
#     return A, B, C
#
#
# A = 10
# B = 20
# C = 30
#
# A1, B1, C1 = ShiftLeft2(A, B, C)
# A2, B2, C2 = C1,A1,B1
# print(A2, B2, C2)
#
# def Ishora(x):
#     if x < 0:
#         return -1
#     elif x > 0:
#         return 1
#     else:
#         return 0
#
#
# def ishora_yigindisi(a, b):
#     return Ishora(a) + Ishora(b)
#
#
# a = -2
# b = 3
#
# natija = ishora_yigindisi(a, b)
# print(natija)
#
#

