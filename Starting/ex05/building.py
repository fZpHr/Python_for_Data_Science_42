import sys
import string

def main():
    """
    @brief Main function that processes a given text and counts the number of upper case letters, 
    lower case letters, punctuation marks, spaces, and digits.

    Usage:
        python building.py <text>

    Arguments:
        <text> : str : The text to be analyzed.

    Prints:
        A summary of the counts of different types of characters in the text.
    """
    if len(sys.argv) != 2:
        print("Usage: python building.py <text>")
        sys.exit(1)

    text = sys.argv[1]
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for c in text:
        if c.isupper():
            upper_count += 1
        if c.islower():
            lower_count += 1
        if c in string.punctuation:
            punctuation_count += 1
        if c.isspace():
            space_count += 1
        if c.isdigit():
            digit_count += 1

    print(f"The text contains {len(text)} characters:\n{upper_count} upper letters\n{lower_count} lower letters\n{punctuation_count} punctuation marks\n{space_count} spaces\n{digit_count} digits")


if __name__ == "__main__":
    main()