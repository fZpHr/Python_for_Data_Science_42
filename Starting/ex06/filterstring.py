import sys


def filter_string(S, N):
    """
    Filters words in a string based on their length.

    Args:
        S (str): The input string containing words separated by spaces.
        N (int): The minimum length of words to be included in the output list.

    Returns:
        list: A list of words from the input string that are longer than N characters.
    """
    return [x for x in S.split() if (lambda x: len(x) > N)(x)]


def main():
    print(filter_string(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit() == 1, "the arguments are bad digit"
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
