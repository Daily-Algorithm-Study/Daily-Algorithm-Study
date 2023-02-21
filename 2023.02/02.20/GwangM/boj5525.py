import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
l=input()
idx=0
result=0
temp1='I'+'OI'*n
t1=l.find(temp1)
le=len(temp1)
while(t1!=-1):
  result+=1
  l=l[t1+le:]  
  i=0;j=1
  while(l[i]=="O" and l[j]=="I"):
    result+=1
    i+=2
    j+=2
  l=l[i:]

  t1=l.find(temp1)

print(result)