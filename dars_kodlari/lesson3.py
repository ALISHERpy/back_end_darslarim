####   Matematik Operatorlar (Arithmetic Operators)

# a = int(10) #int()
# b = int(3) #float()
#
# print(a + b)  # Qo‘shish: 13
# print(a - b)  # Ayirish: 7
# print(a * b)  # Ko‘paytirish: 30
# print(a / b)  # Bo‘lish: 3.3333
# print(a % b)  # Qoldiq olish: 1
# print(a ** b) # Darajaga ko‘tarish: 1000 (10^3)
# print(a // b) # Butun bo‘lish: 3


####  Taqqoslash Operatorlari (Comparison Operators)

# x = 5
# y = 10
#
# print(x == y)  # False
# print(x != y)  # True
# print(x > y)   # False
# print(x < y)   # True
# print(x >= 5)  # True
# print(y <= 10) # True

####. Mantiqiy Operatorlar (Logical Operators)

# a = True #1
# b = False #0
# c= True
# d= True
#
# print(a and b or c and d)  # False   1*0=0
# print(a or b)   # True  1+0=1
# print(not a)    # False



########    Qo‘shilish Operatorlari (Assignment Operators)


# x = int(5)
# x += 3  # x = x + 3
# print(x)  # 8
#
# x *= 2  # x = x * 2
# print(x)  # 16
#
# x -= 5  # x = x - 5
# print(x)  # 11



######   Bitwise Operatorlar
# Bu operatorlar ikkilik sonlar bilan ishlaydi:
# & (AND)
# | (OR)
# ^ (XOR)
# ~ (NOT)
# << (chapga siljitish)
# >> (o‘ngga siljitish)

# a = 5   # 0101
# b = 3   # 0011
#
# print(a & b)  # 1 (0001)
# print(a | b)  # 7 (0111)
# print(a ^ b)  # 6 (0110)
# print(~a)     # -6 (1010)
# print(a << 1) # 10 (1010)
# print(a >> 1) # 2 (0010)


#####    Identifikatsiya va A'zo Operatorlari
# Identifikatsiya operatorlari:
# is (xuddi o‘sha obyektmi?)
# is not (xuddi o‘sha obyekt emasmi?)
# Misol:

# ism="G'ofurov Abdurouf"
# print(ism)

# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]
#
# print(x is y)      # True (bir obyekt)
# print(x is z)      # False (faqat qiymat teng)
# print(x is not z)  # True

# a = [1, 21222, 13, 4]
# print(13 in a)
# print(13 not in a)
# print(1 in a)
# print(4 not in a)


# ###7. Matematik Kutubxona

# import math
#
# print(math.sqrt(16))  # 4.0 (ildiz)
# print(math.pi)        # 3.14159
# print(math.sin(math.radians(90))) # 1.0 (sinus)
# print(math.factorial(5))          # 120

