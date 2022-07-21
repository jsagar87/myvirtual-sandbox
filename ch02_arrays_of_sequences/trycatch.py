tc_list1 = [1, 2, 3, 4, 1]
tc_list2 = [1, 2, 3, 4, 5]


def test_list(mList):
    try:
        mList.index(1, 2, 5)
    except ValueError:
        print("Value error")
        return -1
    else:
        return mList.index(1, 2, 5)


print(test_list(tc_list1))
print(test_list(tc_list2))
