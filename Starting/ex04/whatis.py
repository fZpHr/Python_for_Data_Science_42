import sys 

if len(sys.argv) == 1:
    sys.exit(1)
try:
    assert len(sys.argv) < 3, "more than one argument is provided"
    if sys.argv[1][0] == "-":
        sys.argv[1] = sys.argv[1][1:]
    assert sys.argv[1].isdigit(), "argument is not an integer"
    number = int(sys.argv[1])
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit(1)

