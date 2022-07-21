def bestDaysToBuyAndSell(arr):
    # Write your code here
    copy_arr = list(arr)
    copy_arr = sorted(copy_arr, reverse=True)
    purchase_day = arr.index(copy_arr[len(arr) - 1])
    sell_day = arr.index(copy_arr[0],purchase_day)
    return [purchase_day, sell_day]


