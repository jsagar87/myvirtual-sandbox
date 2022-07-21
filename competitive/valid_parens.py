import collections


def reverse_paren(s: str) -> str:
    if s == ")": return "("
    if s == "]": return "["
    if s == "}": return "{"


class Solution:

    def isValid(self, s: str) -> bool:
        chek_para = collections.deque()
        for c in s:
            if c in ["(", "{", "["]:
                chek_para.append(c)
                continue
            elif c in [")", "}", "]"]:
                if len(chek_para) == 0:
                    return False

                pair = chek_para.pop()
                if pair != reverse_paren(c):
                    return False
        if len(chek_para) != 0:
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))