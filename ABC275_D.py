import io
import sys

_INPUT = """\
6
2
0
100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  memo={}
  def f(x):
    if x in memo: return memo[x]
    if x==0: return 1
    memo[x]=f(x//2)+f(x//3)
    return memo[x]
  print(f(N))