class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def printList(self):
    global res
    if self.size == 0:
        return
    cur = self.head
    while cur is not None:
        #print(cur.data, end=' ')
        res.append(str(cur.data))
        cur = cur.next


def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None:
        lst.head, lst.tail = first, last

    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]:
                break
            cur = cur.next
        if cur is None:
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None:
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)


import sys
sys.stdin = open("0410수열합치기.txt", "r")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]

    res = []
    ans = ''
    mylist = LinkedList()
    for i in range(M):
        addList(mylist, data[i])

    printList(mylist)
    res = res[-1:0:-1]
    for i in range(10):
        ans += res[i] + ' '

    print("#{} {}".format(tc+1, ans))