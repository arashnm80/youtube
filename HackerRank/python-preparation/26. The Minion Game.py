def minion_game(string):
    kevin_score = stuart_score = 0
    for i, ch in enumerate(string):
        if ch in "AEIOU":
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
