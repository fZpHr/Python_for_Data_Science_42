def ft_tqdm(lst: range) -> None:
    for i, elem in enumerate(lst):
        if i % 2 == 0:
            current = (i + 1) * 100 // len(lst)
            block = "█" * current
            print(f"\r{current}% |{block:<100}| {elem}/{len(lst)}", end="")
            yield
