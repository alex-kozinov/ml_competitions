from sys import stdout

a0 = []
a1 = []
a2 = []
for i in range(1):
    print('?', 0)
    stdout.ﬂush()

    a0.append(float(input()))

for i in range(1):
    print('?', 0.001)
    stdout.ﬂush()

    a1.append(float(input()))

for i in range(1):
    print('?', -0.001)
    stdout.ﬂush()

    a2.append(float(input()))

min_dist = 1000
x0, x1, x2 = 0, 0.001, -0.001
y0, y1, y2 = -1, -1, -1
for i in range(1):
    for j in range(1):
        for k in range(1):
            curr_dist = abs(a0[i] - a1[j]) + abs(a0[i] - a2[k])
            if curr_dist < min_dist:
                min_dist = curr_dist
                y0, y1, y2 = a0[i], a1[j], a2[k]

a = (y2 - (x2* (y1 - y0) + x1*y0-x0*y1) / (x1 - x0)) / (x2* (x2 - x0 - x1) + x0* x1)
b = (y1 - y0) / (x1 - x0) - a * (x0 + x1)
c = y0

print('!', a, b, c)
stdout.ﬂush()