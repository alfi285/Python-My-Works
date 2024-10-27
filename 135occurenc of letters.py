def count_characters(input_string):
    # Initialize empty dictionary
    char_count = {}

    # Iterate over each character in the string
    for char in input_string:
        # Convert to lowercase for case-insensitive counting
        char = char.lower()

        # Check if character is already in dictionary
        if char in char_count:
            # Increment count if present
            char_count[char] += 1
        else:
            # Initialize count to 1 if absent
            char_count[char] = 1

    return char_count

# Test the function
input_str = input("Enter a string: ")
result = count_characters(input_str)

# Print character counts
print("Character Counts:")
for char, count in result.items():
    print(f"{char}: {count}")

