# Python code to demonstrate
# insertion of items in beginning of ordered dict
from collections import OrderedDict

# initialising ordered_dict
iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# inserting items in starting of dict
iniordered_dict.update({'manjeet':'3'})
iniordered_dict.move_to_end('manjeet', last = False)

# print result
print ("Resultant Dictionary : "+str(iniordered_dict))
