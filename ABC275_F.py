import io
import sys

_INPUT = """\
6
4 5
1 2 3 4
1 5
3
12 20
2 5 6 5 2 1 7 9 7 2 5 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  dp1,dp2=[10**20]*(M+1),[10**20]*(M+1)
  dp2[0]=1
  for i in range(N):
    tmp=[10**20]*(M+1)
    for j in reversed(range(M+1)):
      if j+A[i]<=M:
        if N==1 and i==0:
          tmp[j+A[i]]=dp2[j]-1
        elif i==0:
          tmp[j+A[i]]=dp2[j]
        elif i==N-1:
          tmp[j+A[i]]=min(dp1[j]-1,dp2[j])
        else:
          tmp[j+A[i]]=min(dp1[j],dp2[j]+1)
    dp2=[min(dp1[j],dp2[j]) for j in range(M+1)]
    dp1=tmp.copy()
  ans=[min(dp1[j],dp2[j]) for j in range(M+1)]
  for i in range(1,M+1):
    if ans[i]>=10**10: print(-1)
    else: print(ans[i])