def search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "nothing to show here"

#Example :
print(search([2,4,6,8,10,12,14,16,18,20,22],8))
