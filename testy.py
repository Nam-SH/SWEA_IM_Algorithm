import sys; sys.stdin = open('data/(5110)input.txt', 'r')

class Node:
    def __init__(self, data, pre, link):
        self.data = data
        self.pre = pre
        self.link = link

def addLast(data):
    global pHead
    global pTail
    if pHead == None:
        pHead = Node(data, None, None)
        pTail = pHead
    else:
        p = pHead
        while p.link != None:
            p = p.link
        p.link = Node(data, p, None)
        pTail = p.link
    return


def addNumbers():
    global pHead
    global pTail
    p = pHead
    if p == None:
        for i in range(N): addLast(s[i])
    else:
        while p.link != None and p.data <= s[0]:
            p = p.link
        if p.data > s[0]:
            if p.pre == None:
                p.pre = Node(s[0], None, p)
                pHead = p.pre
                for i in range(1, N):
                    p.pre.link = Node(s[i], p.pre, p)
                    p.pre = p.pre.link
            else:
                for i in range(N):
                    p.pre.link = Node(s[i], p.pre, p)
                    p.pre = p.pre.link
        else:
            for i in range(N): addLast(s[i])
    return


def print_res():
    global pTail
    p = pTail
    for i in range(10):
        print(p.data, end=' ')
        p = p.pre
    print()

for tc in range(int(input())):
    N, M = map(int, input().split())
    pHead = None
    pTail = None
    for i in range(M):
        s = list(map(int, input().split()))
        addNumbers()
    print('#' + str(tc + 1), end=' ')
    print_res()
