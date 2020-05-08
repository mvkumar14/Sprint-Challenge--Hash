def finder(files, queries):

    """
    YOUR CODE HERE
    """
    # store every value 
    # of the file into a dictionary
    # key = last bit of file (from end to last slash)
    # value = path

    #for item in query:
    # if it exists in the dictionary
    # add to result
    # else
    # continue
    result = []
    storage= {}
    for item in files:
        for index in range(len(item)):
            loc = index+1
            if item[-loc] == '/':
                key = item[-loc + 1:]
                break
        try:
            temp = storage[key] #exists
            if type(storage[key]) == list:
                storage[key].extend(item)
            else: # not a list just one item
                storage[key] = [item,temp]
        except KeyError:
            storage[key] = item


    for item in queries:
        try:
            if type(storage[item]) == list:
                result.extend(storage[item])
            else:
                result.append(storage[item])
        except KeyError:
            continue

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
