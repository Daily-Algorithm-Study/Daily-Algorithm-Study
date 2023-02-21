import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
l1=deque()
l2=deque()
for i in range(n):
  l1.append(input())
for i in range(m):
  l2.append(input())
l3 = set(l1)&set(l2)
l3=list(l3)
l3.sort()
print(len(l3))
for i in l3:
  print(i,end='')