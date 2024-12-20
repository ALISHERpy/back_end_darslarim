# x = 32
# n = 5
# ildiz = x ** (1 / n)
# print(ildiz)
from idlelib.debugobj import myrepr
from itertools import count

# import math
#
# x = 32
# n = 5
# ildiz = math.pow(x, 1 / n)
# print(ildiz)

# List yaratish
# my_list = [1, 2, 3, 'salom', 5.5,False,True]
# print(my_list)

# # Elementlarni olish
# print(my_list[0])  # 1
# print(my_list[3])  # 'salom'

# Element qo'shish
# my_list.append(6)
# my_list.append('BackEnd')
# print(my_list)  # [1, 2, 3, 'salom', 5.5, 6]

# # Element o'chirish
# my_list.remove('salom')
# print(my_list)  # [1, 2, 3, 5.5, 6]

# Elementni o'zgartirish
# my_list[1] = 'Shunqor'
# print(my_list)  # [1, 'yangi', 3, 5.5, 6]


# mylist = ["apple","banana","cherry",'apple','pamildori','kartishka','apple',11111]

# bizninglist=[122,2334,21,213]
# print(bizninglist.index(21))

# mylist.insert(3,bizninglist)
# print(mylist)
# print(mylist[3])
# print(mylist[3][2])



# print(mylist)
# mylist[2]='olcha'
# print(mylist)


# mylist[1:3] = ["watermelon"]
# print(mylist)


# mylist[1:2] = ["blackcurrant","watermelon",23232323]
# print(mylist)




# print('banana' not in mylist)
# if 'pamildori' not in mylist:
#     print("bor ekan")
# else:
#     print("yo'q ekan")


# print(mylist[2:5])
# print(mylist[-4:-1])
# print(mylist[:5])
# print(mylist[2:])
# print(mylist[-1])
# print(mylist[4])
# fullname='Alisher Axmadov Navoiy viloyatida tavallud topgan'
# print(fullname.split())
# print(mylist.count("apple"))
# print(len(mylist))
# print(type(mylist))
# print(type(1))
# print(type(3.4))


# from math import pow
# print(pow(2,3))



# from pprint import pprint
# #ppritn bu shunchaki printning chiroylirooo versiyasi
# mylist = ["apple","banana","cherry",'apple','pamildori','kartishka','apple',11111]
#
# bizninglist=[122,2334,21,213]
# bizninglist.insert(2,[1111,222,333,444])
# # print(bizninglist)
# mylist.insert(5,bizninglist)
# # pprint(mylist)
# pprint(mylist[5][2][3])


# mylist = ["apple","banana","cherry",'apple','pamildori','kartishka','apple',11111]
# bizninglist=[122,2334,21,213]
# mylist.extend(bizninglist)
# print(mylist)



# mylist = ["apple","banana",'sss',11,"cherry",'apple','pamildori','sss','kartishka',11,'apple']
# mylist=set(mylist)
# print(mylist)
# mylist.remove('apple')
# mylist.pop(1)
# print(mylist)

# mylist = ["apple","banana",'sss',"cherry",'apple','pamildori','sss','kartishka','apple']
# mylist.sort()
# print(mylist)

# mylist=[21,2,4334,1.2,1,0.5]
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)


# mylist = ["apple","banana",'sss',"cherry",'apple','pamildori','sss','kartishka']
# mylist.reverse()
# print(mylist)

# mylist = ["apple","banana",'sss',"cherry",'apple','pamildori','sss','kartishka']
# mylist2=mylist.copy()
# # print(mylist2)
#
# mylist.remove('banana')
# print(mylist)
# print(mylist2)



# mylist = ["apple","banana","cherry",'apple','pamildori','kartishka','apple',11111]
# bizninglist=[122,2334,21,213]
# print(mylist+bizninglist)

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# for obj in bozorlik:
#     print(obj," olishimiz kerak")


# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# x=(4,334,45,4225,34,34,23,23,2)
# print(type(x))
# y=list(x)
# y[2]=44
# print((y))


# Tuple yaratish
# my_tuple = (1, 2, 3, 'salom', 5.5)
#
# # Elementlarni olish
# print(my_tuple[0])  # 1
# print(my_tuple[3])  # 'salom'

# Elementni o'zgartirishga urinishda xato beradi:
# my_tuple[1] = 'yangi'  # TypeError: 'tuple' object does not support item assignment

# # Tuple ichida list saqlasa, list o'zgartirilishi mumkin:
# mixed_tuple = (1, [2, 3], 'salom')
# print(mixed_tuple)
# mixed_tuple[1][0] = 'yangi'
# mixed_tuple[1].append([1212,212])
# print(mixed_tuple)  # (1, ['yangi', 3], 'salom')



