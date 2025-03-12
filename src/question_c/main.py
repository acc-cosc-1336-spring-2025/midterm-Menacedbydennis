import question_c
# Main program loop
def main():
    while True:
        try:
            sales = float(input("Enter the sales amount (or type 'quit' to exit): "))
            if sales == 'quit':
                break  # Exit if user types 'quit'

            bonus = question_c.get_bonus_pay_amount(sales)
            if bonus == 'Invalid arguments':
                print(bonus)
            else:
                print(f"Bonus: ${bonus:.2f}")
        
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
