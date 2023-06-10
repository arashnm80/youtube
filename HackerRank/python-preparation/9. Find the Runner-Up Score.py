if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    arr.sort()
    new_arr = []
    [new_arr.append(x) for x in arr if x not in new_arr]
    print(new_arr[-2])
    

# If you want to learn more about map() in python:
    # https://www.simplilearn.com/tutorials/python-tutorial/map-in-python
    # https://www.geeksforgeeks.org/python-map-function/#
# If you want to learn more about how duplicate items can be removed from a list:
    # https://www.simplilearn.com/tutorials/python-tutorial/remove-duplicates-from-list-python
