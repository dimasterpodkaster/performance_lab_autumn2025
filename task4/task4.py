import sys
import random

filename1 = sys.argv[1]

with open(filename1, 'r') as file_mass:
    values = []
    elems = file_mass.readlines()
    for elem in elems:
        values.append(int(elem.strip('\n')))

    if not values:
        print(0)
    else:
        def quick_select(massive, k):
            l, r = 0, len(massive) - 1
            while l < r:
                mid = random.randint(l, r)
                pivot = massive[mid]
                massive[mid], massive[l] = massive[l], massive[mid]

                lt = l
                i = l + 1
                rt = r
                while i <= rt:
                    if massive[i] < pivot:
                        massive[lt], massive[i] = massive[i], massive[lt]
                        lt += 1
                        i += 1
                    elif massive[i] > pivot:
                        massive[i], massive[rt] = massive[rt], massive[i]
                        rt -= 1
                    else:
                        i += 1

                if k < lt:
                    r = lt - 1
                elif k > rt:
                    l = rt + 1
                else:
                    return pivot

            return massive[l]

        needed = len(values) // 2
        median = quick_select(values, needed)
        sum_of_dists = 0
        for i in range(len(values)):
            sum_of_dists += abs(values[i] - median)
            if sum_of_dists > 20:
                break
        if sum_of_dists > 20:
            print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
        else:
            print(sum_of_dists)
