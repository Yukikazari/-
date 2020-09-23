N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

class Union_Find():
    def __init__(self, n):
        """
        要素数n
        """
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        """
        要素xが属するグループの根を返す
        return int
        """
        if self.par[x] < 0:
            return x

        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        要素xが属するグループと要素yが属するグループを併合する
        return null
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        """
        要素xが属するグループの要素数を取得する
        return int
        """
        return - self.par[self.find(x)]
        
    def same(self, x, y):
        """
        要素xと要素yが同じグループに属するかどうかを返す
        return bool
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        要素xが属するグループに属する要素を返す
        return array
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素を返す
        return array
        """
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        """
        グループ数を返す
        return int
        """
        return len(self.roots())

    def all_group_members(self):
        """
        全てのグループに対してそれぞれ属する要素を返す
        return dict[array]
        """
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

UF = Union_Find(N)

for a, b in AB:
    UF.union(a-1, b-1)

ans = 0

for i in UF.roots():
    ans = max(ans, UF.size(i))

print(ans)