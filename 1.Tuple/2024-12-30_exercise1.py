# reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
tuple1[::-1]

# access value 20 from the tuple
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
tuple2[1][1]


# create a tuple with single item 50
tuple3 = (50, )
tuple3

# unpack the tuple into 4 variables
tuple4 = (10, 20, 30, 40)
a, b, c, d = tuple4

# swap two tuples in Python
tuple5 = (11, 22)
tuple6 = (99, 88)

tuple5, tuple6 = tuple6, tuple5
tuple5
tuple6


# copy specific elements from one tuple to a new tuple
# write a program to copy elements 44 and 55 from the following tuple into a new tuple
tuple7 = (11, 22, 33, 44, 55, 66)
tuple8 = tuple7[3:5] # or tuple7[3:-1]
tuple8

# write a program to modify the first item (22) of a list inside a following tuple to 222
tuple9 = (11, [22, 33], 44, 55)
tuple9[1][0]=222
tuple9

# sort a tuple of tuples by 2nd item
tuple10 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple(sorted(list(tuple10), key=lambda x: x[1]))

# count the number of occurrences of item 50 from a tuple
tuple11 = (50, 10, 60, 70, 50)
tuple11.count(50)

# check if all items in the tuple are the same
tuple12 = (45, 45, 45, 45)

def check_dupe(tuple):
    return all(item == tuple[0] for item in tuple)

check_dupe(tuple12)