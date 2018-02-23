'''
Number Complement
Yufang Lin

My Solution to leetCode problem called ,"Number Complement":
https://leetcode.com/problems/number-complement/description/
'''

class Solution:
	def findComplement(self, num):
		"""
		Find the binary complement of the number

		: type num 	:	int
		: rtype		:	int
		"""

		# create a tracker which will keep track of each '1' in its binary version
		tracker = num

		# create a number whose binary version will eventually only have one leftmost '1'
		leftMostOne = 0

		# loop until tracker has no 1 bitset in its binary version
		while(tracker):
			# leftMostOne will eventually only have one '1' left
			leftMostOne = tracker

			# switch the rightmost '1' in tracker to 0
			tracker &= tracker - 1


		# shift leftMostOne to the left, then swap all 0 bitsets to 1, and the 1 bitset to 0
		# then find the difference between leftMostOne and the number, this is the complement
		# 	ex: 4 (100) shift: 1000
		#		swap:	1000 - 0001 = 0111
		#		DiffL	5 ^ 7 = 101 ^ 111 = 010 <-- this is the complement, which is 2
		return num ^ ((leftMostOne << 1) - 1)


def main():
	# Create an instance of the Solution class
	sol = Solution()

	# Get user input
	number = int(input("Input a number:\t"))

	# complement
	complement = sol.findComplement(number)

	# print out solution
	print("Complement:\t", complement)

if __name__ == "__main__":
	main()