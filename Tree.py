class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def create_two(index, length, arr):
    if index > length:
        return None

    node = Node(arr[index])
    node.left = create_two(index * 2 + 1, length, arr)
    node.right = create_two(index * 2 + 2, length, arr)

    return node


def BFS(root):
    queue = [root]
    while queue:
        cur = queue.pop(0)
        print(cur.value)

        if cur.left:
            queue.append(cur.left)

        if cur.right:
            queue.append(cur.right)


arr = [1, 2, 3, 4, None, None, None, None, None]
length = len(arr) - 1
head = create_two(0, length, arr)

print(head.value)
print(head.left)
print(head.right)

# BFS(head)

print("jfoisdjfoisdjfiosdnviuaf")

print(10 * 2 / 3 + 5 / 3)


a = 6400000
b = 6400 + 100

for i in range(9, 0, -1):
    print(i)