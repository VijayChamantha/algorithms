
def binary_search(li,target):

    first=0
    last=len(li)-1
    while first<=last:
        midpoint=(first+last)//2
        if li[midpoint]==target:
            return midpoint
        elif li[midpoint]<target:
            first=midpoint+1
        else:
            last=midpoint-1
    return None

def recursive_binarySearch(li,target):
    if len(li)==0:
        return False
    else:
        midpoint=len(li)//2
        if li[midpoint]==target:
            return midpoint
        elif li[midpoint]<target:
            return recursive_binarySearch(li[midpoint+1:],target)
        else:
            return recursive_binarySearch(li[:midpoint],target)
    

print('target value at index: ',binary_search([1,2,3,4,5,6],2))
print('in recursive target value at index: ',recursive_binarySearch([1,2,3,4,5,6],10))
