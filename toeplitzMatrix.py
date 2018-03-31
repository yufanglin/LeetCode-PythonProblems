"""
Title: 	Toeplitz Matrix
By:		Yufang Lin

My solution to the leetCode problem, "Toeplitz Matrix":
https://leetcode.com/problems/toeplitz-matrix/description/
"""

class Solution:
	def isToeplitzMatrix(self, matrix):
		"""
		:type matrix 	: List[List[int]]
		:rtype			: bool
		"""

		# loop through each row in the matrix
		for i, row in enumerate(matrix):
			# loop through each element in a row
			for j, elem in enumerate(row):
				#print(elem)
				# skip the first row/col, since they are the lower bound
				if(i > 0 and j > 0):
					# check if current element DOESN'T matches previous row/col element
					if (matrix[i-1][j-1] != elem):
						#print("Prev: ", matrix[-i][-j])
						#print("Curr: ", elem)
						# doesnt match, so not toeplitz
						return False
					# else continue to next element
					continue
				# else continue to next element
				continue

		# reached this point, meaning matrix is toeplitz
		return True

def main():
	# create an instance of the solutin class
	sol = Solution()

	# ---- Create two example Matrix ----
	toeplitzM= [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
	nonToeplitzM = [[1,2],[2,2]]

	# check matrix
	sol1 = sol.isToeplitzMatrix(toeplitzM)
	sol2 = sol.isToeplitzMatrix(nonToeplitzM)

	# print out results
	print("First Matrix is Toeplitz: ", sol1)
	print("Second Matrix is Toeplitz: ", sol2)

if __name__ == "__main__":
	main()