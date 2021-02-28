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
    return result
        



if __name__ == "__main__":
    #solution("We test coders. GIve us a try?")
    solution("Forget  CVs..Save time . x x")
# print("this is a debug message")
 