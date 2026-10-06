def find_duplicates(numbers):
    seen = set()
    duplicates = []

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 2, 3, 4, 4]))
    print(find_duplicates([5, 5, 6, 7, 7]))