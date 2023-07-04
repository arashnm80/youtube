def merge_the_tools(string, k):
    i = 0
    while i + k <= len(string):
        sub = string[i:i+k]
        new_sub = ""
        for ch in sub:
            if ch not in new_sub:
                new_sub += ch
        print(new_sub)
        i += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
