class Solution:
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        result = 0
        isnegative = False
        signset = False
        for c in iter(s):
            if c in digits:
                break
            if c == " ":
                continue
            if c == '-' and signset == False:  # and idx == len(s)-1:
                isnegative = True
                signset = True
                s = s.lstrip("-")
                continue
            elif c == '+' and signset == False:
                isnegative = False
                signset = True
                s = s.lstrip("+")
                continue
            elif (c == '-' or c == '+') and signset == True:
                isnegative = True
                signset = True
                return 0

        for c in iter(s):
            try:
                digit = self.digits.index(c)
            except ValueError:
                break
            result = result * 10 + digit

        if isnegative:
            result -= 2 * result

        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        elif result < -2 ** 31:
            result = -2 ** 31

        return result


if __name__ == '__main__':
    converter = Solution()
    hundread = converter.myAtoi("-100")
    print(type(hundread))
    print(hundread)
    fortytwo = converter.myAtoi(("42"))
    print(fortytwo)
    print(converter.myAtoi("-91283472332"))

