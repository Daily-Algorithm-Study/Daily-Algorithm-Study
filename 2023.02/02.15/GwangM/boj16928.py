from collections import deque
n,m=map(int,input().split())
ladder={}
for i in range(n+m):
  a,b=map(int,input().split())
  ladder[a]=b

def bfs(start, ladder):
  queue=deque([(start,0)])
  visited=[start]
  while(queue):
    temp, x=queue.popleft()
    for i in range(temp+1,temp+7):
      if i not in visited:
        if i==100:
          return x+1
        visited.append(i)
        if i in ladder:
          t=ladder[i]
          visited.append(t)
          queue.append((t,x+1))
        else:
          queue.append((i,x+1))

print(bfs(1,ladder))