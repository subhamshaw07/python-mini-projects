# PIN Matching Program
# This program validates a 4-digit PIN using arithmetic operators for digit extraction.

def check_pin():
    # 1. The stored correct PIN
    correct_pin = 5432
    
    # 2. Get user input
    try:
        user_entry = int(input("Enter a 4-digit PIN: "))
    except ValueError:
        print("Error: Please enter numbers only.")
        return

    # Check if entry is actually 4 digits
    if user_entry < 1000 or user_entry > 9999:
        print("Error: Please enter exactly 4 digits.")
        return

    # 3. Extract digits from the USER'S entry using Math
    # Example: 1234
    # Thousands: 1234 // 1000 = 1
    # Hundreds: (1234 % 1000) // 100 = 2
    # Tens: (1234 % 100) // 10 = 3
    # Ones: 1234 % 10 = 4
    
    u_digit1 = user_entry // 1000
    u_digit2 = (user_entry % 1000) // 100
    u_digit3 = (user_entry % 100) // 10
    u_digit4 = user_entry % 10

    # 4. Extract digits from the CORRECT PIN (for comparison)
    c_digit1 = correct_pin // 1000
    c_digit2 = (correct_pin % 1000) // 100
    c_digit3 = (correct_pin % 100) // 10
    c_digit4 = correct_pin % 10

    # 5. Logic Logic & Comparison
    if user_entry == correct_pin:
        print("Access Granted")
        
    elif (u_digit1 == c_digit1) and (u_digit2 == c_digit2):
        # First 2 digits are correct, but the whole PIN is not
        print("Partially Correct: You are close (First 2 digits matched)")
        
    else:
        print("Access Denied")

# Run the function
if __name__ == "__main__":
    check_pin()
