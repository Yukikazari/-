#!/usr/bin/env python3

#import
import math
A, B = map(int, input().split())

print(A * B // math.gcd(A, B))
