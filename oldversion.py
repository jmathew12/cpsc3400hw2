# James Mathew
# cpsc3400
# hw2-2.py

import sys

# def createTree(file, tree):
#     with open(file, 'r') as inputFile:
#         for i in inputFile:
#             if insert(tree, int(i)) == -1:
#                 print(i + " is already in tree")
#             # makeTree(tree, int(i))
#     return tree

def search(tree, value):
    x = False
    if searchHelper(tree, value, x):
        x = True
    # print(x)
    return x

def searchHelper(tree, value, x):
    if len(tree) > 0:
        if not (x):
            if tree[0] == value:
                return True
            elif value > tree[0]:
                search(tree[2], value)
            elif tree[0] > value:
                search(tree[1], value)

def insert(tree, value):
    x = 0
    if search(tree, value):
        x = -1
    else:
        tree = makeTree(tree, value)
    return x

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
        if len(tree[1]) == 0:
            yield tree[0]
        else:
            yield from inOrder(tree[1])
            yield tree[0]
            yield from inOrder(tree[2])



input = sys.argv
tree = []
with open(input[1], 'r') as inputFile:
    for i in inputFile:
        print(i)
        insert(tree, int(i))
search(tree, 8)
print(tree)