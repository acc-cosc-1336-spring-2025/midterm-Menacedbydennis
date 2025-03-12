import question_b
# Main program loop
def main():
    # Run tests
    question_b.test_reverse_string()

    while True:
        # Prompt the user for a string
        string_input = input("Enter a string to reverse (or type 'quit' to exit): ")

        if string_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Call reverse_string to get the reversed string
        reversed = question_b.reverse_string(string_input)
        print(f"The reverse of '{string_input}' is '{reversed}'.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
