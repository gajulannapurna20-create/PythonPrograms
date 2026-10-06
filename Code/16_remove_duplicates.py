def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4]))
    print(remove_duplicates([5, 5, 6, 7, 7]))