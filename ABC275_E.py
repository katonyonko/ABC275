import io
import sys

_INPUT = """\
6
2 2 1
10 5 6
100 1 99
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,M,K=map(int,input().split())
  ans=0
  prob=[0]*N
  prob[0]=1
  I=pow(M,mod-2,mod)
  # print(prob[0]*I%mod)
  for i in range(K):
    tmp=[0]*N
    for j in range(N):
      for k in range(M):
        if j+k+1==N: ans=(ans+prob[j]*I)%mod
        else: tmp[min(j+k+1,2*N-j-k-1)]=(tmp[min(j+k+1,2*N-j-k-1)]+prob[j]*I)%mod
    prob=tmp.copy()
  print(ans)