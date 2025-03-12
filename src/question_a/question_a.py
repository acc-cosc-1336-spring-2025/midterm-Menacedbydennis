## Function to get assessment value (60% of actual value)
def get_assessment_value(value):
    return value * 0.60

# Function to get tax assessed (72¢ for each $100 of assessment value)
def get_tax_assessed(assessment_value):
    return (assessment_value / 100) * 0.72

# Test cases for get_assessment_value function
def test_get_assessment_value():
    assert get_assessment_value(10000) == 6000
    assert get_assessment_value(20000) == 12000
    print("get_assessment_value tests passed!")

# Test cases for get_tax_assessed function
def test_get_tax_assessed():
    assert get_tax_assessed(6000) == 43.20
    assert get_tax_assessed(10000) == 72
    print("get_tax_assessed tests passed!")

# Main program loop
def main():
    # Run tests
    test_get_assessment_value()
    test_get_tax_assessed()

    while True:
        # Prompt user for actual value of the property
        try:
            actual_value = float(input("Enter the actual value of the property (or type 'quit' to exit): "))
            assessment_value = get_assessment_value(actual_value)
            tax = get_tax_assessed(assessment_value)

            print(f"Assessment Value: ${assessment_value:.2f}")
            print(f"Property Tax: ${tax:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit' to exit.")
            continue
        
        # Ask the user if they want to quit
        continue_input = input("Do you want to enter another value? (yes/no): ").strip().lower()
        if continue_input == 'no':
            print("Goodbye!")
            break

# Call the main function to run the program
if __name__ == "__main__":
    main()