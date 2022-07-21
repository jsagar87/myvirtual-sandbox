import collections


def opposite_of(bracket: str) -> str:
    if bracket == "}":
        return "{"
    elif bracket == ")":
        return "("
    else:
        return "["


def is_balanced(s):
    stack = collections.deque()
    # Write your code here
    for br in s:
        if br in "{[(":
            stack.append(br)
        elif br == "}":
            try:
                left_paren = stack.pop()
                if left_paren == "{":
                    continue
                else:
                    return "NO"
            except IndexError:
                return "NO"
        elif br == "]":
            try:
                left_paren = stack.pop()
                if left_paren == "[":
                    continue
                else:
                    return "NO"
            except IndexError:
                return "NO"
        elif br == ")":
            try:
                left_paren = stack.pop()
                if left_paren == "(":
                    continue
                else:
                    return "NO"
            except IndexError:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
