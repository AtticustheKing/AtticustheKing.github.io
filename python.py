def dirReduc(arr):
    didDel = False
    badDirections = [["NORTH", "SOUTH"], ["SOUTH", "NORTH"], ["EAST", "WEST"], ["WEST", "EAST"]]
    i = 0
    while i < (len(arr)-1):
        placeholder = [arr[i], arr[i+1]]
        if placeholder in badDirections:
            del arr[i]
            del arr[i]
            didDel = True
            i -= 1
        i += 1
    if didDel == True:
        return dirReduc(arr)
    else:
        return arr

practice = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
list = dirReduc(practice)
print(list)