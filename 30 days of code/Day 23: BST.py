import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        a=list()
        nt=""
        a.append(root)
        while(len(a)>0):
            node=a.pop(0)
            if node.left:
                a.append(node.left)
            if node.right:
                a.append(node.right)
            nt+=str(node.data)+" "
        print(nt) 
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
