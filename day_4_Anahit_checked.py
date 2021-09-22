"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# Վաղը կնայենք։ Բայց որպես հուշում երկու ցիկլ է պետք։ Մեկով դատարկ լիստին կցում ենք դատարկ լիստեր, իսկ մյուսով ներքին
# լիստերն ենք լցնում։

# for i in range(1,10):

 #չկարողացա սա կատարել։

# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# Այստեղ էլ լիստի տարրերը նույնպես պետք է comprehension-ներ լինեն
# lst_2 = [i*i for i in range(1,10) for [] in range ]
# Չկարողացա մատրիցային տեսքով ներկայացնել :(



# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։

# Ճիշտ է։ Բայց մեծատառ b-ն էլ պետք է հաշվեինք։

# nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
# result = int(0)  # int() ֆունկցիան այստեղ օգտագործելու իմաստ չկա, կարելի է ուղղակի գրել result = 0
# for i in range(len(nonsense)):
#     if nonsense[i] == "b":
#         result += 1
# print(result)

# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։

# number = int(3)  # Այստեղ նույնպես int()-երի իմաստը չկա
# result = int(1)
# for i in range(1, number + 1):
#     result = result * i
#
# print(result)
