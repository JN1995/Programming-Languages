## For Loop

# How to define a for loop 
# For loop with: 
# list
# String
# Tuple
# Dictionary


my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)
    
for num in my_list:
    if num % 2 == 0:
        print(num)
        
for num in my_list:
    if num % 2 != 0:
        print(num)
        
my_list = [1,2,3,4,5]
list_sum = 0

for num in my_list:
    list_sum = list_sum + num
print(list_sum)


my_string = "Hello World"

for letter in my_string:
    print(letter)
    
for i in "string":
    print(i)
    
my_list = [(1,2), (3,4), (5,6), (7,8)]
len(my_list)

for tup in my_list:
    print(tup)

for a,b in my_list:
    print(a,b)
    
    
for a,b in my_list:
    print(b)
    

my_list = [(1,2,3), (4,5,6), (7,8,9)]

for a,b,c in my_list:
    print(b,c)

# tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for num in my_tuple:
    print (num)

    
my_dict = {"k1":1, "k2":2, "k3":3}

for i in my_dict:
    print(i)
    
for i in my_dict.items():
    print(i)
    
for a,b in my_dict.items():
    print(b)
 
