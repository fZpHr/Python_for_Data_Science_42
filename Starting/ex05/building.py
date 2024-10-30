import sys


def main():
    """
    Main function to analyze the text provided via
    command line argument or standard input.

    The function counts and prints the number of:
    - Uppercase letters
    - Lowercase letters
    - Punctuation marks
    - Spaces
    - Digits

    Usage:
        python building.py text
        or
        python building.py (without text to read from standard input,
        press Ctrl+D to finish)

    If more than one command line argument is provided,
    the function prints a usage message and exits.

    Returns:
        None
    """
    if len(sys.argv) > 2:
        print("Usage: python building.py <text>")
        sys.exit(1)
    if len(sys.argv) == 1:
        text = sys.stdin.read()
    else:
        text = sys.argv[1]
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0
    punctuation_list = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in text:
        if c.isupper():
            upper_count += 1
        if c.islower():
            lower_count += 1
        if c in punctuation_list:
            punctuation_count += 1
        if c.isspace():
            space_count += 1
        if c.isdigit():
            digit_count += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    main()
