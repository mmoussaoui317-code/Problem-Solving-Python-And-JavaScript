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

# # TP 04


# firstList = [1,-30,0,-2,500,4,2,100, -7]

# orderList = []

# count = len(firstList)

# place = 0

# print(firstList)

# for i in range(count):
#     if firstList[i] < 0:
#         orderList.insert(place, firstList[i])
#         place += 1
#     else:
#         print(place + i, i)
#         orderList.insert(place + i, firstList[i])
#         print(orderList)



# print(orderList)

# # done

# # # TP 05 : insert value val in list sorted

# def insertToStored(val):
#     list = [100, 200, 300, 400, 500, 10, 5, 2,  1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
#     # list.append(val)
#     list.sort()
#     # return list
#     for el in list:
#         if el > val:
#             list.insert(list.index(el), val)
#             return list

# print(insertToStored(5))
# print(insertToStored(-100))
# print(insertToStored(50))

# # # done

# # # TP06: 


# arrNbs = [1, 1, 1, 11, 44, 78, 7, 7, 100, 78]

# try:
#     nbr = int(input("Give me the Numbers :"))
    
#     arrNbs =  [i for i in arrNbs if i != nbr]

# except:
#     print("The value isn't a number")

# print(arrNbs)

# # # Done

# # # TP 07: programme deleting the repeated values

# def deletingRepeated(L = []): 
#     tb = []
#     for nb in L: 
#         if nb not in tb:
#             tb.append(nb)
#     return tb

# print(deletingRepeated([1,2,5,8,6,2,5,9,1,8,8]))

# # # done