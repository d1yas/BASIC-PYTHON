# 1
# kun = int(input("Son kiritin: "))

# if kun == 1:
#     print("Dushanba")
# elif kun == 2:
#     print("Seshanba")
# elif kun == 3:
#     print("Chorshanba")
# elif kun == 4:
#     print("Payshanba")
# elif kun == 5:
#     print("Juma")
# elif kun == 6:
#     print("Shanba")
# elif kun == 7:
#     print("Yakshanba")
# else:
#     print("error")
# 2
# k = int(input("K: "))
# if k == 1:
#     print("Yomon")
# elif k == 2:
#     print("Qoniqarsiz")
# elif k == 3:
#     print("Qoniqarli")
# elif k == 4:
#     print("Yaxshi")
# elif k == 5:
#     print("Alo")
# else:
#     print("hato")
# 3
# oy = int(input("Oy soni: "))
# if oy > 0 and oy<3 or oy==12:
#     print("Qish")
# elif oy>2 and oy < 6:
#     print("Bahor")
# elif oy>5 and oy<9:
#     print("Yoz")
# elif oy>8 and oy<12:
#     print("kuz")
# else:
#     print("Hato son")
# 4
# oy = int(input("Oy: "))
#
# if oy == 1 or oy ==3 or oy==5 or oy == 7 or oy == 10 or oy == 12:
#     print("31 kun")
# elif oy == 4 or oy == 6 or oy == 9 or oy == 11:
#     print("30 kun")
# elif oy == 2:
#     print("28-29kun")
# else:
#     print("Error")
# 5
# A = int(input("A: "))
# B = int(input("B: "))
# qiymat = int(input("qiymat kiriting: "))
#
# if qiymat == 1:
#     natija = A+B
# elif qiymat == 2:
#     natija = A-B
# elif qiymat == 3 :
#     natija = A/B
# elif qiymat == 4:
#     natija = A*B
#
# print(natija)
# 6
# A = int(input("A: "))
#
# qiymat = int(input("qiymatni metrda kiriting: "))
#
# if qiymat == 1:
#     natija = A / 10
# elif qiymat == 2:
#     natija = A / 1000
# elif qiymat == 3:
#     natija = A
# elif qiymat == 4:
#     natija = A * 1000
# elif qiymat == 5:
#     natija = A * 100
#
# print(natija)
# 7
# a = int(input("A: "))
# qiymat = int(input("Qiymat:(1-5) "))
# if qiymat == 2:
#     natija = a * 1000000
# elif qiymat == 3:
#     natija = a * 1000
# elif qiymat == 4:
#     natija = a / 1000
# elif qiymat == 5:
#     natija = a / 100
# elif qiymat == 1:
#     print("kilogram kiritdiz")
# else:
#     print("error")
#
# print(natija)
# 8
# D = int(input("Kun: "))
# M = int(input("Oy: "))
#
# if M == 1 and D <= 31:
#     print("Yanvar", D)
# elif M == 2 and D <= 29:
#     print("Fevral", D)
# elif M == 3 and D <= 31:
#     print("Mart", D)
# elif M == 4 and D <= 30:
#     print("Aprel", D)
# elif M == 5 and D <= 31:
#     print("May", D)
# elif M == 6 and D <= 30:
#     print("Iyun", D)
# elif M == 7 and D <= 31:
#     print("Iyul", D)
# elif M == 8 and D <= 31:
#     print("Avgust", D)
# elif M == 9 and D <= 30:
#     print("Sentyabr", D)
# elif M == 10 and D <= 31:
#     print("Octyabr", D)
# elif M == 11 and D <= 30:
#     print("Noyabr", D)
# elif M == 12 and D <= 31:
#     print("Decabr", D)
# else:
#     print("Error")
# 9
# D = int(input("Kun: "))
# M = int(input("Oy: "))
# s = 0
# keyngi_sana = D
# if M == 1 and D <= 31:
#     if M == 1 and D <=32:
#         print(False)
#         print(s+keyngi_sana)
#         print(True)
#     keyngi_sana +=1
#     print("Keyngi sana Yanvar", keyngi_sana)
# elif M == 2 and D <= 29:
#     keyngi_sana +=1
#     print("Keyngi sana Fevral", keyngi_sana)
# elif M == 3 and D <= 31:
#     keyngi_sana += 1
#     print("Keyngi sana Mart",keyngi_sana)
# elif M == 4 and D <= 30:
#     keyngi_sana += 1
#     print("Keyngi sana Aprel", keyngi_sana)
# elif M == 5 and D <= 31:
#     keyngi_sana += 1
#     print("Keyngi sana May", keyngi_sana)
# elif M == 6 and D <= 30:
#     keyngi_sana += 1
#     print("Keyngi sana Iyun", keyngi_sana)
# elif M == 7 and D <= 31:
#     keyngi_sana += 1
#     print("Keyngi sana Iyul", keyngi_sana)
# elif M == 8 and D <= 31:
#     keyngi_sana += 1
#     print("Keyngi sana Avgust", keyngi_sana)
# elif M == 9 and D <= 30:
#     keyngi_sana += 1
#     print("Keyngi sana Sentyabr", keyngi_sana)
# elif M == 10 and D <= 31:
#     keyngi_sana += 1
#     print("Keyngi sana Octyabr", keyngi_sana)
# elif M == 11 and D <= 30:
#     keyngi_sana += 1
#     print("Keyngi sana Noyabr", keyngi_sana)
# elif M == 12 and D <= 31:
#     keyngi_sana += 1
#     print("Keyngi sana Decabr", keyngi_sana)

# 10
# Y = "Ortada"
# print("Hozir robot",Y,"turibdi")
# comand = int(input("Comand: "))
#
# if comand == 0:
#     Y = "Sharqga"
# elif comand == 1:
#     Y = "Garbga"
# elif comand == 2:
#     Y = "Janubga"
# else:
#     print("error")
#
# print("Robot",Y,"yurdi")
# 11
# C = "Shimol"
# K1 = int(input("K1 commanda kiriting: "))
# K2 = int(input("K2 commanda kiriting: "))
#
# if C == 'Shimol':
#     if K1 == 0 or K2 == 0:
#         C = 'Sharq'
#     elif K1 == 1 or K2 == 1:
#         C = 'Garb'
#     elif K1 == 2 or K2 == 1:
#         C = 'Janub'
# elif C == 'Sharq':
#     if K1 == 0 or K2 == 0:
#         C = 'Janub'
#     elif K1 == 1 or K2==1:
#         C = 'Shimol'
#     elif K1 == 2 or K2==2:
#         C = 'Garb'
# elif C == 'Janub':
#     if K1 == 0 or K2 == 0:
#         C = 'Garb'
#     elif K1 == 1 or K2 == 1:
#         C = 'Sharq'
#     elif K1 == 2 or K2==2:
#         C = 'Shimol'
# elif C == 'Garb':
#     if K1 == 0 or K2 == 0:
#         C = 'Shimol'
#     elif K1 == 1 or K2 == 1:
#         C = 'Janub'
#     elif K1 == 2 or K2 ==2:
#         C = 'Sharq'
#
# print(C)
# 12

t = 3.14

D = None
R = None
L = None
S = None

if R is not None:
    D = 2 * R
    L = 2 * t * R
    S = t * R * R
if D is not None and R is not None:
    R = D / 2
    L = 2 * t * R
    S = t * R * R
if L is not None and R is not None:
    R = L / (2 * t)
    D = 2 * R
    S = t * R * R
if S is not None and R is None:
    R = (S / t) ** 0.5
    D = 2 * R
    L = 2 * t * R

print("Radius (R):",R)
print("Diametr (D):",D)
print("Uzunlig (L):",L)
print("Yuza (S):",S)