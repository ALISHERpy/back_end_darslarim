# import random
#
# son = (random.randint(1, 100))
# matn = "men o'ylagan sonni kirting: "
# while True:
#     x = int(input(matn))
#     if son == x:
#         print("to'g'ri !!")
#         break
#     else:
#         print("yo'q topa olmadinggiz qaytadan urunib ko'ring")
#     if son > x:
#         print(f"men o'ylagan son {x} dan KATTA !!")
#     else:
#         print(f"men o'ylagan son {x} dan KICHIK !!")
from idlelib.pyshell import idle_showwarning

##________________________________________-

# mylist=[3,4,5]
# second_one=[]
# for x in mylist:
#     summasi=1
#     for son in range(1,x+1):
#         summasi*=son
#     second_one.append(summasi)
# print(second_one)
##________________________________________-

# i=1
# while i <= 5:
#     print(i)
#     i += 1  # i ni 1 ga oshiramiz
# if True:
#     print("bajariladi")
##________________________________________
# i=4
# while True:
#     if i >= 14:
#         break
#     print("Cheksiz tsikl")
#     i+=3
##________________________________________-
# parol = str()
# while parol != "parol02":
#     parol = input("Parolni kiriting: ")
#     if parol !='parol02':
#         print("xato parol qayta uruning ! ")
# print("Parol to'g'ri!")
##________________________________________-
## Sonlarni yig'indisini hisoblash:
# n = 1
# yigindi = 0
# while n <= 10:
#     yigindi += n
#     n += 1
# print("1 dan 10 gacha sonlar yig'indisi:", yigindi)

##________________________________________
# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# ### print('nexia' in cars)
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)
##________________________________________-
# i=1
# while 1<6:
#     if i == 3:
#         print("if ichiamiz")
#         break
#     print(i)
#     i+=1
##________________________________________-
# string1 = "98765"
# string2 = "Ninja" #
# print(string1.isdigit()) #faqat raqammi ?
# print(string2.isdigit())
# print(string1.isalpha()) #faqat harfmi ?
# print(string2.isalpha())
##________________________________________

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# try:
#     while qiymat != 'exit':
#         qiymat = input(savol)
#         if qiymat != 'exit':
#             print(float(qiymat)**2)
#
#     print("dastur to'xtadi")
# except:
#     print("nomalum xatolik yuz berdi bir necha daqiqadan so'ng urunib ko'ring ! ")
##_____________________yuqoridagi try exceptdan foydalanib isdigit() ni qo'lda yozib chiqila___________________-

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

##________________________________________
# parol = input("Parolni kiriting: ")
# ## parol="1525bobur"
# if (
#     len(parol) >= 8  # Uzunligi 8 ta belgidan kam bo'lmasligi kerak
#     and any(x.isdigit() for x in parol)  # Kamida 1 ta raqam
#     and any(y.isupper() for y in parol)  # Kamida 1 ta katta harf
#     and any(a.islower() for a in parol)  # Kamida 1 ta kichik harf
#     and any(b in "!@#$%^&*()-_+=<>?/|~`" for b in parol)  # Maxsus belgi
# ):
#     print("Parol kuchli!")
# else:
#     print("Parol kuchli emas!")

##________________________________________
# import re
# parol = input("Parolni kiriting: ")
#
# # Regular expression sharti
# pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$])[A-Za-z\d@$!%*?&]{8,}$"
# if re.match(pattern, parol):
#     print("Parol kuchli!")
# else:
#     print("Parol kuchli emas!")
##________________________________________-

# import lesson7
# print(lesson7.ism)