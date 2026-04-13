# # first TP:

# number = int(input("Enter Number: "))

# total = number + int(str(number) * 2) +int(str(number) * 3) + int(str(number) * 4)

# print(f"The Equation {number} + {str(number) * 2} + {str(number) * 3} + {str(number) * 4} = {total}")

# # done

# second TP:

# endPosition = int(input("Enter The Number Of Your Polygon: "))

# for i in range(endPosition):
#     j = -1
#     while j < i:
#         print("@", end="")
#         j += 1
    
#     print("")

# # # done

# for i in range(1, 6):
#     for j in range(0, i):
#         print(i, end="")
    
#     print("")

# # done

# #  3 TP:

# import random as rd

# cached = int(rd.random() * 100)

# trying = 0


# while trying < 7:
#     user_nb = int(input("Try To Guess The Cached Number In (7 Try): "))

#     if user_nb > cached:
#         print("Very Small Then It")
#     elif user_nb < cached:
#         print("Very Big Then It")
#     elif user_nb == cached:
#         print("Yes. You Find It")
#     else: 
#         print("This Not A number")

#     trying += 1

# print(f"The Cached Number Is: {cached}")

# # done