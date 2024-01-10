from heapq import heappush, heappop
def solution(operations):
    maxQueue = []
    minQueue = []

    for ops in operations:
        if ops.startswith("I"):
            number = int(ops.split()[1])
            heappush(maxQueue, -number)
            heappush(minQueue, number)
        elif ops == "D 1":
            if maxQueue:
                minQueue.remove(-heappop(maxQueue))
        else:
            if minQueue:
                maxQueue.remove(-heappop(minQueue))
    return [-maxQueue[0], minQueue[0]] if maxQueue and minQueue else [0, 0]