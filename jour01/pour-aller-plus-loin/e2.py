def analyze_string(input_string):
    # Check if the string contains the character 'e'
    contains_e = 'e' in input_string

    # Get all indices of 'e'
    e_indices = [index for index, char in enumerate(input_string) if char == 'e']

    # Count the frequency of the character 'e'
    e_count = input_string.count('e')

    return contains_e, e_indices, e_count

def main():
    # User inputs a string
    input_string = input("Please enter a string: ")

    # Analyze the string
    contains_e, e_indices, e_count = analyze_string(input_string)

    # Output the results
    if contains_e:
        print("The string contains the character 'e'")
        print(f"Indices of the character 'e': {e_indices}")
        print(f"Frequency of the character 'e': {e_count} times")
    else:
        print("The string does not contain the character 'e'")

if __name__ == "__main__":
    main()
