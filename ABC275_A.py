import io
import sys

_INPUT = """\
6
3
50 80 70
1
1000000000
10
22 75 26 45 72 81 47 29 97 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  H=list(map(int,input().split()))
  print(H.index(max(H))+1)