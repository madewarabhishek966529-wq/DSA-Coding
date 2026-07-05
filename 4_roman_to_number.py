class Solution(object):
    def romanToInt(self, s):
        total = 0

        for i in range(len(s)):
            if s[i] == "I":
                value = 1
            elif s[i] == "V":
                value = 5
            elif s[i] == "X":
                value = 10
            elif s[i] == "L":
                value = 50
            elif s[i] == "C":
                value = 100
            elif s[i] == "D":
                value = 500
            else:
                value = 1000

            if i < len(s) - 1:
                if s[i + 1] == "I":
                    next_value = 1
                elif s[i + 1] == "V":
                    next_value = 5
                elif s[i + 1] == "X":
                    next_value = 10
                elif s[i + 1] == "L":
                    next_value = 50
                elif s[i + 1] == "C":
                    next_value = 100
                elif s[i + 1] == "D":
                    next_value = 500
                else:
                    next_value = 1000

                if value < next_value:
                    total -= value
                else:
                    total += value
            else:
                total += value

        return total