class Solution:
    def convert(s: str, numRows: int) -> str:
        print(s)
        print(numRows)
        print(len(s))
        line = 0
        position = 1
        outp = [""]*numRows
        print(outp)
        #PAYPALISHIRING, 3
        for i in range(len(s)):
            outp[line] += s[i]
            if numRows > 1:
                line += position
                if line == 0 or line == numRows-1:
                    position *= -1

        print(outp)
        outputstring=""
        for j in range(numRows):
            outputstring +=outp[j]
        print(outputstring)


if __name__ == "__main__":
    Solution.convert("PAYPALISHIRING", 3)
    # output: PAHNAPLSIIGYIR
    Solution.convert("PAYPALISHIRING", 4)
    # output: PINALSIGYAHRPI
