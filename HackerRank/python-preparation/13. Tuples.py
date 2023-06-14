# should be written in pypy3 instead of python 3 due to some bugs from hackerrank side
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
