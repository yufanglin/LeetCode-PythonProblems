class Solution:
	def selfDividingNumbers(self, left, right):
		"""
		:type left: int
		:type right: int
		:rtype: List[int]
		"""

		# create an empty list to append to and return
		selfDividingNumList = []

		# check case: right bound is 10 or less 
		if right < 10: 
			selfDividingNumList = list(range(left,right+1))
			
			return selfDividingNumList

		elif right == 10:
			selfDividingNumList = list(range(left,right))
			
			return selfDividingNumList

		# check case: left bound is less than 10
		elif left < 10:
			selfDividingNumList = list(range(left,10))
			# because 10 isn't self dividing, set left to 11
			left = 11

		# loop through the left and right bounds
		for num in range(left, right+1):

			# get the num as a string to get specific
			numStr = str(num)

			# get the number of digits in num
			numLen = len(str(num))

			# loop through each digit in number
			while(numLen > 0):
				
				# check if digit is 0, if so break
				if int(numStr[numLen-1]) == 0:
					break

				# check if number can be divided
				if num % int(numStr[numLen-1]) == 0:
					# check if this is the last digit the number is to be divided by
					if numLen == 1:
						# append the number to the list
						selfDividingNumList.append(num)
				else:
					break

				numLen -= 1


		return selfDividingNumList

def main():
	solution = Solution()

	# get user input
	leftBound = int(input("Input left bound: "))
	rightBound = int(input("Input right bound: "))

	selfDividingNumList = []
	selfDividingNumList = solution.selfDividingNumbers(leftBound,rightBound)
	print(selfDividingNumList)


if __name__ == "__main__":
	main()