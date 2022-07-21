from collections import deque

# # get biggest number recursively
# for_best = deque(digits)
#
#
# def get_max_of_rest(digits: deque) -> int:
#     best = 0
#     best = digits.popleft()
#     best_from_rest = get_max_of_rest(digits)
#     digits.appendleft(best)
#     return max(best, best_from_rest)


def biggest_int_recursive(digits):
    digits_queue = deque(digits)
    return biggest_int_recursive_helper(digits_queue)


def biggest_int_recursive_helper(digits):
    best = 0
    for _ in range(len(digits)):
        digit = digits.popleft()
        biggest_int_recursive_helper(digits)
    # digits.
    return 0


def biggest_int_greedy(digits):
    return 0


digits = [5, 4, 0, 1, 9, 3]
