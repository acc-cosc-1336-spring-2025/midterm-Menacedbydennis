import question_a # Assuming question_a contains the required functions
# Main program loop
def main():
    while True:
        try:
            actual_value = float(input("Enter the actual value of the property: "))
            assessment_value = question_a.get_assessment_value(actual_value)
            tax_assessed = question_a.get_tax_assessed(assessment_value)
            
            print(f"Assessment value: ${assessment_value:.2f}")
            print(f"Property tax: ${tax_assessed:.2f}")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        if input("Do you want to enter another property value? (yes/no): ").strip().lower() == 'no':
            break

# Run the program
if __name__ == "__main__":
    main()

