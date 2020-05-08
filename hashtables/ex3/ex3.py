def intersection(arrays):
    # for every value in arrays
    # try to access dictionary
        # if successful add to result
    # if keyerror
    # add to dictionary
    """
    YOUR CODE HERE
    """
    result = []
    storage = {}
    for array in arrays:
        for val in array:
            try:
                if storage[val] == 1:
                    result.append(val)
                    storage[val] += 1
            except KeyError:
                storage[val] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
