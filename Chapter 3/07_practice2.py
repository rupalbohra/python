letter = '''
Dear <|NAME|>,

Greetings from ABC coding house. I am happy to tell you about your selection.

You are selected!

Have a great day.
Date: <|DATE|>
'''
name = input("Enter your name: ")
date = input("Enter date:")
letter = letter.replace("<|DATE|>", date) 
letter = letter.replace("<|NAME|>", name) 
print(letter)