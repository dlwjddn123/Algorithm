start = [0.5, 0.8, 0.2]
w = [0.4, 0.7, 0.8]
alpha = 0.5

for t in range(1, 6):
    e = 1
    delta = []
    for i in range(3):
        e -= start[i] * w[i]
    for i in range(3):
        delta.append(e * alpha * w[i])
        w[i] += delta[i]
    print("Repeat", t)
    print("e = ", e)
    print("delta = ", delta)
    print("w = ", w)
    print()