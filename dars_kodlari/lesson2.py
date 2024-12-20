# Pythonda **o'zgaruvchilar** (variables) dasturdagi ma'lumotlarni saqlash uchun ishlatiladi. O'zgaruvchi bu nom bilan belgilangan va unda qiymat saqlanadigan joydir. O'zgaruvchi yaratishda qiymatni belgilash orqali avtomatik ravishda ma'lumot turi aniqlanadi.

# ### O'zgaruvchi yaratish
# O'zgaruvchi yaratish uchun oddiygina `=` operatoridan foydalaniladi:
# ```python
# x = 5          # Butun son
# y = "Hello"    # Matn
# z = 3.14       # O'nlik son
# ```

# ### O'zgaruvchilarga nom berish qoidalari
# 1. O'zgaruvchi nomi harf yoki pastki chiziq (`_`) bilan boshlanishi kerak. Masalan: `name`, `_age`.
# 2. Raqam bilan boshlanishi mumkin emas. Masalan, `2name` noto'g'ri.
# 3. Faqat harflar, raqamlar va pastki chiziqdan iborat bo'lishi kerak. Masalan: `my_name_1`.
# 4. Pythonning kalit so'zlaridan foydalansa bo'lmaydi (masalan, `class`, `if`, `else` va h.k.).

# ### Ma'lumot turlari
# Python o'zgaruvchilarda turli xil ma'lumot turlarini saqlash imkonini beradi:
# ```python
# x = 10            # int (butun son)
# y = 3.14          # float (o'nlik son)
# z = "Salom"       # str (matn)
# is_active = True  # bool (mantiqiy qiymat)
# ```

# ### Bir nechta o'zgaruvchini bitta qatorda yaratish
# ```python
a, b, c = 1, 2, 3
print(a, b, c)  # Natija: 1 2 3
# ```
# a, b, c = 1, 20.2, "GeeksforGeeks"

# print(a)
# print(b)
# print(c)


# a = b = c = 10

# print(a)
# print(b)
# print(c)


# ### O'zgaruvchini qayta belgilash
# O'zgaruvchi qiymatini istalgan vaqtda o'zgartirish mumkin:
# ```python
# x = 5
# x = "Dasturlash"
# print(x)  # Natija: Dasturlash
# ```

# Agar sizda boshqa savollar bo'lsa yoki amaliy yordam kerak bo'lsa, bemalol so'rang! 😊




# Pythonda **`input()`** funksiyasi foydalanuvchidan ma'lumot olish uchun ishlatiladi.
#  Ushbu funksiya foydalanuvchiga terminal yoki konsolda ma'lumot kiritish imkonini beradi.
#  Kiritilgan qiymatni string (matn) sifatida qaytaradi, shuning uchun boshqa ma'lumot turida
#  ishlatish kerak bo'lsa, kiritilgan qiymatni mos ravishda o'zgartirish kerak.

# ---

# ### `input()` funksiyasining asosiy ishlatilishi
# Foydalanuvchidan matn olish:
# ```python
# name = input("Ismingizni kiriting: ")
# print(f"Salom, {name}!")
# ```

# ---

# ### Kiritilgan qiymatni boshqa turga o'zgartirish
# Odatda, foydalanuvchi sonlar yoki boshqa ma'lumot turlarini kiritishi kerak bo'lsa, stringni mos turga aylantirish kerak:
# - **Butun son (`int`) olish:**
# ```python
# age = int(input("Yoshingizni kiriting: "))
# print(f"Siz {age} yoshdasiz.")
# ```

# - **O'nlik son (`float`) olish:**
# ```python
# height = float(input("Bo'yingizni kiriting (metr): "))
# print(f"Bo'yingiz {height} metr.")
# ```

# - **Mantiqiy qiymat (`bool`) olish:**
# ```python
# is_student = input("Talabamisiz? (ha/yo'q): ").lower() == "ha"
# print(f"Talaba: {is_student}")
# ```

# ---

# ### Misollar
# 1. **Ikki sonni qo'shish:**
# ```python
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# print(f"Natija: {a + b}")
# ```

# 2. **Oddiy kalkulyator:**
# ```python
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# operation = input("Qanday amalni bajarishni istaysiz? (+, -, *, /): ")

# if operation == "+":
#     print(f"Natija: {x + y}")
# elif operation == "-":
#     print(f"Natija: {x - y}")
# elif operation == "*":
#     print(f"Natija: {x * y}")
# elif operation == "/":
#     if y != 0:
#         print(f"Natija: {x / y}")
#     else:
#         print("Bo'lish nolga mumkin emas!")
# else:
#     print("Noto'g'ri amal tanlandi!")
# ```

# ---

# ### `input()` dan kelib chiqadigan muammolar
# 1. **String qiymatni to'g'ridan-to'g'ri son sifatida ishlatishga urinish:**
#    ```python
#    age = input("Yoshingizni kiriting: ")
#    print(age + 5)  # Xatolik: TypeError
#    ```
#    **To'g'ri yechim:**
#    ```python
#    age = int(input("Yoshingizni kiriting: "))
#    print(age + 5)
#    ```

# 2. **Bo'sh qiymat kiritilishi:**
#    Foydalanuvchi hech narsa kiritmasa, dastur noto'g'ri ishlashi mumkin. Buni tekshirish kerak:
#    ```python
#    data = input("Ma'lumot kiriting: ")
#    if not data.strip():
#        print("Hech narsa kiritilmadi!")
#    else:
#        print(f"Siz kiritdingiz: {data}")
#    ```

# ---

# Agar `input()` funksiyasiga oid boshqa savollaringiz bo'lsa, so'rashingiz mumkin! 😊