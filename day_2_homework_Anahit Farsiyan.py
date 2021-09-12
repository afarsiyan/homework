"""VARIABLES, TYPES, MAINLY STRINGS"""

# 1. Given the radius of a circle, compute its area.
#    Տրված է շրջանագծի շառավիղը։ Հաշվել մակերեսը։
import math

# r = 12
# print(r**2*math.pi)


# 2. Write a program that asks for users name and surname. Then print the reverse of their name and surname separated
# by a space.
# Գրել ծրագիր, որն օգտատիրոջից կպահանջի անունը և ազգանունը։ Այնուհետև տպել անունն ու ազգանունը տառերի հակառակ
# հերթականությամբ և առանձնացված բացատով։

# Name=input("Please enter your name: ")
# print(Name)
# Surname=input("Please enter your surname: ")
# print(Surname)
#
# print(Name[::-1],Surname[::-1])

# 3. Given a three-digit number, print its digits on separate lines. DO NOT convert the number into a string.
# Տրված է եռանիշ թիվ։ Տպել թվի բոլոր թվանշաններն առանձին տողերի վրա, միայն հանրահաշվական գործողություններով,
# ԱՌԱՆՑ փոխակերպելով string-ի։

# n = 534
# a=math.floor(n/100)
# print(a)
#
# b=math.floor(n/10)-a*10
# print(b)
#
# c=n-100*a-10*b
# print(c)



# 4. Find the remainder of 418 dividing by 16.
# Գտնել 418-ի և 16-ի բաժանման մնացորդը։

# print(418%16)

# 5. Ask the user to input a number. Print the negative of the square of that number.
# Գրել ծրագիր, որն օգտատիրոջից կպահանջի ներմուծել թիվ։ Այնուհետև տպել այդ թվի քառակուսու բացասականը։

# x=input("Please input a number: ")
# print(int(x)**2*(-1))


# 6. Ask the user to input a number. Then print the number, its square and its cube in a following format (for n = 3):
# Գրել ծրագիր, որն օգտատիրոջից կպահանջի։ Այնուհետև տպել այդ թիվը, դրա քառակուսին և խորանարդը հետևյալ ֆորմատով՝

# Number:       3
# Square:       9
# Cube:        27

n=input("Please enter any number: ")
# print(int(n))
# print(int(n)**2)
# print(int(n)**3)

# 7. Given an integer, print base-2, base-8 and base-16 versions of that number. Formatting must be as in previous
# exercise.
# Տպել տրված ամբողջ թիվը երկուական, ութական և տասնվեցական համակարգում։ Ֆորմատավորումը կատարել նախորդ վարժության պես։



# 8. Given x, calculate the following expression -> x * x + 4 * x - 19.
# Հաշվել հետևյալ արտահայտությունը պատահական իքսի համար     ^

# x=input("Please input any number: ")
# print(int(x)**2+4*int(x)-19)

# 9. Ask the user to input 2 numbers. Print the whole expression of the sum of these numbers, e.g. '4 + 3 = 7'
# Գրել ծրագիր, որն օգտատիրոջից կպահանջի երկու թիվ։ Տպել այդ թվերի գումարման ողջ արտահայտությունը։     ^

# X1=input("Please input any number: ")
# X2=input("Please input any number: ")
# print(int(X1)+int(X2))

# 10. Ask the user to input a number. Check if the number is larger than 12 and smaller than 35.
# Գրել ծրագիր, որն օգտատիրոջից կպահանջի թիվ։ Ստուգել, արդյո՞ք այդ թիվը [12,35] միջակայքում է։

# x=input("Please input any number: ")
# print(12<=int(x)<=35)
