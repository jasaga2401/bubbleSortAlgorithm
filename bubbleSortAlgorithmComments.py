# bubble sorting algorithm function
def bubbleSort(items):

    swapped = True
    # outer loop that will continue until the boolean value swapped
    # is assigned to False
    while swapped:
        # the boolean variable swapped is assigned to False. If it
        # stays this way it will stop the outer loop from running
        swapped = False
        # inner loop that compares consecutive data items, one pair
        # after another pair of data items, checking if the first data item
        # is greater than the second data item
        for index in range(0, len(items)-1):
            # checks to see if the first data item is greater
            # than the second data item
            if (items[index] > items[index+1]):
                # swaps data items
                temp = items[index]
                items[index] = items[index+1]
                items[index+1] = temp

                # changes the value of swapped from False to True
                swapped = True
    # returns the list (as it is a function)
    return items

items = [5, 3, 8, 1, 7, 2]
print(bubbleSort(items))
