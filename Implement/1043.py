from typing import List, Dict
from collections import deque

N, M = map(int, input().split())
first_known_people = list(map(int, input().split()))[1:]

known_group = first_known_people[:]     # 진실을 아는 사람들
q = deque(first_known_people)           # bfs 탐색
party: Dict[int, List[int]] = {i: [] for i in range(1, M+1)}    # 파티 별 포함된 인원
involved: Dict[int, List[int]] = {i: [] for i in range(1, N+1)} # 각 인원 별 포함된 파티

# Initialize
for i in range(1, M+1):
    people = list(map(int, input().split()))[1:]
    party[i] = people
    for p in people:
        involved[p].append(i)

# BFS
visited = [False for _ in range(M+1)]
while q:
    human = q.popleft()
    for party_num in involved[human]:
        if not visited[party_num]:
            visited[party_num] = True
            new_known_people = [p for p in party[party_num] if p not in known_group]
            q.extend(new_known_people)
            known_group.extend(new_known_people)
    
    # Test2 passed
    # print(f"New known people: {new_known_people}")
    # print(f"Updated: {known_group}")

# Iterate all partys
sol = 0
if len(known_group) == N:   # Early exit
    print(sol)
else:
    for party_num in range(1, M+1):
        is_pure = True
        for human in party[party_num]:
            if human in known_group:
                is_pure = False
                break
        if is_pure:
            sol += 1
    print(sol)

# Test1 passed
# for key, value in party.items():
#     print(f"Party {key}: {value}")
# for key, value in involved.items():
#     print(f"Human {key} involved in {value}")