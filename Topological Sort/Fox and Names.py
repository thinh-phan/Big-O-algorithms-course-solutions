"""
Input:
3
rivest
shamir
adleman

Output:
bcdefghijklmnopqrtuvwxyzsa
"""
from sys import stdin, stdout
from queue import Queue

def main():
    global io
    io = Stdio()

    n = io.next_int()
    names = []

    # nhập các chuỗi tên vào một mảng chuỗi names
    for i in range(n):
        names.append(io.next())

    lexicographical = set_up_lexicographical(names)
    
    # trường hợp đặc biệt ta cần xét đó là khi 
    # chuỗi thứ i trong danh sách là hậu tố của 
    # chuỗi thứ i+1
    if lexicographical == None:
        io.println("Impossible")
        return

    result = topo_sort(lexicographical)

    if result == None:
        io.println("Impossible")
        return

    io.println(result)


def set_up_lexicographical(names):
    lexicographical = [[] for u in range(26)]
    # tạo mảng bool 2 chiều 26∗26 phần tử
    # tượng trưng cho quan hệ giữa 26 ký tự với nhau
    relation = [[False for v in range(26)] for u in range(26)]
        
    # Duyệt i từ chuỗi đầu đến chuỗi áp chót trong names
    # Mỗi lần duyệt ta sẽ có 1 biến bool là 
    # flag sẽ gán bằng false lúc đầu, nhiệm vụ 
    # của biến này là để kiểm tra trường hợp đặc biệt
    for i in range(len(names) - 1):
        flag = False
        min_size = min(len(names[i]), len(names[i + 1]))
        # Duyệt tiếp j từ 0 đến độ dài của chuỗi 
        # ngắn hơn trong 2 chuỗi ta đang xét để 
        # tìm ký tự khác nhau đầu tiên giữa 2 chuỗi.
        # Sau đó ta gán flag = true tức đây không phải 
        # là trường hợp đặc biệt.
        for j in range(min_size):
            if names[i][j] != names[i + 1][j]:
                relation[ord(names[i][j]) - 97][ord(names[i + 1][j]) - 97] = True
                flag = True
                break
        # chuỗi names​[i] là hậu tố của chuỗi names​[i+1​] , 
        # lúc này ta chỉ cần xuất thẳng Impossible và 
        # kết thúc chương trình.
        if not flag and len(names[i]) > len(names[i + 1]):
            return None

    for i in range(26):
        for j in range(26):
            if relation[i][j]:
                lexicographical[i].append(j)

    return lexicographical


def topo_sort(lexicographical):
    in_deg = [0 for u in range(26)]
    result = []
    zero_in_deg_queue = Queue()

    for u in range(26):
        for v in lexicographical[u]:
            in_deg[v] += 1

    for u in range(26):
        if in_deg[u] == 0:
            zero_in_deg_queue.put(u)

    while not zero_in_deg_queue.empty():
        u = zero_in_deg_queue.get()
        result.append(chr(u + 97))

        for v in lexicographical[u]:
            in_deg[v] -= 1

            if in_deg[v] == 0:
                zero_in_deg_queue.put(v)

    for u in range(26):
        if in_deg[u] != 0:
            return None

    return ''.join(str(c) for c in result)


class Stdio:
    index = 0
    tokens = []
    line = None

    def next_line(self):
        tokens = []
        return stdin.readline()

    def next(self):
        while (self.index >= len(self.tokens)):
            self.tokens = self.next_line().strip().split()
            if len(self.tokens) == 0:
                return None
            self.index = 0
        token = self.tokens[self.index]
        self.index += 1
        return token

    def next_int(self):
        return int(self.next())

    def next_float(self):
        return float(self.next())

    def next_char(self):
        return chr(self.next())

    def print(self, *objects):
        for obj in objects:
            stdout.write(str(obj))

    def println(self, *objects):
        for obj in objects:
            stdout.write(str(obj))
        stdout.write('\n')


if __name__ == "__main__":
    main()