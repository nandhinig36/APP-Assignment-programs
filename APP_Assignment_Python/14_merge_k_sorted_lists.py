import heapq

def merge_k_lists(lists):
    heap = []
    for i, values in enumerate(lists):
        if values: heapq.heappush(heap, (values[0], i, 0))
    result = []
    while heap:
        value, list_id, index = heapq.heappop(heap)
        result.append(value)
        nxt = index + 1
        if nxt < len(lists[list_id]):
            heapq.heappush(heap, (lists[list_id][nxt], list_id, nxt))
    return result

if __name__ == "__main__":
    print(merge_k_lists([[1,4,5],[1,3,4],[2,6]]))
