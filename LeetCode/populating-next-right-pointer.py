#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        level = 2
        count = 0 
        queue = [root]
        while count != len(queue):
            if queue[count].left:
                queue.append(queue[count].left)
                queue.append(queue[count].right)
            if count == level - 2:
                queue[count].next = None 
                level *= 2
            else:
                queue[count].next = queue[count+1]
            count += 1     

        