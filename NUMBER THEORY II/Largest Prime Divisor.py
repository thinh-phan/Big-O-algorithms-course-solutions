from sys import stdin, stdout

def main():
    global io
    io = Stdio()

    while True:
        n = io.next_int()
        
        if n == 0:
            break
        
        io.println(largest_prime_divisor(abs(n)))


def largest_prime_divisor(n):
    res = -1
    cnt = 0
    
    i = 2
    
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            res = i
        
        while n % i == 0:
            n //= i

        i += 1

    if cnt > 0 and n > 1:
        return n
    elif cnt == 1:
        return -1

    return res


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