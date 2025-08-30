import sys

n1, m1 = int(sys.argv[1]), int(sys.argv[2])
n2, m2 = int(sys.argv[3]), int(sys.argv[4])

if n1 <= 0 or n2 <= 0 or m1 == 0 or m2 == 0:
    print('Invalid input')

else:
    m1 = m1 % n1
    if m1 == 0:
        m1 = n1
    m2 = m2 % n2
    if m2 == 0:
        m2 = n2

    ans1 = [1]
    ans2 = [1]

    next_value1 = (ans1[-1] + m1 - 2) % n1 + 1
    next_value2 = (ans2[-1] + m2 - 2) % n2 + 1
    while next_value1 != 1 or next_value2 != 1:
        # print(next_value1, next_value2)
        if next_value1 != 1:
            ans1.append(next_value1)
            next_value1 = (ans1[-1] + m1 - 2) % n1 + 1
        if next_value2 != 1:
            ans2.append(next_value2)
            next_value2 = (ans2[-1] + m2 - 2) % n2 + 1

    print(''.join(map(str, ans1 + ans2)))
