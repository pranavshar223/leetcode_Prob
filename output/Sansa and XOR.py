import heapq

def runningMedian(arr):
    min_heap = []  # right side (higher half)
    max_heap = []  # left side (lower half, stored as negative numbers)
    medians = []

    for number in arr:
        # Step 1: Add to max_heap
        heapq.heappush(max_heap, -number)

        # Step 2: Balance: max_heap's top must be <= min_heap's top
        if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # Step 3: Rebalance if size difference > 1
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Step 4: Compute median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2.0
        else:
            median = -max_heap[0] * 1.0

        medians.append(median)

    return medians

# Driver code
n = int(input())
arr = [int(input()) for _ in range(n)]

medians = runningMedian(arr)
for m in medians:
    print(f"{m:.1f}")
