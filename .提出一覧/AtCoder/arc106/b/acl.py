import types

_atcoder_code = """
# Python port of AtCoder Library.

__version__ = '0.0.1'
"""

atcoder = types.ModuleType('atcoder')
exec(_atcoder_code, atcoder.__dict__)

_atcoder_dsu_code = """
import typing


class DSU:
    '''
    Implement (union by size) + (path compression)
    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        if self.parent_or_size[a] < 0:
            return a

        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))
"""

atcoder.dsu = types.ModuleType('atcoder.dsu')
exec(_atcoder_dsu_code, atcoder.dsu.__dict__)
DSU = atcoder.dsu.DSU

#!/usr/bin/env python3

# from atcoder.dsu import DSU
#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = [list(map(int, input().split())) for _ in range(M)]

cnt = [0] * N
for i in range(N):
    cnt[i] = B[i] - A[i]

uf = DSU(N)

for cd in CD:
    c = cd[0]
    d = cd[1]
 
    uf.merge(c - 1, d - 1)
    
al = uf.groups()

ans = True
for li in al:
    t = 0
    for d in li:
        t += cnt[d]

    if t != 0:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")