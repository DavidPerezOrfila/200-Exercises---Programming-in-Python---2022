# Exercise 48
"""
The following list is given:
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
Add the file 'phone.jpg' to this list at the beginning.
Then delete the file 'ball.png'. In response, print the filenames list to the console.
Expected result:
['phone.jpg', 'view.jpg', 'bear.jpg']
"""
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
FILE = 'phone.jpg'
filenames.insert(0, FILE)
filenames.pop()
print(filenames)
