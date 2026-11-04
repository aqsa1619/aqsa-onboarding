
def calculate_payment(amount):

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    return amount


try:
    payment = calculate_payment(-500)
    print("Payment:", payment)

except ValueError as error:
    print("Error:", error)
