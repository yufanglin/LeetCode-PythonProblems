class Solution:
	def fizzBuzz(self, n):
		"""
		:type 	n: int
		:rtype	 : List[str]
		"""

		# create a list to hold the fizz buzz array
		fizzBuzzList = []

		# Loop n times, starting at 1 and including n
		for i in range(1, n+1):
			# Check if integer is divisible by 3 and 15
			if i % 15 == 0:
				fizzBuzzList.append("FizzBuzz")
				continue

			# Check if integer is divisible by 3
			elif i % 3 == 0:
				fizzBuzzList.append("Fizz")
				continue

			# Check if integer is divisible by 5
			elif i % 5 == 0:
				fizzBuzzList.append("Buzz")
				continue

			# Otherwise just append the integer
			else:
				fizzBuzzList.append('%s' % i)

		return fizzBuzzList

def main():
	# create an instance of the Solution class
	sol = Solution()

	# get user input
	usrInput = int(input("Enter an integer: "))

	# get the fizz buzz array
	ans = sol.fizzBuzz(usrInput)
	print("Output: ", ans)

if __name__ == "__main__":
	main()