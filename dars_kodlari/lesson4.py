# x = 55
#
# if x == 5:
#     print("x 5 ga teng")
# else:
#     print("x 5ga teng emas")  # Bu chop etiladi, chunki x 5 dan kichik.


# x = 576543
#
# if x < 5:
#     print("x 5 dan kichik")
# elif x == 5:
#     print("x 5 ga teng")
# else:
#     print("x 5 dan katta")  # Bu chop etiladi, chunki x 5 dan katta.
#


# x = 10
# y = 15
# if x>5 or y>55555:
#     print("okey")
# if x < 5:
#     if y > 10000000:
#         print("x 5 dan katta va y 10 dan katta")  # Bu yerda har ikkala shart ham rost.
# else:
#     # print("X tekshiruvning else statment")
#     print("elsening davomig")
# print("hamma tekshiruvlardan tahqariagi text")



# x = 7
# natija = "Katta" if x > 5 else "Kichik"
# print(natija)  # Chop etadi: Katta
#
# if x>5:
#     natija="katta"
# else:
#     natija="kichik"
# print(natija)

# yosh = int(input("Yoshingizni kiriting: "))
#
# if yosh < 18:
#     print("Siz hali voyaga yetmagansiz.")
# elif yosh == 18:
#     print("Siz roppa rosa 18da ekansiz !")
# else:
#     print("Siz voyaga yetgansiz.")

# son = int(input("Sonni kiriting: "))
#
# if son > 0:
#     print("Bu son musbat.")
# elif son < 0:
#     print("Bu son manfiy.")
# else:
#     print("Bu nol.")

# ball = float(input("Imtihon ballingizni kiriting: "))
#
# if not (ball>0 and ball <=100):
#     print("Nol va 100 oralig'ida son kiriting")
# elif ball >= 90:
#     print("Sizning bahoyingiz: 5")
# elif ball >= 80:
#     print("Sizning bahoyingiz: 4")
# elif ball >= 70:
#     print("Sizning bahoyingiz: 3")
# elif ball >= 60:
#     print("Sizning bahoyingiz: 2")
# else:
#     print("Siz yiqilgansiz")

#UY ISHI

# 1. Ko‘p shartli uchburchak aniqlash
# Foydalanuvchidan uchburchakning uch tomonini kiritishni so‘rang
# va bu tomonlardan uchburchak yasash mumkin yoki yo‘qligini tekshiring.
# Keyin uchburchak turini aniqlang:
#
# Teng tomonli,
# Teng yonli,
# Turli tomonli.

# a = float(input("1-tomon uzunligini kiriting: "))
# b = float(input("2-tomon uzunligini kiriting: "))
# c = float(input("3-tomon uzunligini kiriting: "))
#
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Bu teng tomonli uchburchak.")
#     elif a == b or b == c or a == c:
#         print("Bu teng yonli uchburchak.")
#     else:
#         print("Bu turli tomonli uchburchak.")
# else:
#     print("Bu tomonlar bilan uchburchak yasab bo‘lmaydi.")



# a=float(input("1-son: "))
# b=float(input("2-son: "))
# a=0 if a<b else a
# print(a)

# def kabisa_yilimi(yil):
#     if yil > 0:
#         if yil % 4 == 0:
#             if yil % 100 != 0:
#                 print("Bu kabisa yili")
#             else:
#                 if yil % 400 == 0:
#                     print("Bu kabisa yili")
#                 else:
#                     print("Bu kabisa yili emas")
#         else:
#             print("Bu kabisa yili emas")
#     else:
#         print("Xato: yilda 0 yoki manfiy qiymat bo'lishi mumkin emas!")
#
#
# kabisa_yilimi(2024)
# kabisa_yilimi(1900)
# kabisa_yilimi(2000)
# kabisa_yilimi(-2024)
