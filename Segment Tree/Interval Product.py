import math
import sys


def main():
    try:
        while True:
            n, k = map(int, input().split())

            x = list(map(int, input().split()))
            a = [0 for i in range(n)]

            for i in range(n):
                if x[i] < 0:
                    a[i] = -1
                elif x[i] > 0:
                    a[i] = 1
                else:
                    a[i] = 0

            h = int(math.ceil(math.log2(n)))
            tree_size = 2 * int(math.pow(2, h)) - 1
            seg_tree = [0 for i in range(tree_size)]

            build_tree(a, seg_tree, 0, 0, n - 1)

            for i in range(k):
                line = input().split()
                c = line[0]

                if c == 'C':
                    I = int(line[1]) - 1
                    V = int(line[2])

                    if V > 0:
                        sign = 1
                    elif V < 0:
                        sign = -1
                    else:
                        sign = 0
                    update_query(seg_tree, 0, 0, n - 1, I, sign)
                elif c == 'P':
                    I = int(line[1]) - 1
                    J = int(line[2]) - 1

                    product = product_range(seg_tree, 0, 0, n - 1, I, J)

                    if product > 0:
                        print('+', end='')
                    elif product < 0:
                        print('-', end='')
                    else:
                        print('0', end='')

            print()
    except:
        pass


def product_range(seg_tree, index, left, right, range_from, range_to):
    if range_from > right or range_to < left:
        return 1

    if range_from <= left and right <= range_to:
        return seg_tree[index]

    mid = (left + right) // 2

    return product_range(seg_tree, 2 * index + 1, left,    mid,   range_from, range_to) \
         * product_range(seg_tree, 2 * index + 2, mid + 1, right, range_from, range_to)


def update_query(seg_tree, index, left, right, pos, val):
    if pos < left or pos > right:
        return

    if left == right:
        if left == pos:
            seg_tree[index] = val
        return

    mid = (left + right) // 2

    update_query(seg_tree, 2 * index + 1, left,    mid,   pos, val)
    update_query(seg_tree, 2 * index + 2, mid + 1, right, pos, val)

    seg_tree[index] = seg_tree[2 * index + 1] * seg_tree[2 * index + 2]


def build_tree(a, seg_tree, index, left, right):
    if left == right:
        seg_tree[index] = a[left]
        return

    mid = (left + right) // 2

    build_tree(a, seg_tree, 2 * index + 1, left,    mid)
    build_tree(a, seg_tree, 2 * index + 2, mid + 1, right)

    seg_tree[index] = seg_tree[2 * index + 1] * seg_tree[2 * index + 2]


if __name__ == '__main__':
    main()