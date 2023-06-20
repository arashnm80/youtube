if __name__ == '__main__':
    s = input()

    status = False
    for ch in s:
        if ch.isalnum():
            status = True
            break
    print(status)
    
    status = False
    for ch in s:
        if ch.isalpha():
            status = True
            break
    print(status)
    
    status = False
    for ch in s:
        if ch.isdigit():
            status = True
            break
    print(status)

    status = False
    for ch in s:
        if ch.islower():
            status = True
            break
    print(status)
    
    status = False
    for ch in s:
        if ch.isupper():
            status = True
            break
    print(status)
