## List's ##

# 1) concatenation
# 2) Define empty list
# 3) Indexing in list
# 4) Editing the list's
# 5) Add list into list
# 6) Python in-build functions with the list's

my_list = ["Hello", 100, 23.47]
print(my_list)

second_list = ["one", "two", "three"]
print(second_list)

print(my_list, second_list)

# 1) concatenation

new_list = my_list + second_list
print(new_list)

# 2) Define empty list
empty_list = []
print(empty_list)

# 3) Indexing in list

students = ["Robert", "Chris", "Katarina", "Scarlett"]
students

students[0]
students[2]
students[-1]
students[0:2]

# 4) Editing the list's

# Replace values
students[0] = "Sam"
students

# Add values
students.append("Paul")
students

# Remove values
students.remove("Scarlett")
students

list1 = ["one", "two", "three", "four", "five"]
list1
list1.pop()

list1.pop(0)
list1

# 5) Add list into list
color = ["Red", "Green", "Blue", "Violet"]
color
age = [21, 23, 25, 27]
age

color.extend(age)
color


# 6) Python in-build functions with the list's
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
numbers

print(sorted(numbers))

len(numbers)
max(numbers)
min(numbers)
