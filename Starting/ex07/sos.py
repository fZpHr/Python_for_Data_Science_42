import sys


def convert(s):
    """
    Convert a string to its Morse code representation.

    Parameters:
    s (str): The input string to be converted to Morse code.

    Returns:
    list: A list of Morse code strings corresponding to each character in the input string.
          If a character in the input string does not have a Morse code representation,
          None is returned for that character.
    """
    dict_morse = {
        "A": ".-",
        "a": ".-",
        "B": "-...",
        "b": "-...",
        "C": "-.-.",
        "c": "-.-.",
        "D": "-..",
        "d": "-..",
        "E": ".",
        "e": ".",
        "F": "..-.",
        "f": "..-.",
        "G": "--.",
        "g": "--.",
        "H": "....",
        "h": "....",
        "I": "..",
        "i": "..",
        "J": ".---",
        "j": ".---",
        "K": "-.-",
        "k": "-.-",
        "L": ".-..",
        "l": ".-..",
        "M": "--",
        "m": "--",
        "N": "-.",
        "n": "-.",
        "O": "---",
        "o": "---",
        "P": ".--.",
        "p": ".--.",
        "Q": "--.-",
        "q": "--.-",
        "R": ".-.",
        "r": ".-.",
        "S": "...",
        "s": "...",
        "T": "-",
        "t": "-",
        "U": "..-",
        "u": "..-",
        "V": "...-",
        "v": "...-",
        "W": ".--",
        "w": ".--",
        "X": "-..-",
        "x": "-..-",
        "Y": "-.--",
        "y": "-.--",
        "Z": "--..",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
    }
    return [dict_morse.get(c) for c in s]


def main():
    text = sys.argv[1]
    morse = convert(text)
    print(" ".join(morse))


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert sys.argv[1].isalpha() == 1, "the arguments are bad"
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
