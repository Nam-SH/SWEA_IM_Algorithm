import sys; sys.stdin = open('data/(5110)input.txt', 'r')

from another_linked_list import LinkedList



T = int(input())
N, M = map(int, input().split())

dl =LinkedList((list(map(int, input().split()))))

for i in range(M - 1):
    data = list(map(int, input().split()))
    for j in list(dl):
        if j > data[0]:


