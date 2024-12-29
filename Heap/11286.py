import sys

def swap(heap, i, j):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp

def find_min_idx(heap, i, j):
    min_idx = -1
    if heap[i][0] < heap[j][0]:
        min_idx = i
    elif heap[i][0] == heap[j][0] and heap[i][1] < heap[j][1]:
        min_idx = i
    else:
        min_idx = j
    return min_idx

def abs_heapify_up(heap, idx):
    parent = idx // 2
    if parent > 0:
        if heap[parent][0] > heap[idx][0]:
            swap(heap, parent, idx)
            abs_heapify_up(heap, parent)
        elif heap[parent][0] == heap[idx][0]:
            if heap[parent][1] > heap[idx][1]:
                swap(heap, parent, idx)
                abs_heapify_up(heap, parent)

def abs_heapify_down(heap, idx):
    left, right = idx*2, idx*2+1
    n = heap[0]
    if right <= n:
        min_idx = find_min_idx(heap, left, right)
    elif left <= n:
        min_idx = left
    else:
        min_idx = -1
    
    if min_idx != -1:
        if heap[idx][0] > heap[min_idx][0]:
            swap(heap, idx, min_idx)
            abs_heapify_down(heap, min_idx)
        elif heap[idx][0] == heap[min_idx][0]:
            if heap[idx][1] > heap[min_idx][1]:
                swap(heap, idx, min_idx)
                abs_heapify_down(heap, min_idx)

heap = [0]
N = int(sys.stdin.readline())
printed = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap[0] == 0:
            printed.append(0)
        else:
            swap(heap, 1, heap[0])
            printed.append(heap.pop()[1])
            heap[0] -= 1
            abs_heapify_down(heap, 1)
    else:
        heap.append((abs(x), x))
        heap[0] += 1
        abs_heapify_up(heap, heap[0])

for p in printed:
    print(p)