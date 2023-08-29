Here's a simplified version of the code using Noon's algorithm:


def validate_credit_card(card_number):
    reversed_number = card_number[::-1]  # Reverse the card number
    total = 0

    for i, digit in enumerate(reversed_number):
        if i % 2 == 1:  # Double every second digit
            doubled_digit = int(digit) * 2
            if doubled_digit > 9:
                doubled_digit -= 9  # Subtract 9 from digits greater than 9
            total += doubled_digit
        else:
            total += int(digit)

    return total % 10 == 0  # Return True if total is divisible by 10, else False

# Test the algorithm with a credit card number
credit_card_number = "45320151128336"
is_valid = validate_credit_card(credit_card_number)
if is_valid:
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")


"""
This simplified code performs the same validation using Noon's algorithm. It checks the credit card number digit by digit, doubling every second digit and subtracting 9 if the result is greater than 9. The total sum is then checked if it is divisible by 10 to determine the validity of the credit card number.
"""