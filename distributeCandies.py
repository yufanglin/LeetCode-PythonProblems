class Solution:
	def distributeCandies(self, candies):
		"""
		Returns the max number of different kinds of
		candies the sister of a brother-sister duo can gain

		:type 	candies : List[int]
		:rtype			: int
		"""
		# create a set for candies
		uniqueCandies = set(candies)
		
		# Find the min of uniqueCandies/candies list, that min is the max candy type
		return min(len(uniqueCandies), int(len(candies)/2))


def main():
	# create an instance of the solution class
	sol = Solution()

	# create examples 
	candies1 = [1,1,2,2,3,3]
	candies2 = [1,1,2,3]

	# find the max number of different types of candy that can be distributed
	maxCandyTypes1 = sol.distributeCandies(candies1)
	maxCandyTypes2 = sol.distributeCandies(candies2)

	# print out solution
	print("Example 1 Max Candy Types: ", maxCandyTypes1)
	print("Example 2 Max Candy Types: ", maxCandyTypes2) 

	pass

if __name__ == "__main__":
	main()