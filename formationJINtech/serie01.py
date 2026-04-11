# # first Tp
# # must added the casting here
# a = input("Saisir une valuer: ")

# b = int(a) + 1

# print(b)

# # done


# # Second TP:

# age = int(input("Enter Your Age: "))
# tall = float(input("Enter Your tall: "))

# print(f"You are {age} years old and your tall is {tall:.2f}m")

# # done


# # third TP

# distance = int(input("Enter the Distance By KiloMetre: "))
# t_ime = int(input("Enter the Time By Minute: "))

# distance = distance * 1000
# time_by_second = t_ime * 60

# fast = distance / t_ime

# print(f"you must fin this distance in {int(fast / 60)} Minutes")

# # done

# # fourth TP

# seconds = int(input('Put a seconds: '))

# hours = int(seconds / 3600)

# minute = int((seconds % 3600) / 60)

# second_s = int((seconds % 3600) % 60)

# print(f"The Seconds {seconds}  = {hours} h {minute} min {second_s} sec")

# # done

# # fifth TP

# number = int(input("enter a number: "))

# # if number % 2 != 0:
# #     div = number / 3
# #     if type(div) != type(float):
# #         print(f"Your number {number} is impair and multiple of 3 ")
# #     else:
# #         print("your numbers is impair")
# # elif number % 2 == 0:
# #     div = number / 3
# #     if type(div) != type(float):
# #         print(f"Your number {number} is pair and multiple of 3 ")
# #     else:
# #         print("your numbers is pair")
# # else:
# #     print("tanks for sharing")

# if number % 2 == 0:
#     print("This Number Is Even")
# elif number % 3 == 0 and number % 2 != 0:
#     print("This Number Is Odd, but is multiple by 3")
# else:
#     print("This Number Is not a even and not multiple by 3")

# done

# # sixth TP

# F_num = int(input("Give me the first number: "))

# S_num = int(input("Give me the second number: "))

# if F_num < 0 or S_num < 0:
#     print("the multiplication of this to numbers is negative")
# elif F_num > 0 and S_num > 0:
#     print("the multiplication of the numbers is positive")
# else:
#     print("I'm not learn this Course Thanks")

# done

# # seventh tp

# F_num = int(input("Give me the first number: "))

# S_num = int(input("Give me the second number: "))

# ope = input("Choose an operation {  *    +    -    /  }")

# if ope == "+":
#     print(f"you are choose the addition so {F_num} + {S_num}: is {F_num + S_num}")
# elif ope == "-":
#     print(f"you are choose the substr so {F_num} - {S_num}: is {F_num - S_num}")
# elif ope == "*":
#     print(f"you are choose the multiplication so {F_num} * {S_num}: is {F_num * S_num}")
# elif ope == "/":
#     print(f"you are choose the Division so {F_num} / {S_num}: is {F_num / S_num}")
# else:
#     print("i'm not learn this operation to this time see you")

# done but not there are more things must be perfect

# # eighth tp

# s_notes = 0
# s_coef = 0

# for i in range(4):
#     note = float(input(f"Enter Note {i + 1}:\t"))
#     coefficient = float(input("Enter there coefficient:\t"))

#     s_notes = (note * coefficient) + s_notes
#     s_coef += coefficient

# f_note = s_notes / s_coef

# if f_note > 10:
#     print(f"the final note is {f_note:.2f}, congratulation")
# elif f_note >= 7 and f_note < 10:
#     print(f"the final note is {f_note:.2f}, have second choice")
# elif f_note  < 7:
#     print(f"the final note is {f_note:.2f}, you are not pass")
# else:
#     print("You are not Muslim you want to dead me")

# # done

# # ninth tp

# list_article = []

# for i in range(1, 3):
#     prefix = i == 1 and "st" or i == 2 and "nd" or i > 2 and "rd" or "th"
#     nom_a = input(f"Enter the {i}{prefix} article : ")
#     quantity_a = int(input(f"Enter the Unite {i}{prefix} article : "))
#     price_a = float(input(f"Enter the Price {i}{prefix} article : "))

#     total_price = price_a * quantity_a

#     list_article.append((nom_a, total_price))

# total_price = 0
# for article in list_article:
#     total_price += article[1]

# total_price = (total_price * 0.2) + total_price


# for article in list_article:
#     print(f"Total of the L'article {article[0].upper()} : {article[1]:.2f} (HT)")

# print(f"Total Of your Facture Is : {total_price:.2f} (TTC)")

# # done



# # teeth tp

# login = input("Enter your Identifier: ")
# password = input("Enter you Password: ")
# secret = "admin"

# if login.lower() == secret and password.lower() == secret:
#     print("You are Welcome In Your Profile")
# else:
#     print("The Information Incorrect Please Checks Them!!!!")

# # done

# #Eleventh TP

# weight = float(input("Enter Your Weight: "))
# tall = float(input("Enter Your Tall: "))

# IMC = weight / tall ** 2
# Interpretation = ""


# if IMC > 40:
#     Interpretation = "Obesite Morbide ou Massive"
# elif IMC < 40 and IMC > 35:
#     Interpretation = "Obesite severe"
# elif IMC < 35 and IMC > 30:
#     Interpretation = "Obesite moderee"
# elif IMC < 30 and IMC > 25:
#     Interpretation = "Surpoids"
# elif IMC < 25 and IMC > 18.5:
#     Interpretation = "corppulence normale"
# elif IMC < 18.5 and IMC > 16.5:
#     Interpretation = "Maigreur"
# elif IMC < 16.5:
#     Interpretation = "Famine"


# print(f"After the Calculate Your Indic Of Weight you are: {Interpretation}")

# # done


# 12 TP

grade = input("Enter the grade of Employer: ")
hours = int(input("Enter the Number Of Hours: "))


list_grades = [
    {"grade": "A", "horaire traif": 200, "prime": [20, 1000]},
    {"grade": "B", "horaire traif": 150, "prime": [20, 800]},
    {"grade": "C", "horaire traif": 120, "prime": [15, 500]},
    {"grade": "D", "horaire traif": 100, "prime": [15, 350]},
    {"grade": "E", "horaire traif": 80, "prime": [10, 100]},
]

total_salary = 0

for row in list_grades:
    if grade.upper() == row["grade"]:
        prime = int(hours / row["prime"][0])
        total_salary += (hours * row["horaire traif"]) + (row["prime"][1] * prime)


print(f"Your net salary is: {total_salary}")

# done
