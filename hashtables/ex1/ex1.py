def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    # for every item
    # if storage[limit - item] exists:
        # compose and return result
    # else
        # add the weight:index to the 
        # storage
    
    if length < 1:
        return None

    storage = {}
    output = []
    possible = False
    for index,i in enumerate(weights):
        try:
            test = storage[limit-i] # should return index
            return (index, test)
        except KeyError:
            storage[i] = index
    
    if possible:
        return (storage[max(output)],storage[min(output)])
    else: 
        return None
