#Function to reverse a string using a while loop
def reverse_string(string1):
    reversed_string = ""  # Initialize an empty string to store the reversed string
    index = len(string1) - 1  # Start at the last character of the string

    # While loop to iterate over the string in reverse order
    while index >= 0:
        reversed_string += string1[index]  # Add the current character to the reversed string
        index -= 1  # Move to the previous character

    return reversed_string

# Test cases for reverse_string function
def test_reverse_string():
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("hello") == "olleh"
    print("reverse_string tests passed!")

# Main program loop
def main():
    # Run tests
    test_reverse_string()

    while True:
        # Prompt the user for a string
        string_input = input("Enter a string to reverse (or type 'quit' to exit): ")

        if string_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Call reverse_string to get the reversed string
        reversed = reverse_string(string_input)
        print(f"The reverse of '{string_input}' is '{reversed}'.")

# Call the main function to run the program
# Function to reverse a string using a while loop
def reverse_string(string1):
    reversed_string = ""  # Initialize an empty string to store the reversed string
    index = len(string1) - 1  # Start at the last character of the string

    # While loop to iterate over the string in reverse order
    while index >= 0:
        reversed_string += string1[index]  # Add the current character to the reversed string
        index -= 1  # Move to the previous character

    return reversed_string

# Test cases for reverse_string function
def test_reverse_string():
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("hello") == "olleh"
    print("reverse_string tests passed!")


    