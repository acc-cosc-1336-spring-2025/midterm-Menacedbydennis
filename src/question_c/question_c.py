# Function to calculate bonus pay amount based on sales
def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return 'Invalid arguments'
    elif sales <= 499:
        return sales * 0.05  # 5% bonus
    elif sales <= 999:
        return sales * 0.06  # 6% bonus
    elif sales <= 1499:
        return sales * 0.07  # 7% bonus
    else:
        return sales * 0.08  # 8% bonus

# Test cases
def test_get_bonus_pay_amount():
    # Testing different sales values and expected results
    assert get_bonus_pay_amount(-1) == 'Invalid arguments'  # Invalid case
    assert get_bonus_pay_amount(200) == 10  # 5% of 200 = 10
    assert get_bonus_pay_amount(600) == 36  # 6% of 600 = 36
    assert get_bonus_pay_amount(1000) == 70  # 7% of 1000 = 70
    assert get_bonus_pay_amount(1500) == 120  # 8% of 1500 = 120
    assert get_bonus_pay_amount(2000) == 'Invalid arguments'  # Invalid case

    print("All test cases passed!")

# Run the test cases
test_get_bonus_pay_amount()

 
