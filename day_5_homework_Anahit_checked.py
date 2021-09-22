"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։

# lst = [1, 6, 7, 8, 9, 10]
# prod = 1
# for i in lst:
#     prod *= i
# print(prod)

# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող այն լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։

# lst_1 = ["Man", "madam", "ok", "kk", "kick", "statistics"]
# counter = 0
# for item in lst_1:
#     if len(item) >= 2:
#         if item[0] == item[-1]:
#             counter += 1
# print(counter)

# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։

# lst_2 = ["Value1", "Value2","Value1","Value4",] # Վերջին ստորակետը ավելորդ է։ Բացատները չենք մոռանում ստորակետներից հետո
# lst_3 = []
# for i in lst_2:
#     if i not in lst_3:
#         lst_3.append(i)
#
# print(lst_3)

# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից
# a = int(input("Please enter any number: "))  # Կարելի է ցիկլով անել։ Մեծ քանակի input-ների համար այս մոտեցումը հարմար չէ
# b = int(input("Please enter any number: "))
# c = int(input("Please enter any number: "))
# d = int(input("Please enter any number: "))
# e = int(input("Please enter any number: "))
#
# lst_4 = [a, b, c, d, e]
# print(lst_4)


# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։

lst = ['Rock', 'Pop', 'Metal','Hip-Hop', 'Rap']

# lst.pop(1)
# lst.pop(2)
# lst.pop(2)
# print(lst)


# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

# lst_5 = [1, 5, 4, 5, 2, 2, 6, 7]
#
# for i in lst_5:
#     if i == len(lst_5):
#         break
#     if lst_5[i:i + 1] == [2, 2]:  # Այստեղ lst_5[i:i + 1] մի երկարությամբ է, քանի որ վերջին ինդեքսը չի ներառվում կտորի
#         # մեջ։ Փորձեք ուղղել :)
#         result = True
#     else:
#         result = False  # Այս դեպքում խնդիր չի առաջանա, բայց else-ը չլիներ, ծրագիրը չէր աշխատի, որովհետև հնարավոր կլիներ
#         # մի դեպք, երբ result-ը գոյություն չէր ունենա և print(result)-ից էռոռ կստանայինք։ Այսպիսի փոփոխականները միշտ
#         # սկզբում հայտարարեք ինչ-որ նախնական արժեքով
#
# print(result)


# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:

lst_6 = [1, 4, 1, 4, 4, 5, 1, 1]

# for i in lst_6:
#     if i == 1 or i == 4:
#         result = True  # Այստեղ նույն խնդիրն է, result-ը դրսում սահմանեք
#     else:
#         result = False
#         break
# print(result)


# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ

# dic_0 = {"Key1": "Vale1", "Key2": "Value2", "Key3": "Value3", "Key4": "Value4", "Key5": "Value5"}
#
# m = input("Please enter a Key! ")
#
# if m in dic_0.keys():
#     print("This Key is already existing!")
# else:
#     dic_0 = dic_0.update({m: "Value6"})
#     print(dic_0)

# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։

# dic_1 = {"Key1": "Vale1", "Key2": "Value2", "Key3": "Value3", "Key4": "Value4", "Key5": "Value5"}
#
# lst_7 = list(dic_1.values())
# # Պահանջվում էր օգտագործել ցիկլ։ Այսինքն ցիկլի մեջ append-ի միջոցով պետք է ավելացնել տարրերը
# print(lst_7)

# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։

d = dict()
for i in range(1,16):
    d[i] = i ** 2

print(d)

"""Ընդհանուր լավ է Անահիտ ջան"""
