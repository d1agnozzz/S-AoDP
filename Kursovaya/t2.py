import heapq


def fill_zero_array(num) :
    array = [0] * num
    heap = [(-num, 0)] # (leftInd, length)

    for i in range(1, num+1):
        length, l = heapq.heappop(heap)
        length = - length
        r = l + length - 1
        mid = (l+r) //2
        array[mid] = i

        if mid > l:
            heapq.heappush(heap, (-(mid-l), l))
        if mid < r:
            heapq.heappush(heap, (-(r-mid), mid+1))
    return array


quant = int(input())
inputs = list()
for i in range(quant):
    inputs.append(int(input()))
for i in inputs:
    print(*fill_zero_array(i))