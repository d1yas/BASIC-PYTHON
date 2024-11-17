#1
# a = int(input("Kvadrat tomonini kiriting: "))
# P = 4 * a
# print('Perimetr',P)
#2
# a = int(input("Kvadrat tomoni kiriting: "))
# s = a**2
# print("Yuzasi",s)
#3
# a = int(input("Kvadrat tomoni a kiriting: "))
# b = int(input("Kvadrat tomoni b kiriting: "))
# s = a*b
# p = 2*(a+b)
# print("Perimetri = ",p, "Yuzasi = ",s )
#4
# d = int(input("Diametrni kiriting: "))
# p = 3.14
# l = p * d
# print("Diametri = ",l)
#5
# a = int(input("Kubning a kiriting: "))
# V = a**3
# S = 6*a**2
# print("Hajmi = ",V,"Tola sirti = ",S)
#6
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# c = int(input("Enter c number: "))
# V = a*b*c
# S = 2*(a*b+b*c+a*c)
# print("Hajmi = ", V, "Tola sirti = ",S )
#7
# R = int(input("Doira Radiusni kiriting: "))
# P = 3.141592653589793
# L = 2*P*R
# S = P*R**2
# print("Uzunligni: ",L,"Yuzasi: ", S)
#8
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# orta_arifmetik_son = (a+b)/2
# print("Orta Arifmetik Son: ",orta_arifmetik_son)
#9
import math
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# geometric_mean = math.sqrt(a * b)
#
# print(geometric_mean)
#10
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# toplami = a+b
# kopaytmasi = a*b
# kvadrat_a = a**2
# kvadrat_b = b**2
# print("A va B ning Toplami  = ", toplami,"Kopaytmasi = ", kopaytmasi,"A ning kvadrati = ", kvadrat_a, "B ning Kvadrati = ", kvadrat_b )
#11
# a = int(input("Birinchi son: "))
# b = int(input("Ikkinchi son: "))
# toplami = a+b
# kopaytmasi = a*b
# modul1 = abs(a)
# modul2 = abs(b)
# print("Toplami:", toplami)
# print("Kopaytmasi :", kopaytmasi)
# print("Birinchi sonning moduli :", modul1)
# print("Ikkinchi sonning moduli :", modul2)

#12
# a = int(input("Katet a"))
# b = int(input("Katet b"))
# c = math.sqrt(a**2 + b**2)
# perimetr = a+b+c
# print("Perimetr = ", perimetr)
# print("Gipotenuza = ", c)

#13
# p = 3.14
# R1 = int(input("Birinchi Aylana: "))
# R2 = int(input("Ikkinchi Aylana: "))
# s1_yuzasi = p*R1
# s2_yuzasi =p*R2
# s3 = s1_yuzasi + s2_yuzasi
# print(s3)

#14
# L = int(input("Aylananing uzunligi: "))
# p = 3.14
#
# R = L/(2/p)
# S = p * R**2
# print("Radius: ", R)
# print("Aylaning Yuzasi")
#15

# L = int(input("Enter a number: "))
# pi = 3.14
#
# R = L / (2 * pi)
#
# d = 2 * R
#
# print(f"Aylaning radiusi: ",R)
# print(f"Aylaning diametri: ",d)
#16
# x1 = 5
# x2 = 12
#
# masofa = abs(x1 - x2)
#
# print(f"Nuqtalar orasidagi masofa:", masofa)
#17
# A = int(input("A:"))
# B = int(input("B:"))
# C = int(input("C:"))
#
# AC = abs(A-C)
# BC = abs(B-C)
#
# summa = AC + BC
# print("AC",AC)
# print("BC",BC)
# print("summa",summa)
#18
# A = int(input("A:"))
# B = int(input("B:"))
# C = int(input("C:"))
#
# AC = abs(A-C)
# BC = abs(B-C)
#
# kopaytmasi = AC * BC
# print("AC",AC)
# print("BC",BC)
# print("Kopaytmasi",kopaytmasi)
#19
# x1,y1 = 1, 2
# x2,y2 = 4, 5
#
# lengh = abs(x2-x1)
# width= abs(y2-y1)
#
# h = lengh*width
# perimeter = 2*(lengh+width)
# print("Perimetr",perimeter)
# print("Yuza",h)
#20
# x1,x2 = 4,6
# y1,y2 = 5,8
#
# masofa = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print("Masofa",masofa)
#21
# x1,y1 = 2,3
# x2,y2 = 5,7
# x3,y3 = 6,9
#
# a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
# b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
# c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# perimeter = a + b + c
#
# s = perimeter / 2
#
# yuzasi = math.sqrt(s * (s - a) * (s - b) * (s - c))
# print("Perimeter : ", perimeter)
# print("Yuzasi : ", yuzasi)
#22
# A = 20
# B = 30
# print("Hozir A = ", A)
# print("Hozir B = ", B)
# A = int(input("A: "))
# B = int(input("B: "))
# print("A = ",A)
# print("B = ",B)
#23
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
# a = b
# b = c
# c = a
# print("A ning yangi qiymati = ",a)
# print("B ning yangi qiymati = ",b)
# print("C ning yangi qiymati = ",c)
#24
# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# c = int(input("Enter c : "))
# a = c
# c = b
# b = a
# print("A = ",a )
# print("B = ",b)
# print("C = ",c)

#25
# x = int(input("Enter a number: "))
# y = 3*x**6-6*x**2-7
# print("Javob: ", y)
#26
# x = int(input("Enter a number: "))
# y = 4*(x-3)**6-7*(x-3)**3+2
# print("Javob: ", y)
#27
# A = int(input("Enter a number: "))
# a2 = A**2
# a4 = A**4
# a8 = A**8
# print("A ning A 2 darajasi = ",a2)
# print("A ning A 4 darajasi = ",a4)
# print("A ning A 8 darajasi = ",a8)
#28
# A = int(input("Enter a number: "))
# a2 = A**2
# a3 = A**3
# a5 = A**5
# a10 = A**10
# a15 = A**15
# print("A ning A 2 darajasi = ",a2)
# print("A ning A 3 darajasi = ",a3)
# print("A ning A 5 darajasi = ",a5)
# print("A ning A 10 darajasi = ",a10)
# print("A ning A 15 darajasi = ",a15)
#29
# gradus = float(input("Gradus kiriting: "))
#
# radian = gradus*(math.pi/180)
# print(radian)
#30
# radian = float(input("Gradus kiriting: "))
#
# gradus = radian*(180/math.pi)
# print(gradus)
#31
# T_F = int(input("T_f gradus kiriting: "))
# T_c = (T_F-32)*5/9
# print(T_c)
#32
# T_c = int(input("T_f gradus kiriting: "))
# T_f = (T_c*5/9)+32
# print(T_f)
#33
# x = int(input("Enter kg konfet: "))
# a = int(input("Enter cost in konfet: "))
#
# bir_kg = a//x
# y_kg = a/x
#
# print("1 kg = ",bir_kg,"Y kg = ", y_kg)
#34
# x_shokolad = int(input("Kg Shokolad: "))
# a_cost_shokolad = int(input("Shokolad Narxi: "))
# y_konfet = int(input("Konfet kg: "))
# b_cost_konfet = int(input("Konfet narxi: "))
#
# one_kg_sh = a_cost_shokolad//x_shokolad
# one_kg_konf = b_cost_konfet//y_konfet
# print("Shokolad 1 kg narxi = ",one_kg_sh, "Konfet 1 kg narxi = ",one_kg_konf)
#35
# v = int(input("Qayiq Tezligini kiriting: "))
# u = int(input("Daryo oqim tezligini:"))
#
# t1 = int(input("Oqim boyicha: "))
# t2 = int(input("Oqimga qarshi: "))
# S1 = (v+u)*t1
# S2 = (v+u)*t2
# S3 = S1+S2
# print("Qayiqni umumiy yurgan yo'li tezligi",S3,"km")
#36
# V1 = int(input("Birinchi avto tezligi: "))
# V2 = int(input("Ikkinchi avto tezligi: "))
# S = int(input("Avtomobillar orasidagi boshlang'ich masofani kiriting: "))
# t = int(input("Uzoqlanish vaqti T kiriting  : "))
# yangi_masofa = S + (V1+V2)*t
# print("Masofa = ", yangi_masofa)
#37
# V1 = int(input("Birinchi avto tezligi: "))
# V2 = int(input("Ikkinchi avto tezligi: "))
# S = int(input("Avtomobillar orasidagi boshlang'ich masofani kiriting: "))
# t = int(input("Uzoqlanish vaqti T kiriting  : "))
# yangi_masofa = S - (V1+V2)*t
# print("Masofa = ", yangi_masofa)
#38
# A = int(input("A kofeffisent kiriting "))
# B = int(input("B kofeffisent kiriting "))
#
# if A != 0:
#     x = -B / A
#     print("Tenglamaning yechimi: x =", x)
# else:
#     print("Xatolik: A qiymati 0 bo'lmasligi kerak.")
#39
A = int(input("A koefifisentni kiriting: "))
B = int(input("B koefifisentni kiriting: "))
C = int(input("C koefifisentni kiriting: "))
if A == 0:
    print("A 0 ga teng bo'lmasligi kerak.")
else:
    diskriminant = B ** 2 - 4 * A * C

    if diskriminant > 0:
        x1 = (-B + math.sqrt(diskriminant)) / (2 * A)
        x2 = (-B - math.sqrt(diskriminant)) / (2 * A)
        print(f"Yechimlar: x1 = {x1}, x2 = {x2}")
    else:
        print("Diskriminant noldan katta bo'lishi kerak.")
#40
# Ko'rsatmalar
A1 = int(input("A1 ni kiriting: "))
B1 = int(input("B1 ni kiriting: "))
C1 = int(input("C1 ni kiriting: "))
A2 = int(input("A2 ni kiriting: "))
B2 = int(input("B2 ni kiriting: "))
C2 = int(input("C2 ni kiriting: "))

D = A1 * B2 - A2 * B1
Dx = C1 * B2 - C2 * B1
Dy = A1 * C2 - A2 * C1

if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"Yechimlar: x = {x}, y = {y}")
else:
    if Dx == 0 and Dy == 0:
        print("Tenglamalar sistemasining cheksiz ko'p yechimlari mavjud.")
    else:
        print("Tenglamalar sistemasining yechimlari mavjud emas.")

# > katta
# < kichik
# == teng bo`lsa
# != teng emas
# >= katta yoki teng
# <= kichik yoki teng
# is teng bo`lsa
# not bu emas
# in ichida bor yoki yoqligi "S" in "Salom"
# not in ichida bo`lmasa
# and va
# or yoki


