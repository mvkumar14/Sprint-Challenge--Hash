def has_negatives(a):

    """
    YOUR CODE HERE
    """
    # for every item
    # if dict[-item] exists
        # add to result
    # else (except KeyError)
    # add dict[item]
    result = []
    storage = {}
    for item in a:
        try:
            if storage[-item] == 1:
                result.append(abs(item))
        except KeyError:
            storage[item] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
