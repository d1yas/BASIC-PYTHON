# 1
# a = int(input("Enter a number: "))
#
# if a>0:
#     a+=1
#     print(a)
# 2
# if a>0:
#     a+=1
#     print(a)
# else:
#     a-=2
#     print(a)
# 3
# if a>0:
#     a+=1
#     print(a)
# elif a<=0:
#     a-=2
#     print(a)
# elif a==0:
#     a=10
#     print(a)
# 4
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))
# hisob = 0
# if a>0:
#     hisob+=1
# if b>0:
#     hisob+=1
# if c>0:
#     hisob+=1
# print(hisob)
# 5
# hisob_musbat = 0
# hisob_manfiy = 0
# if a>0:
#     hisob_musbat+=1
# else:
#     hisob_manfiy+=1
# if b>0:
#     hisob_musbat+=1
# else:
#     hisob_manfiy+=1
# if c>0:
#     hisob_musbat+=1
# else:
#     hisob_manfiy+=1
# print("Musbat sonlar", hisob_musbat)
# print("Manfiy sonlar", hisob_manfiy)
# 6
# a = int(input("A: "))
# b = int(input("B: "))
# if a > b:
#     print("a kotta")
# else:
#     print("b kotta")
# 7
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# if A < B:
#     kichik = 1
# else:
#     kichik = 2
#
# print("Sonalrni Kichik tartibi",kichik)
# 8
# A = int(input("A: "))
# B = int(input("B: "))
#
# if A > B:
#     katta = A
#     kichik = B
# else:
#     katta = B
#     kichik = A
# print("Katta",katta,"kichik",kichik)
# 9
# A = int(input("A: "))
# B = int(input("B: "))
# if A>B:
#     A = B
#     B = A
# print("A ",A)
# print("B ",B)
# 10
# A = int(input("A: "))
# B = int(input("B: "))
#
# if A != B:
#     A = B = A + B
# else:
#     A = B = 0
#
# print("A = ",A," B = ",B)
# 11
# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
#
# if A != B:
#     if A > B:
#         A = B = A
#     else:
#         A = B = B
# else:
#     A = B = 0
# print("A = ",A," B = ",B)
# 12
# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
#
# kichik = A
# if B < kichik:
#     kichik = B
# if C < kichik:
#     kichik = C
#
# print("Kichik son:", kichik)
# 13


# 14
# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
#
# kichik = A
# katta = A
#
# if B < kichik:
#     kichik = B
# if C < kichik:
#     kichik = C
#
# if B > katta:
#     katta = B
# if C > katta:
#     katta = C
# 15
# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
# sum_AB = A + B
# sum_AC = A + C
# sum_BC = B + C
#
# if sum_AB >= sum_AC and sum_AB >= sum_BC:
#     print(A,B,"Yigindisi eng kotta")
# elif sum_AC >= sum_AB and sum_AC >= sum_BC:
#     print(A,C,"Yigindisi eng kotta")
# else:
#     print(B, C, "Yigindisi eng kotta")
# 16
# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
# if A < B < C:
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A = -A
#     B = -B
#     C = -C
#
# print("A =" ,A,"B = ",B,"C = ",C)
# 17
# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
#
#
#
# if (A < B < C) or (A > B > C):
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A = -A
#     B = -B
#     C = -C
# print("A =" ,A,"B = ",B,"C = ",C)
# 18
# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
#
# if A == B:
#     print("C soni boshqa")
# elif A == C:
#     print("B soni boshqa")
# elif B == C:
#     print("A soni boshqa")
# else:
#     print("Uchala son har xil.")
# 19
# A = int(input("A: "))
# B = int(input("B: "))
# C = int(input("C: "))
# D = int(input("D: "))
#
# if A == B == C:
#     print("D soni boshqa")
# elif A == B == D:
#     print("C soni boshqa")
# elif A == C == D:
#     print("B soni boshqa")
# elif B == C == D:
#     print("A soni boshqa")
# else:
#     print("To'rtta son har xil.")
# 20
# 21
# x = int(input("x: "))
# y = int(input("y: "))
# if x == 0 and y == 0:
#     print(0)
# elif x == 0:
#     print(2)
# elif y == 0:
#     print(1)
# else:
#     print(3)
# 22
# x = int(input("x: "))
# y = int(input("y: "))
#
# if x > 0 and y > 0:
#     print("1 chorak")
# elif x < 0 and y > 0:
#     print("2 chorak")
# elif x < 0 and y < 0:
#     print("3 chorak")
# elif x > 0 and y < 0:
#     print("4 chorak")
# else:
#     print("Nuqta oqlarda joylashgan emas.")
# 24
# import math
#
# x = int(input("x: "))
#
# if x > 0:
#     f_x = 2 * math.sin(x)
# else:
#     f_x = x - 6
#
# print("f(x) =",f_x)
# 25
# x = int(input("x ni kiriting: "))
#
# if x < -2 or x > 2:
#     f_x = 2 * x
# else:
#     f_x = -3 * x
# print("f(x) =",f_x)
# 26
# x = int(input("x: "))
#
# if x < 0:
#     f_x = -x**9
# elif 0 <= x < 2:
#     f_x = x**2
# else:
#     f_x = 4
# print("f(x) =",f_x)
# 29
# son = int(input("Son: "))
#
# if son == 0:
#     n = "son nolga teng"
# elif son > 0 and son % 2 == 0:
#     n = "musbat juft son"
# elif son > 0 and son % 2 != 0:
#     n = "musbat toq son"
# elif son < 0 and son % 2 == 0:
#     n = "manfiy juft son"
# else:
#     n = "manfiy toq son"
#
# print(n)
# 30
# son = int(input("son kiriting: "))
#
# if son < 1 or son > 999:
#     print("Berilgan oraliqda son emas.")
# elif son < 10:
#     xona = "bir xonali"
# elif son < 100:
#     xona = "ikki xonali"
# else:
#     xona = "uch xonali"
#
# if son % 2 == 0:
#     juft_toq = "juft"
# else:
#     juft_toq = "toq"
# print(xona,juft_toq,"son")
