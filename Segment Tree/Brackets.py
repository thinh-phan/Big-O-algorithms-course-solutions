from sys import stdin, stdout

N = 30009

class segment_tree_node:
    def __init__(self, _open, _close):
        self.open = _open
        self.close = _close
        self.match = 0
    
n = 0
m = 0
st = str()
segment_tree = [0 for _ in range(4 * N)]

def calculate (left, right):
    result = segment_tree_node(0, 0)
    result.match = min(left.open - left.match, right.close - right.match) + left.match + right.match
    result.open = left.open + right.open;
    result.close = left.close + right.close;
    return result;

def build_tree (left, right, index):
    if left == right:
        if st[left] == ')':
            segment_tree[index] = segment_tree_node(0, 1)
        else:
            segment_tree[index] = segment_tree_node(1, 0)
        return

    mid = (left + right) // 2

    build_tree(left, mid, 2 * index + 1)
    build_tree(mid + 1, right, 2 * index + 2)
 
    segment_tree[index] = calculate(segment_tree[2 * index + 1], segment_tree[2 * index + 2])

def update_tree (left, right, pos, index):
    if pos < left or right < pos:
        return
    
    if left == right:
        if segment_tree[index].close == 1:
            segment_tree[index] = segment_tree_node(1, 0)
        else:
            segment_tree[index] = segment_tree_node(0, 1)
        return

    mid = (left + right) // 2
 
    update_tree(left, mid, pos, 2 * index + 1)
    update_tree(mid + 1, right, pos, 2 * index + 2)
 
    segment_tree[index] = calculate(segment_tree[2 * index + 1], segment_tree[2 * index + 2])


if __name__ == "__main__":
    for t in range(10):
        n = int(stdin.readline())
        st = stdin.readline()
        m = int(stdin.readline())

        stdout.write("Test " + str(t + 1) + ":\n")
        build_tree(0, n - 1, 0)

        for i in range(m):
            p = int(input())
            if p == 0:
                if segment_tree[0].match == n // 2 and n % 2 == 0:
                    stdout.write("YES\n")
                else:
                    stdout.write("NO\n")
            else:
                update_tree(0, n - 1, p - 1, 0)