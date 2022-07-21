def isPossible(arr, n) -> bool:
    totalsum = 0
    for n in arr:
        totalsum += n

    desired_sum = int(totalsum / 2)
    subset_size = len(totalsum)


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 4, 4, 5, 6]
    n = len(arr)

    if isPossible(arr, n):
        print("Yes")
    else:
        print("No")


