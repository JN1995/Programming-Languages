## Map, Filter and  Lambda Expressions

# 1) map function
# 2) filter function
# 3) lambda expression
# 4) lambda expression with map and filter function

# Map function

def cal_square(n):
    return n*n

cal_square(4)

my_num = [1,2,3,4,5]

map(cal_square, my_num)

list(map(cal_square, my_num))

for items in map(cal_square, my_num):
    print(items)
    
def len_char(c):
    return len(c)

my_char = ["Apple", "Banana", "Mushroom"]

list(map(len_char, my_char))

for items in map(len_char, my_char):
    print(items)
    
## Filter function

def even_num(n):
    return n % 2 == 0

my_num = [1,2,3,4,5,6,7,8,9,10]

list(filter(even_num, my_num))

for items in filter(even_num, my_num):
    print(items)
    
## Lambda Expressions

# Stem 1
    
def cal_square(n):
    return n*n
cal_square(3)

# Step 2

def cal_square(n):return n*n
cal_square(4)

# Step 3
    
cal_square = lambda n:n*n
cal_square(5)

my_list = [1,2,3,4,5]

list(map(cal_square, my_list))

list(map(lambda n:n*n, my_list))

# Step 1

def even_num(n):
    return n % 2 == 0

# Step 2
def even_num(n):return n % 2 == 0

# Step 3

even_num = lambda n:n % 2 == 0

my_list = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda n:n % 2 == 0, my_list))
