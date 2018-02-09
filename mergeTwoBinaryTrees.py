'''
My solution to the 'Merge Two Binary Trees' LeetCode problem found here:
https://leetcode.com/problems/merge-two-binary-trees/description/
'''
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        # Check if nodes t1 & t2 exists
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        # Both nodes exists, add the values together
        t1.val += t2.val;
        
        # Traverse to left child
        t1.left = self.mergeTrees(t1.left, t2.left)
        
        # Traverse right child
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        # return the new t1 node
        return t1
        