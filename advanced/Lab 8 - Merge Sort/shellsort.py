def shell_sort(target):
    gap = len(target) // 2
    while gap > 0:
        # print(gap)
        for pos in range(gap, len(target)):
            tmp = target[pos]
            k = pos
            while tmp < target[k-gap] and k >= gap:
                target[k] = target[k-gap]
                k -= gap
            target[k] = tmp
        gap //= 2
