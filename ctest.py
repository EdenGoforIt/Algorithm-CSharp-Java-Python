def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1
    #need to find the index where the max value occurs
    index = occurrences.index(max(occurrences))
    #first need to earlier alphabet and best frequent number
    best_char = chr(ord('a')+index)
    best_res = max(occurrences)

    for i in range(1, 26):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re
def solution(S):
    # write your code in Python 3.6
    #print(S)
    divided =  re.split("\.\s+", S)
    #print(divided)
    result = 0
    for sentence in divided:
        result = len(sentence.split())
        if result > len(sentence.split()):
            result = len(sentence.split()) 
    #print(result)
    return result
