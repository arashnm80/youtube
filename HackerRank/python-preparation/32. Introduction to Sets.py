from statistics import mean

def average(array):
    my_set = set(array)
    return mean(my_set)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
