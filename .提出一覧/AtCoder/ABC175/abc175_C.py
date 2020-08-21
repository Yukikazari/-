X, K, D = map(int, input().split())

k = round(abs(X) / D)

if k > K:
    if k == 1:
        print(abs(abs(X) - K * D))
    else:
        print(min(abs(abs(X) - K * D), abs(abs(X) - (K - 2) * D)))

else:
    if k % 2 == K % 2:
        print(min(abs(abs(X) - k * D), abs(abs(X) - (k + 2) * D), abs(abs(X) - (k - 2) * D)))

    else:
        print(min(abs(abs(X) - (k + 1) * D), abs(abs(X) - (k - 1) * D), abs(abs(X) - (k + 3) * D), abs(abs(X) - (k - 3) * D)))