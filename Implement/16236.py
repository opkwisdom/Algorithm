from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
INF = float('inf')


class BabyShark:
    def __init__(self):
        self.x = None
        self.y = None
        self.size = 2
        self.eaten = 0
        self.t = 0
        self.fish_info = {i: [] for i in range(1, 7)}
        self.maps = None

    def load_map(self, maps):
        self.maps = maps
        for y in range(N):
            for x in range(N):
                if maps[y][x] == 9:
                    self.x = x
                    self.y = y
                elif maps[y][x] > 0:
                    self.fish_info[self.maps[y][x]].append((x, y))
    
    def get_closest(self):
        prey = []
        for i in range(self.size):
            prey.extend(self.fish_info[i])

        if not prey:
            return None
        
        target_x, target_y, dist = -1, -1, INF
        for x, y in prey:
            d = self.compute_dist(x, y)
            if d < dist:
                dist = d
                target_x, target_y = x, y

        if dist < INF:
            return target_x, target_y, dist

    def compute_dist(self, x, y):
        d = 0
        visited = [[False for _ in range(N)] for _ in range(N)]
        q = deque([(self.x, self.y)])
        visited[self.y][self.x] = True

        while q:
            for _ in range(len(q)):
                cx, cy = q.popleft()
                if cx == x and cy == y:
                    return d
                for i in range(4):
                    nx, ny = cx+dx[i], cy+dy[i]
                    if (nx >= 0 and nx < N and ny >= 0 and ny < N) and not visited[ny][nx]:
                        q.append((nx, ny))
                        visited[ny][nx] = True
            d += 1
        return d
    
    def eat(self, x, y):
        s = self.maps[y][x]
        if self.size > s:
            self.maps[y][x] = 0
            self.fish_info[s].remove((x, y))
            self.eaten += 1
            self.evolve()
            return True
        return False

    def evolve(self):
        if self.eaten >= self.size:
            self.size += 1
            self.eaten = 0

    def play(self):
        while True:
            closest = self.get_closest()
            if closest is None:
                break
            tx, ty, d = closest
            self.t += d
            self.eat(tx, ty)

        return self.t
        

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
baby_shark = BabyShark()
baby_shark.load_map(maps)
t = baby_shark.play()
print(t)