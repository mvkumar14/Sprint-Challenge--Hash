#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    # loop through the tickets
    # if you find the first one ( where source = None)
    # set it aside
    # else put everything into storage
    # where the key = storage
    # value = destination

    # while current isn't none
    # add the current object's source to the list
    # make the destination the "current" value
    storage = {}
    current = ''
    route = []
    for item in tickets:
        if item.source == 'NONE':
            current = item.destination
            route.append(current)
            continue
        storage[item.source] = item.destination
    
    
    while current != 'NONE':
        destination = storage[current]
        route.append(destination)
        current = destination

    # what would the equivalent of being able to create
    # order through insertion be in this case? aka the way a human would do it?

    # the command would be I want to insert this after __
    # where __ is a value not an index (which I might need a dictionary for)
    # so you could say "insert where an item in the storage's destination is the source of this ticket"

    return route
