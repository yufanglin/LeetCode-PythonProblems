'''
Hamming Distance
Yufang Lin

My Solution to leetCode problem called ,"Hamming Distance":
https://leetcode.com/problems/hamming-distance/description/
'''

class Solution:
	def hammingDistance(self, x, y):
		"""
		Find the hamming distance between x and y
		:type	x:	int
		:type 	y:	int
		:rtype	 :	int
		"""

		# contert x and y to binary

		# createa variable to store the distance
		dist = 0

		diff = x^y;

		# while there is a difference
		while(diff):
			dist += 1
			diff &= diff - 1;

		# return distance
		return dist

def main():
	# create an instance of the solution class
	sol = Solution()

	# get two values from user
	xInput = int(input("Enter x value: "))
	yInput = int(input("Enter y value: "))

	# get the distance
	dist = sol.hammingDistance(xInput, yInput)

	# print out the solution
	print("Hamming Distance: ", dist)

if __name__ == "__main__":
	main()