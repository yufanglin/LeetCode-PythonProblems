'''
Island Perimeter
Yufang Lin
My solution to the leetCode problem, "Island Perimeter":
https://leetcode.com/problems/island-perimeter/description/
'''

class Solution:
	def islandPerimeter(self, grid):
		"""
		The grid is made out of 0's and 1's
		Each 0 is a water cell, while each 1 is a land cell.
		All cells have four sides with a length of one.
		This method counts the perimeter of an island that is 
		made out of a combination of land cells.

		:type grid	: List[List[int]]
		:rtype		: int
		"""
		perimeter = 0

		# loop through the rows in the grid
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				# check if cell is water, if so, skip to next element
				if (grid[row][col] == 0):
					continue

				# Check if land cell's top is connected to water or boundary
				if (row - 1 == -1 or grid[row-1][col] == 0):
					perimeter += 1

				# Check if land cell's right is connected to water or boundary
				if (col + 1 == len(grid[0]) or grid[row][col+1] == 0):
					perimeter += 1

				# Check if land cell's bottom is connected to water or boundary
				if (row + 1 == len(grid) or grid[row+1][col] == 0):
					perimeter += 1

				# Check if land cell's left is connected to water or boundary
				if (col - 1 == -1 or grid[row][col-1] == 0):
					perimeter += 1

		return perimeter

def main():
	# create a Solution instance
	sol = Solution()

	# create examples for testing
	grid1 = [	[0,1,0,0],
				[1,1,1,0],
				[0,1,0,0],
				[1,1,0,0]]

	grid2 = [[0,1]]

	# get the perimeter of each grid
	perimeter1 = sol.islandPerimeter(grid1)
	perimeter2 = sol.islandPerimeter(grid2)


	# print out results
	print("Island 1 Perimeter: ", perimeter1)
	print("Island 2 Perimeter: ", perimeter2)


if __name__ == "__main__":
	main()

