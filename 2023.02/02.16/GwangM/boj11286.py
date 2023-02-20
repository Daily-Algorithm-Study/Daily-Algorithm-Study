import sys
import heapq
input=sys.stdin.readline

n=int(input())
l=[]
for i in range(n):
  x=int(input())
  if x==0:
    if l:
      temp=heapq.heappop(l)
      print(temp[1])
    else:
      print(0)
  elif x>0:
    heapq.heappush(l,(2*x+1,x))
  else:
    heapq.heappush(l,(2*(-x),x))