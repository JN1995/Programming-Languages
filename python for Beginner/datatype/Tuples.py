## Tuple's ##

# 1) Define a Tuple
# 2) Indexing in Tuple's
# 3) Difference between the List and Tuple

# 1) Define a Tuple

prime_numbers = (2,3,5,7,11)
type(prime_numbers)

perfect_squares = [1,4,9,16,25,36]
type(perfect_squares)

len(prime_numbers)
len(perfect_squares)

my_tuple = ("Hieee", 100, 12.47)
my_tuple
type(my_tuple)

# 2) Indexing in Tuple's
my_tuple[0]
my_tuple[1]
my_tuple[0:2]
my_tuple[-1]

my_tuple.count(100)


# 3) Difference between the List and Tuple

l = ["a", "b", "c", "d", "e"]
t= ("a", "b", "c", "d", "e")
type(l)
type(t)

l[0] = "New Element"
l
t[0] = "New Element" # tuple is immutable sequence of objects
