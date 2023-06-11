if __name__ == '__main__':
    lowest = 1000
    second_lowest = 1001
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest:
            second_lowest = lowest
            lowest = score
        elif lowest < score < second_lowest:
            second_lowest = score
        records.append([name, score])
    
    output = []
    for r in records:
        if r[1] == second_lowest:
            output.append(r[0])
    output.sort()
    print(*output, sep="\n")
