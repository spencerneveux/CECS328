
def isOrdered(list):
    for i in range(1, len(list)):
        if list[i-1] > list[i]:
            return False
    return True

