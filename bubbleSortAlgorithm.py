
def bubbleSort(items):

    swapped = True
    
    while swapped:

        swapped = False

        for index in range(0, len(items)-1):

            if (items[index] > items[index+1]):

                temp = items[index]
                items[index] = items[index+1]
                items[index+1] = temp

                swapped = True

    return items

items = [5, 3, 8, 1, 7, 2]
print(bubbleSort(items))
