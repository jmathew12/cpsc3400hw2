# James Mathew
# cpsc3400
# hw2-2.py

import sys

def createTree( file, tree):
    with open(fi le, 'r') as inputFile:
        for i in inputFile:
            if insert(tree, int(i)) == -1:
                print("Duplicate value detected:", str(i))
    return tree

def search(tree, value):
    if len(tree) > 0:
        if (value == tree[0]):
            return True
        elif value > tree[0]:
            return search(tree[2], value)
        elif tree[0] > value:
            return search(tree[1], value)
    return False


def insert(tree, value):
    if search(tree, value):
        return -1
    else:
        makeTree(tree, value)
    return 0


def makeTree(tree, value):
    if len(tree) == 0:
        tree.append(value)
        tree.append([])
        tree.append([])
        return tree
    else:
        if value == tree[0]:
            return tree
        elif  value > tree[0]:
            tree[2] = makeTree(tree[2], value)
        elif tree[0] > value:
            tree[1] = makeTree(tree[1], value)
    return tree

def inOrder(tree):
    if len(tree) > 0:
            yield from inOrder(tree[1])
            yield tree[0]
            yield from inOrder(tree[2])



input = sys.argv
tree = []
tree = createTree(input[1], tree)
print("Step 3:")
print(tree)
print("Step 4:")
for i in range(1,10):
    if search(tree, i):
        print(str(i), "YES")
    else:
        print(str(i), "N0")
print("Step 5:")
for x in inOrder(tree):
    print(x)
listTreeInOrder = [n for n in inOrder(tree)]
print(listTreeInOrder)