def print_formatted(number):
    size = len(bin(number)[2:])
    for i in range(1, number + 1):
        a = str(i)
        b = str(oct(i)[2:])
        c = str(hex(i)[2:])
        d = str(bin(i)[2:])
        print(a.rjust(size," "),b.rjust(size," "),c.rjust(size," ").upper(),d.rjust(size," "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
