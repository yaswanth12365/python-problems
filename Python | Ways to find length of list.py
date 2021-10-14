# Python code to demonstrate
# length of list
# using len() and length_hint
from operator import length_hint

# Initializing list
test_list = [ 1, 4, 5, 7, 8 ]

# Printing test_list
print ("The list is : " + str(test_list))

# Finding length of list
# using len()
list_len = len(test_list)

# Finding length of list
# using length_hint()
list_len_hint = length_hint(test_list)

# Printing length of list
print ("Length of list using len() is : " + str(list_len))
print ("Length of list using length_hint() is : " + str(list_len_hint))
