'''
 Trim a Binary Search Tree
 Yufang Lin

 My solution to the leetCode problem called, "Trim a Binary Search Tree":
 https://leetcode.com/problems/trim-a-binary-search-tree/description/
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def trimBST(self, root, L, R):
		"""
		: type	root	: TreeNode
		: type 	L 		: int
		: type	R 		: int
		: rtype 		: TreeNode
		"""

		### Case: end of tree or no nodes in tree
		if (root == None):
			return None

		### Case: Root's value is greater than the upper bound
		if (root.val > R):
			# traverse left since its value will be less than root's and hopefully within bounds
			return self.trimBST(root.left, L, R)

		### Case: Root's value is lesser than the lower bound
		if (root.val < L):
			# traverse right since its value will be less than root's and hopefully within bounds
			return self.trimBST(root.right, L, R)

		### Case: Found a root that fits within range
		# set Left Child of root
		root.left = self.trimBST(root.left, L, R)

		# set Right Child of root
		root.right = self.trimBST(root.right, L, R)

		return root


def main():
	# create an instance of the Solution class
	sol = Solution()


	# Binary Search Tree example 1
	root1 = TreeNode(1)
	rt1LeftChild = TreeNode(0)
	rt1RightChild = TreeNode(2)

	root1.left = rt1LeftChild
	root1.right = rt1RightChild


	# Binary Search Tree example 2
	root2 = TreeNode(3)
	rt2LeftChild = TreeNode(0)
	rt2RightChild = TreeNode(4)
	rt2LeftRightChild = TreeNode(2)
	rt2LeftRightLeftChild = TreeNode(1)

	root2.left = rt2LeftChild
	root2.right = rt2RightChild
	root2.left.right = rt2LeftRightChild
	root2.left.right.left = rt2LeftRightLeftChild


	# trim examples
	exSol1 = sol.trimBST(root1, 1, 2)
	exSol2 = sol.trimBST(root2, 1, 3)


if __name__ == "__main__":
	main()