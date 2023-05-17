# Open the file and read its contents
with open("data.txt", "r") as file:
    data = file.read()

# Manipulate the data using string methods or regular expressions
# Example: Convert all text to uppercase
manipulated_data = data.upper()

# Display the manipulated data to the user
print("Manipulated Data:")
print(manipulated_data)
