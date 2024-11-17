# for va while bu sikl operatorlari
# iterator bu sikl ga mos o`zgaradigan va oshib yoki kamayib boruvchi o`zgaruvchidir
# aylanishlar sonini topish uchun range(n,k) aylanishlar_soni = k-n
# i ning oxirgi natijasi k-1 da tugaydi
# for i in range(1, 11):
#     for d in range(1, 11):
#         print(f"{d} * {i} = {i * d}")
# for i in range(1, 51):
#     if i % 2 == 0:
#         print('juft', i)
#     else:
#         print('toq', i)

# 1
# n = int(input("A: "))
# k = int(input("K: "))
# for i in range(n,k):
#     print(i)
# 2
# a = int(input("A: "))
# b = int(input("B: "))
#
# for i in range(a, b):
#     print(i)
#
# c = b - a + 1
# print("Chaqirilga sonlar", c)
# 3

# a = int(input("A: "))
# b = int(input("B: "))
#
# for i in range(b,a - 1 , -1 ):
#     print(i, end=" ")
# 4
# cost = 10000
#
# for i in range(1,11):
#     narx = i * cost
#     print(f'{i} kg = {narx}')
# 5
# cost = 10000
# for i in range(1,11):
#     s = i/10
#     narx = s * cost
#     print(f'{s} kg = {narx}')
# 6
# cost = 10000
# for i in range(12,21,2):
#     s = i/10
#     narx = s*cost
#     print(f'{s} kg = {narx}')
# 7
# a = int(input("A: "))
# b = int(input("B: "))

# s = 0
#
# for i in range(a, b+1):
#     s += i
#
# print("Yigindisi",s)
# 8
# s = 1
#
# for i in range(a, b + 1):
#     s *= i
#     print(s)
# 9
# s = 1
# for i in range(a, b):
#     s = i**2
#     print(s)
# 10
# n = int(input("n sonini kiriting (n > 0): "))
#
# S = 0
# for i in range(1, n + 1):
#     S += 1 / i
#
# print(f"Yig'indisi: {S:.4f}")
# 11
# n = int(input("n: "))
# S = 0
#
# for i in range(n,2*n + 1):
#     S += i**2
#     print(S)
# 12
# n = int(input("n: "))
# S = 1
# for i in range(1, n + 1):
#     S *= 1 + i / 10
# print(f"ko'paytmasi: {S}")
# 13
# n = int(input("n: "))
#
# S = 0
# for i in range(1, n + 1):
#     S += i / 10 * (-1)**(i + 1)
#
# print("Yig'indi S =", S)
# 14


# for i in range(1, 10):
#     if i == 4:
#         print("Xozr sikl 4 chi aylanishda")
#     else:
#         print(i)
baza = ['Olma', "Shaftoli", 'o`rik', 'nok', 'uzum']

for i in baza:
    hardlar_soni = len(i)
    if hardlar_soni % 2 == 0:
        index = hardlar_soni / 2 -1
        print(i[int(index)  ])
    else:
        index = int(hardlar_soni / 2)
        print(i[int(index)])

