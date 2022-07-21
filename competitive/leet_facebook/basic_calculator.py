import collections


def calculator(s: str):
    cur = collections.deque()
    for c in s:
        cur.append(c)
    # So far O(N)

    glub = collections.deque()

    holder = 0
    while cur:
        item = cur.popleft()
        if item in ["+", "-", "(", ")"]:
            if holder != 0:
                glub.append(holder)
                holder = 0
            glub.append(item)
        elif item.isdigit():
            holder = int(holder) * 10 + int(item)

    if holder != 0:
        glub.append(int(holder))

    print(glub)

    club = collections.deque()
    flip_sign = 1
    for val in glub:
        if val == "-":
            club.append("+")
            flip_sign = -1
        else:
            club.append(flip_sign * val)
            flip_sign = 1

    print(club)

    proccess_queue = collections.deque()

    while club:
        item = club.popleft()
        if len(club) == 0:
            proccess_queue.append(item)
        op1 = 0
        if item == ")" or len(club) == 0:
            while proccess_queue:
                cur = proccess_queue.pop()
                if type(cur) is int:
                    op1 = cur
                    if len(proccess_queue) == 1:
                        club.appendleft(op1)
                    continue
                if cur == "+":
                    cur = proccess_queue.pop()
                    op1 = cur + op1
                    continue
                if cur == "(":
                    # club.appendleft(op1)
                    proccess_queue.append(op1)
                    op1 = 0
                    continue
            if len(club) == 0 and len(proccess_queue) == 0:
                return op1
        else:
            proccess_queue.append(item)


if __name__ == '__main__':
    # print(calculator("(1+2+21)+10-12"))
    # print(calculator("(1+31)+10-11"))
    # print(calculator(" 2-1 + 2 "))
    print(calculator("(1+(4+5+2)-3)+(6+8)"))
