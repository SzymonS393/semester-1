# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #prints the input
print(f"Modified String 1: {user_string.lower()}") #prints the input in lowercase
print(f"Modified String 2: {user_string.upper()}") #prints the input in uppercase
print(f"Modified String 3: {user_string.strip()}") #removes spaces before and after the string
print(f"Modified String 4: {user_string.replace('a', '@')}") #replaces the letter a with @
print(f"Modified String 5: {user_string.capitalize()}") #capitalises the first letter of the string
print(f"Modified String 6: {user_string[::-1]}") #prints the string backwards
print(f"Modified String 7: {user_string.title()}") #capitalises the first letter in every word
print(f"Modified String 8: {len(user_string)}") #prints the length of the string
print(f"Modified String 9: {user_string.find('a')}") #prints the first position of the letter a
print(f"Modified String 10: {user_string.count('a')}") #prints how many times the letter a appears
print(f"Modified String 11: {user_string.startswith('Hello')}") #prints true if the string starts with Hello
print(f"Modified String 12: {user_string.endswith('!')}") #prints true if the string ends with an exclamation mark
print(f"Modified String 13: {user_string.isalnum()}") #prints true if all the characters in the string are alphanumeric
print(f"Modified String 14: {user_string.isalpha()}") #prints true if all the characters are letters
print(f"Modified String 15: {user_string.isdigit()}") # prints true if all the characters are numbers



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!