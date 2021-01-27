#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
A, B, K = map(int, input().split())

print(max(0, A - K), max(0, B - max(0, K - A)))
