n,r,c=map(int,input().split())
row=2**n
total=row*row
p1=[0,0]
p2=[row-1,row-1]

def solve(r,c,row):
  if row==1:
    return 0
  else:
    if r>=row//2:
      if c>=row//2:
        return row*row*3/4+solve(r-row/2,c-row/2,row/2)
      else:
        return row*row/2+solve(r-row/2,c,row/2)
    else:
      if c>=row//2:
        return row*row/4+solve(r,c-row/2,row/2)
      else:
        return solve(r,c,row/2)

print(int(solve(r,c,row)))