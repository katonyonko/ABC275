import io
import sys

_INPUT = """\
6
2 3 5 1 2 4
1 1 1000000000 0 0 0
1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  A,B,C,D,E,F=map(int,input().split())
  print((A*B%mod*C%mod-D*E%mod*F%mod)%mod)