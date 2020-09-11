# 0 Bootcamp Hello, World!
# ======================

# lines starting with '#' are comments
# they don't get executed when you run your code

# comments are useful for telling yourself or others
# what a section of code is doing

# Test 0.0
# --------
# try getting python to print "Hello, World!"
# in the terminal to the right

# you can remove the '#' from the beginning
# of the next line, then press "Run" above
print("Hello, World!")

# For some of you this may be your first program,
# so congrats to you!

# `print` is a function that does something
# with the values you provide it.
# in this case, it prints the value in the
# terminal




















# 1 Working with data
# =================

# computers deal with data, and you can handle
# them with python

# Test 1.0
# --------
# calculate 2+2
#2+2

# see how the program doesn't show anything in
# the terminal.
# It performed the calculation, but you didn't
# tell it so print anything

# Test 1.1
# ------
# calculate 2+2 and print the result




















# 2 Assigning variables
# ===================

# you can store values in a variable
#num = 2+2
#print(num)

# we can check its value with operators like
# `==`, `>`, `<`, `>=`, and `<=`

# `num` is the variable's name
# `num` has a value of 4

# Test 2.0
# --------
# change num's value to a number greater than 100
# and check it



















# 3 Working with lists
# ==================

# we can store more than just a single value
# in a variable.
# we can store multiple values using something
# called a "list"

# here is an example list
# (defined with `[` and `]`)
#a_list = [1, 2, 3]
#print(a_list)

# we can access elements of the list with `[]`
# counting starts at 0
#print(a_list[0]) # the first element of the list
#print(a_list[1]) # the second element of the list
#print(a_list[2]) # the third element of the list

# we can select a sublist using `i:j`
# where we start at `i` and stop before `j`

# here is a list containing only the first element
#print(a_list[0:1])

# here is a list containing the first 2 elements
#print(a_list[0:2])

# here is a list containing the 2nd and 3rd elements
#print(a_list[1:3])

# Test 3.0
# --------
# what happens when we try to select elements
# after the end of the list?


# Test 3.1
# --------
# what happens when we try to select elements
# before the beginning of the list?



















# 4 Importing packages
# ==================

# people can make code for a specific purpose
# and share it with others

# this code can be loaded with `import`

# for example, python doesn't doesn't have a 
# built-in way to calculate means

# Test 4.0
# --------
# import a package called `numpy`


# Test 4.1
# --------
# calculate the mean of `a_list` using numpy's
# `numpy.mean` function
#a_list = [1, 2, 3, 6, 10]



















# 5 Working with tables
# ===================

# tables, or data frames, are objects that handle
# lots of data, split into rows and columns

# each column contains some "property" or "feature"
# that we want to look at
# each row contains an "observation" or "sample"

# a popular package to work with tables is `pandas`

# Test 5.0
# --------
# import the `pandas` package

