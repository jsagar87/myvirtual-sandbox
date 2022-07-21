import collections

ip_string = "2*2*4*44+3*66"
sumlist = []

def tokanize_stack(ipstring):
    operation_stack = collections.deque()
    number_stack = collections.deque()
    word = ""
    for i in ipstring:
        if i in ["*", "+"] and word:
            operation_stack.append(i)
            number_stack.append(int(word))
            word = ""
        else:
            word = word+i
    if word:
        number_stack.append(word)

    print(operation_stack)
    print(number_stack)
    return operation_stack, number_stack


operation_stack, number_stack = tokanize_stack(ip_string)

def perform_operation(operation_stack, number_stack):
    global sumlist
    for operation in operation_stack:
        print(operation)
        if operation is "*":
            num1 = number_stack.pop()
            num2 = number_stack.pop()
            number_stack.append(num1*num2)
        else:
            sumlist.append(number_stack.pop())

perform_operation(operation_stack, number_stack)
