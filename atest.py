def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1
    #print(occurrences)
    index = occurrences.index(max(occurrences))
    best_char = chr(ord('a')+index)
    #print(index)
    #print(best_char)

    best_res = max(occurrences)
    earlier = best_res
    for i in range(1, 26):
        test = occurrences[i]
        if occurrences[i] > best_res:    
            earlier = occurrences[i]
            best_char = chr(ord('a')+i)
            best_res = occurrences[i]

    #print(best_char)
    return best_char

if __name__ == "__main__":
    solution("hello")
    solution("abcdab")
