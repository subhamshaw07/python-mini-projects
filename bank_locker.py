# Bank Locker Access System
# Validates a 6-digit code based on mathematical properties of its digits.

def check_locker_access():
    try:
        code = int(input("Enter your 6-digit locker code: "))
    except ValueError:
        print("Error: Please enter numbers only.")
        return

    # 1. Validation: Must be 6 digits (100000 to 999999)
    if code < 100000 or code > 999999:
        print("Error: Code must be exactly 6 digits.")
        return

    # 2. Separate Locker Number (First 3) and Secret Key (Last 3)
    # Example: 543120
    locker_num = code // 1000   # 543
    secret_key = code % 1000    # 120
    
    print(f"Locker Number: {locker_num}")
    print(f"Secret Key: {secret_key}")

    # 3. Calculate Sum of Locker Number Digits
    # We use a temp variable so we don't lose the original locker_num
    temp_num = locker_num
    digit_sum = 0
    
    while temp_num > 0:
        digit = temp_num % 10       # Get last digit
        digit_sum += digit          # Add to total
        temp_num = temp_num // 10   # Remove last digit

    print(f"Sum of locker digits: {digit_sum}")

    # 4. Final Check (Avoid division by zero!)
    if digit_sum == 0:
        print("Access Denied (Sum of digits cannot be zero)")
    elif secret_key % digit_sum == 0:
        print("Access Granted")
    else:
        print("Access Denied")

if __name__ == "__main__":
    check_locker_access()
