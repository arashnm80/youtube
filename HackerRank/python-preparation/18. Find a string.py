def count_substring(string, sub_string):
    count = 0
    l1 = len(string)
    l2 = len(sub_string)
    for i in range(l1 - l2 + 1):
        if string[i:i + l2] == sub_string:
            count += 1
    return count
    # string = "ABCDE" # 5 chars
    # sub_string = "ABC" # 3 chars
    
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
