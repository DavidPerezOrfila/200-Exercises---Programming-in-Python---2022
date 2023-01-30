# Exercise163
'''Using the random built-in module set the random seed as follows:
random.seed(12)
And select randomly (pseudo-randomly) an item from the list below:
items = ['python', 'java', 'sql', 'c++', 'c']
Print the result to the console.
Expected result:
c++'''
import random as r

r.seed(12)
items = ['python', 'java', 'sql', 'c++', 'c']
result = r.choice(items)
print(result)
