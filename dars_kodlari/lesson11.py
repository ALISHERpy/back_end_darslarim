# mylist=['ali',1223,43,'vali',True]
#
# # for element in mylist:
# #     if element == 43:
# #         break
# #     else:
# #         print(element)
# # while mylist:
# #     print(mylist.pop())
# # qiymat=12
# # while qiymat:
# #     print("1-sikl ketdi")
#     # del qiymat
###########____________________
# def faktorial(n):
#     if n == 1:  # Bazaviy holat (rekursiya to‘xtaydi)
#         return 1
#     return n * faktorial(n - 1)  # Funksiya o‘zini chaqiradi
#
# print(faktorial(5))  # Natija: 120
###########____________________
# def hisobla(n):
#     if n == 0:  # Bazaviy holat
#         return
#     print(n)
#     hisobla(n - 1)
# hisobla(5)
#########_______________
# Example: Check if a number is even or odd
# check = lambda x: "juft" if x % 2 == 0 else "toq"
# print(check(4))
# print(check(7))
#########_______________
# x=4
# check = "juft" if x % 2 == 0 else "toq"
# print(check)

####______________
# Example: Check if a number is positive, negative, or zero
# n = lambda x: "musbat" if x > 0 else "manfiy" if x < 0 else "nol"
#
# print(n(5))
# print(n(-3))
# print(n(0))
# #########_____________
# y=5
# if y>0:
#     print("musbat")
# else:
#     if y<0:
#         print("mnfiy")
#     else:
#         print("nol")

########___________
# Example: Perform addition and multiplication in a single line
# calc = lambda x, y: (x + y, x * y)
#
# res = calc(3, 4)
# print(res)

########_____________________

# raqamlar = [1, 2, 3, 4]
# kvadratlar = list(map(lambda x: x ** 2, raqamlar))
# print(kvadratlar)  # Natija: [1, 4, 9, 16]

# for element in raqamlar:
#     kvadratlar.append(element**2)
########_____________________
# Example: Double each number in a list
# a = [1, 2, 3, 4]
# b = map(lambda x: x * 2, a)
# print(list(b))
########_____________________
# raqamlar = [1, 2, 3, 4, 5, 6]
# juft_sonlar = list(filter(lambda x: x % 2 == 0, raqamlar))
# print(juft_sonlar)  # Natija: [2, 4, 6]
########_____________________
# sonlar = [-10, -5, 0, 5, 10]
# manfiy_sonlar = list(filter(lambda x: x < 0, sonlar))
# print(manfiy_sonlar)
########_____________________

# sozlar = ["salom", "dunyo", "Python", "filter", "misol"]
# uzoq_sozlar = list(filter(lambda x: len(x) > 5, sozlar))
# print(uzoq_sozlar)  #

########_____________________

# satrlar = ["salom", "", "Python", "", "filter"]
# bosh_bolmagan = list(filter(lambda x: x != "", satrlar))
# print(bosh_bolmagan)

########_____________________
