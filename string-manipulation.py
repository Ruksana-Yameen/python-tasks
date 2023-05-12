input_string = input("Enter a string: ")

print("Original string:", input_string)

uppercase_string = input_string.upper()
print("Uppercase string:", uppercase_string)

lowercase_string = input_string.lower()
print("Lowercase string:", lowercase_string)

word_list = input_string.split()
print("List of words:", word_list)

character_count = len(input_string.replace(" ", ""))
print("Character count:", character_count)

# Reverse the string
reverse_string = input_string[::-1]
print("Reversed string:", reverse_string)
