# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


class Solution(object):
    def myAtoi(self, s: str) -> int:
        stripped = s.strip()
        sign = 1
        answer = ""
        if len(stripped) < 1:
            return 0

        if not stripped[0].isdigit() and stripped[0] in ["+", "-"]:
            if stripped[0] == "-":
                sign = -1
            stripped = stripped[1:]

        for char in stripped:
            if char.isnumeric():
                answer += char
            else:
                break

        if not answer:
            return 0

        potential_answer = int(answer) * sign
        maximum = 2**31-1
        minimum = -pow(2, 31)
        if potential_answer > maximum:
            return maximum
        elif potential_answer < minimum:
            return minimum
        else:
            return potential_answer


if __name__ == '__main__':
    answer = Solution().myAtoi("+1")
    print(answer)
