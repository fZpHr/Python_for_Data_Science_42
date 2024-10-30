def is_even(n):
    return n % 2 == 0


def ft_filter(function, iterable):
    for item in iterable:
        if function(item):
            yield item


def main():
    nb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nb2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    next_nb = ft_filter(is_even, nb)
    print(list(next_nb))
    print(next_nb)

    text = filter(is_even, nb2)
    print(list(text))
    print(text)


if __name__ == "__main__":
    main()
