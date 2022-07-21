# Queue using two stacks
import collections


class QueueStack:
    def __init__(self):
        self._stack_forward = collections.deque()
        self._stack_backward = collections.deque()
        self.front = None

    def is_empty(self) -> bool:
        return len(self._stack_forward) == 0 and len(self._stack_backward) == 0

    def peek(self):
        if len(self._stack_backward):
            head = self._stack_backward.pop()
            self._stack_backward.push(head)
            return head
        return self.front
        # if len(self._stack_forward) == 0:
        #     print(None)
        #     return
        # while len(self._stack_forward) > 0:
        #     self._stack_backward.append(self._stack_forward.pop())
        # head = self._stack_backward.pop()
        # print(head)
        # self._stack_forward.append(head)
        # while len(self._stack_backward) > 0:
        #     self._stack_forward.append(self._stack_backward.pop())

    def enqueue(self, data):
        if not len(self._stack_forward):
            self.front = data
        self._stack_forward.append(data)

    def dequeue(self):
        if not len(self._stack_backward):
            while len(self._stack_forward) > 0:
                self._stack_backward.append(self._stack_forward.pop())
        head = self._stack_backward.pop()
        return head
        # if len(self._stack_forward) == 0:
        #     return None
        # while len(self._stack_forward) > 0:
        #     self._stack_backward.append(self._stack_forward.pop())
        # head = self._stack_backward.pop()
        # while len(self._stack_backward) > 0:
        #     self._stack_forward.append(self._stack_backward.pop())
        # return head

    def __repr__(self):
        repressor = ""
        if self._stack_forward:
            repressor = self._stack_forward.__repr__()
        elif self._stack_backward:
            repressor = self._stack_backward.__repr__()
        else:
            repressor = ""
        return repressor


if __name__ == "__main__":
    qs = QueueStack()
    number_of_queries = input()
    for i in range(0, int(number_of_queries)):
        ip = input()
        str_ar = ip.split(" ")

        # Case deque
        if len(str_ar) == 1 and int(str_ar[0]) == 2:
            qs.dequeue()
        # Case print head
        elif len(str_ar) == 1 and int(str_ar[0]) == 3:
            print(qs.peek())
        # Case enqueue
        elif len(str_ar) == 2 and int(str_ar[0]) == 1:
            qs.enqueue(str_ar[1])
        else:
            print("Wrong input format")
    print("Final state of stack : %r" % qs)
