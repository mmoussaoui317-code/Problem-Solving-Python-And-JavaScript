# Exercice 1
# Create un programme qui lit une list d'entier pius affiche, et affiche les pairs 


# Summer en points simples

# first creation of the list empty

list = []

# second ask the user for the number of element of the list

n = int(input("Enter the number of element of the list: "))

# third start the count

count = 1

# fourth create the list

while count <= n:
    element = int(input(f"Enter the {count} element of the list: "))
    list.append(element)
    count += 1

# fifth print the list

print("The list is: ", list)

# sixth print the pairs of the list

print("The pairs of the list are: ", [x for x in list if x % 2 == 0])