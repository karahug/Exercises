#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import deque
def isTreeSymmetric(t):
    if t== None:
        return True
    leftQueue = deque([t.left])
    rightQueue = deque([t.right])
    while len(leftQueue) > 0 and len(rightQueue) > 0:
        leftTree = leftQueue.pop()
        rightTree = rightQueue.pop()
        if(compareNode(leftTree, rightTree)):
            if(leftTree != None):
                leftQueue.appendleft(leftTree.left)
                leftQueue.appendleft(leftTree.right)
                rightQueue.appendleft(rightTree.right)
                rightQueue.appendleft(rightTree.left)
        else:
            return False
    return True

def compareNode(node1, node2):
    if node1 == None and node2 == None:
        return True
    elif((node1 == None) ^ (node2 == None)):
        return False
    else:
        return node1.value == node2.value
