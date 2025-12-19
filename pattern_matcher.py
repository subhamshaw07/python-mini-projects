# Pattern Matcher (Frequency Analysis)
# Checks if two strings follow the same frequency pattern.

def get_frequency_pattern(text):
    # Step 1: Count frequency of each character
    # We use a dictionary where Key = Letter, Value = Count
    freq_map = {}
    
    for char in text:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
            
    # Step 2: Build the pattern list
    # Replace each character in the original text with its count
    pattern = []
    for char in text:
        count = freq_map[char]
        pattern.append(count)
        
    return pattern

def check_pattern():
    print("--- Pattern Matcher ---")
    s1 = input("Enter first string (e.g., 'egg'): ")
    s2 = input("Enter second string (e.g., 'add'): ")
    
    # Validation: Lengths must be equal
    if len(s1) != len(s2):
        print("False: Strings are different lengths.")
        return

    # Get patterns for both
    pattern1 = get_frequency_pattern(s1)
    pattern2 = get_frequency_pattern(s2)
    
    print(f"'{s1}' pattern: {pattern1}")
    print(f"'{s2}' pattern: {pattern2}")
    
    if pattern1 == pattern2:
        print("True: Patterns match!")
    else:
        print("False: Patterns do not match.")

if __name__ == "__main__":
    check_pattern()
