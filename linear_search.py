
def linear_search(li,target):
    """returns index position of the target if found ,else returns None"""
    for i in li:
        if target==li[i]:
            return i

    return None
def verify(index):
    if index is not None:
        print('target found at index: ',index)
    else:
        print('target not found')

li=[1,2,3,4,5,6,7,8,9]
result=linear_search(li,9)
verify(result)
