import textwrap

def wrap(string, max_width):
    output = textwrap.wrap(string, max_width)
    output = "\n".join(output)
    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
