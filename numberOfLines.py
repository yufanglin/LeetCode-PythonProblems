"""
Title: 	Number of Lines To Write String
By:		Yufang Lin

My solution to the leetCode problem, "Number of Lines To Write String":
https://leetcode.com/problems/number-of-lines-to-write-string/description/
"""

class Solution:
	def numberOfLines(self, widths, S):
		"""
		Each line has a width of 100 units. 
		Each character's width may be many
		units wide. This function will 
		return the number of lines required to
		write out a string, as well as how many
		units were used in the last line.

		:type widths	: List[int]
		:type S 		: string
		:rtype			: List[int]
		"""

		# create a storage for the number of lines and current line's width
		lineCount = 1
		lineWidth = 0

		for c in S:
			# find the width of c by getting the index and retrieving the 
			# width from the widths list
			cWidth = widths[ord(c) - ord('a')]
			# add width to current line's width
			lineWidth += cWidth

			# Check if current line's width exceeds the max
			if (lineWidth > 100):
				# add a new line
				lineCount += 1
				# add the current character's width to current line's width
				lineWidth = cWidth


		# return the results
		return [lineCount, lineWidth]


def main():
	# create an instance of the solution class
	sol = Solution()

	# create two examples to test
	widths1 = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
	S1 = "abcdefghijklmnopqrstuvwxyz"

	widths2 = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
	S2 = "bbbcccdddaaa"

	# Find the solutions
	ans1 = sol.numberOfLines(widths1, S1)
	ans2 = sol.numberOfLines(widths2, S2)

	print("S1 has {0} lines, last line has {1} units used.".format(ans1[0], ans1[1]))
	print("S2 has {0} lines, last line has {1} units used.".format(ans2[0], ans2[1]))

if __name__ == "__main__":
	main()