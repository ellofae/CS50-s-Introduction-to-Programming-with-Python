# Ask user for their name
name = input("What's your name? ")

#name = name.strip() # remove spaces from the left and the right the string.
#name = name.capitalize() #capitalizing the first letter
#name = name.title() # capitalizing the first letter of every word

name = name.strip().title()

# Split user's name into first name and last name:
firstName, lastName = name.split(" ")

# Say hello to user
print(f"Hello, {firstName} {lastName}")
