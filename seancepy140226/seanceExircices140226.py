# programme take a number and print the pair or impair

# number = int(input("Enter a number: "))

# while(number != 0) :
#     if number % 2 == 0:
#         print("The number is pair")
#     else:
#         print("The number is impair")

#     number = int(input("Enter a number: "))

# programme take a number between 1 and 10 and print the multiplication table

# try :
#     number = int(input('Enter a number between 1 and 10: '))

#     while(number != 0) :
#         for i in range(1, 11) :
#             print(f"{number} x {i} = {number * i}")
#         number = int(input('Enter a number between 1 and 10: '))
# except :
#     print("Error")


# programme take a list of number and print the max

# try:
#     list = []

#     n = int(input("Enter the number of element of the list: "))

#     count = 1

#     while count <= n:
#         element = int(input(f"Enter the {count} element of the list: "))
#         list.append(element)
#         count += 1

#     print("The list is: ", list)

#     print("The max of the list is: ", max(list))
# except:
#     print("Error")

# programme compte a Rebours

# try: 
#     for i in range(10, 0, -1):
#         print(i)
#     print("Happy new year")
# except:
#     print("Error")


# programme take a list of number and print the sum of elements

# try: 
#     length = int(input("Enter the length of the list: "))

#     list = []

#     for i in range(length):
#         element = int(input(f"Enter the {i + 1} element of the list: "))
#         list.append(element)

#     print("The list is: ", list)

#     print("The sum of the list is: ", sum(list))
# except: 
#     print("Error")

# programme take 5 notes and print the average and the max and the min and the number of notes upper than 10

# try: 
#     notes = []

#     for i in range(5):
#         note = float(input(f"Enter the {i + 1} note: "))
#         notes.append(note)

#     print("The notes are: ", notes)

#     print("The average is: ", sum(notes) / len(notes))

#     print("The max is: ", max(notes))

#     print("The min is: ", min(notes))

#     print("The number of notes upper than 10 is: ", len([note for note in notes if note > 10]))
# except: 
#     print("Error")

# programme take a list of number and print the index of the element if found, -1 otherwise
# def searchInsteadList(list, ele):
#     """
#     Search an element in a list and return its index if found, -1 otherwise.

#     Parameters
#     ----------
#     list : list
#         The list to search in.
#     ele : int
#         The element to search for.

#     Returns
#     -------
#     int
#         The index of the element if found, -1 otherwise.
#     """
#     for i in range(len(list)):
#         if list[i] == ele:
#             return i
#     return -1

# try:
#     list = []

#     n = int(input('Enter the number of element of the list:'))

#     for i in range(1, n):
#         element = int(input(f"Enter the {i} element of the list: "))
#         list.append(element)

#     print("The list is: ", list)

#     ele = int(input("Enter the element to search: "))

#     print("The index of the element is: ", searchInsteadList(list, ele))
# except: 
#     print("Error")

# programme take a list of number and print filtered list of elements upper than 10

# def filterPair(list):
#     return [element for element in list if element % 2 == 0]

# try:
#     list = []

#     n = int(input('Enter the number of element of the list:'))

#     for i in range(1, n):
#         element = int(input(f"Enter the {i} element of the list: "))
#         list.append(element)

#     print("The list is: ", list)

#     print("The filtered list is: ", filterPair(list))
# except: 
#     print("Error")

# programme take a list chained and calculate the vowels

# try: 

#     n = input('Enter your string:')

#     list = []
#     for i in range(1, len(n)):
#         list.append(n[i])

#     print("The list is: ", list)

#     print("The number of vowels is: ", len([element for element in list if element in "aeiouy"]))
# except: 
#     print("Error")


# programme has a matrices and print the sum of the first line and the last line and sum of the principal diagonal

# try: 
#     list = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]

#     # for i in range(i, len(list)):
#     print("The sum of the first line is: ", sum(list[0]))

#     print("The sum of the last line is: ", sum(list[-1]))

#     print("The sum of the principal diagonal is: ", sum([list[i][i] for i in range(len(list))]))
# except: 
#     print("Error")


# programme works with algorithm of sort a bulles for sort a list ask

# try:
#     list = []

#     n = int(input('Enter the number of element of the list:'))

#     for i in range(1, n):
#         element = int(input(f"Enter the {i} element of the list: "))
#         list.append(element)

#     print("The list is: ", list)

#     for i in range(len(list) - 1):
#         for j in range(len(list) - i - 1):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]

#     print("The sorted list is: ", list)
# except: 
#     print("Error")

# programme cache a number and the user has to guess it and print the number of try

# import random

# try:
#     number = random.randint(1, 100)

#     # print("The number is: ", number)

#     n = int(input("Enter a number: "))

#     while(n != number) :
#         if n > number:
#             print("The number is lower")
#         else:
#             print("The number is higher")

#         n = int(input("Enter a number: "))

#     print("You got it")
# except: 
#     print("Error")


# programme take two list try and join them

# try:
#     list1 = [1,2,3,4,5]
#     list2 = [15,16,17,18,19]  
#     list = []
#     # for i in range(len(list2)):
#     #     list.append(list2[i])  

#     # for i in range(len(list1)):
#     #     list.append(list1[i])

#     # list = list1 + list2

#     # list.extend(list1)
#     # list.extend(list2)

#     list = list1.copy()
#     list += list2.copy()

#     print("The list is: ", sorted(list))
# except: 
#     print("Error")


# programme verify the word is palindrome

# try:
#     word = input("Enter a word: ")

#     if word == word[::-1]:
#         print("The word is palindrome")
#     else:
#         print("The word is not palindrome")
# except: 
#     print("Error")


# function take list and return new list without same elements

### with set you can need this function just one time
# def removeDuplicate(list):
#     newList = set()
#     for(i, element) in enumerate(list):
#         if element in list[i + 1:]:
#             newList.add(element)

#     return newList.tolist()
### take the word from the user and directly insert it in the set to remove the duplicate

# try: 
#     list = set()

#     n = int(input('Enter the number of element of the list:'))

#     for i in range(1, n):
#         element = input(f"Enter the {i} element of the list: ")
#         list.add(element)

#     print("The list is: ", [element for element in list])

#     # print("The new list is: ", removeDuplicate(list))
# except: 
#     print("Error")

# TP: 17 - try to calculate the some of every line and column and diagonal principal and verify if the matrix is magic square

# try: 
#     list = [
#         [1, 1, 1],
#         [1, 1, 1],
#         [1, 1, 1]
#     ]

#     for i in range(len(list)):
#         print("The sum of the line", i + 1, "is: ", sum(list[i]))

#     for i in range(len(list)):
#         print("The sum of the column", i + 1, "is: ", sum([list[j][i] for j in range(len(list))]))

#     print("The sum of the principal diagonal is: ", sum([list[i][i] for i in range(len(list))]))

#     if sum(list[0]) == sum(list[1]) == sum(list[2]) == sum([list[i][i] for i in range(len(list))]):
#         print("The matrix is magic square")
#     else:
#         print("The matrix is not magic square")
# except: 
#     print("Error")

# ** TP 18: Analyse the text and print the number of words and the number of phrases and the number of paragraphs

try:
    text = input("Enter the text: ")

    print("The number of words is: ", len(text.split()))

    print("The number of phrases is: ", len(text.split(".")))

    print("The number of paragraphs is: ", len(text.split("\n")))
except: 
    print("Error")