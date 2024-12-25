import sys
sys.setrecursionlimit(10 ** 6)

def swap(heap, i, j):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp

def min_heapify_down(heap, idx):
    n = heap[0]
    
    i, j = idx * 2, idx * 2 + 1
    if j <= n:
        min_idx = i if heap[i] < heap[j] else j
        if heap[min_idx] < heap[idx]:
            swap(heap, idx, min_idx)
            min_heapify_down(heap, min_idx)
    elif i <= n:
        min_idx = i
        if heap[min_idx] < heap[idx]:
            swap(heap, idx, min_idx)

def min_heapify_up(heap, idx):
    parent = idx // 2
    if parent > 0 and heap[parent] > heap[idx]:
        swap(heap, parent, idx)
        min_heapify_up(heap, parent)

N = int(sys.stdin.readline())
heap = [0]

result = []
for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if heap[0] == 0:
            result.append(0)
        else:
            x = heap.pop(1)
            heap[0] -= 1
            heap.insert(1, heap.pop())
            result.append(x)
            min_heapify_down(heap, 1)
    else:
        heap.append(num)
        heap[0] += 1
        min_heapify_up(heap, heap[0])

for a in result:
    print(a)