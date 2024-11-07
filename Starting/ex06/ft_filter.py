def is_even(n):
    return n % 2 == 0


def ft_filter(function, iterable):
    if function is None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item


def main():
    nb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_true_false = [True, False, True, False, True, False, True, False]
    list_true2_false = [True, False, True, False, True, False, True, False]
    nb2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    next_nb = ft_filter(is_even, nb)
    print(list(next_nb))
    text = ft_filter(is_even, nb2)
    print(list(text))
    next_nb = ft_filter(None, list_true_false)
    print(list(next_nb))
    text = ft_filter(None, list_true2_false)
    print(list(text))


if __name__ == "__main__":
    main()
