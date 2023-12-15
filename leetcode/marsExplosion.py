def marsExploration(s):
    duplicate = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            duplicate += 1
        if s[i+1] != 'O':
            duplicate += 1
        if s[i+2] != 'S':
            duplicate += 1

    return duplicate

if __name__ == '__main__':
    print(marsExploration('SOSSPSSQSSOR'))
