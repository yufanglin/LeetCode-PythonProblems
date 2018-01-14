class Solution:
	def arrayPairSum(self, nums):
		"""
		:type nums	:	List[int]
		:rtype		: 	int
		"""

		# sort the nums array
		nums = sorted(nums)

		# keep track of the sum
		minSum = 0

		# loop through the even indexes in the array
		for i in range(int(len(nums) / 2)):
			minSum += nums[2 * i]

		return minSum



def main():
	# Create a Solution object 
	solution = Solution()

	# Ask the user to input a list of integers
	nums = [int(x) for x in input("Please input a list of integers: ").split()]

	# Find the largest sum of the mins in each pair from the list
	minSum = solution.arrayPairSum(nums)

	# Print the sum
	print(minSum)


if __name__ == "__main__":
	main()