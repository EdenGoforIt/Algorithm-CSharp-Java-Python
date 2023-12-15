def find_all_combination(s):
    n = len(s)

    for i in range(n-1):
        for j in range(i+1, n):
            print(s[i],"-", s[j])


names = ['tom', 'ken', 'eden', 'jay']
print(find_all_combination(names))