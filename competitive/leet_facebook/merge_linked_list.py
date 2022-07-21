# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = collections.deque()
        stack2 = collections.deque()
        result_ll = None
        while list1 != None:
            pop = list1.val
            list1 = list1.next
            stack1.append(pop)

        while list2 != None:
            pop = list2.val
            list2 = list2.next
            stack2.append(pop)

        while len(stack1) > 0 and len(stack2) > 0:

            if len(stack2) == 0:
                while len(stack1) > 0:
                    pop = stack1.pop()
                    newNode = ListNode(pop, None)
                    if result_ll == None:
                        result_ll = newNode
                    else:
                        newNode.next = result_ll
                        result_ll = newNode
                return result_ll

            if len(stack1) == 0:
                while len(stack2) > 0:
                    pop = stack2.pop()
                    newNode = ListNode(pop, None)
                    if result_ll == None:
                        result_ll = newNode
                    else:
                        newNode.next = result_ll
                        result_ll = newNode
                return result_ll

            p1 = stack1.pop()
            p2 = stack2.pop()

            if p1 >= p2:
                newNode = ListNode(p1, None)
                stack2.append(p2)
            else:
                newNode = ListNode(p2, None)
                stack1.append(p1)

            if result_ll == None:
                result_ll = newNode
            else:
                newNode.next = result_ll
                result_ll = newNode

        if len(stack1) > 0:
            while len(stack1) > 0:
                pop = stack1.pop()
                newNode = ListNode(pop, None)
                if result_ll == None:
                    result_ll = newNode
                else:
                    newNode.next = result_ll
                    result_ll = newNode

        if len(stack2) > 0:
            while len(stack2) > 0:
                pop = stack2.pop()
                newNode = ListNode(pop, None)
                if result_ll == None:
                    result_ll = newNode
                else:
                    newNode.next = result_ll
                    result_ll = newNode

        return result_ll
