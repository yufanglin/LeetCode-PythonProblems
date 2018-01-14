
class Solution:
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		# split the string based on spaces
		wordList = s.split(' ')
		reverseWordList = []

		# loop through words in list
		for word in wordList:
			reverseWordList.append(word[::-1])

		# Now join the words in the list to create one string
		return " ".join(reverseWordList)


def main():
	
	solution = Solution()

	userStr = input("Please enter a string to reverse: ")

	reverseStr = solution.reverseWords(userStr)

	print("Output: " + reverseStr)


if __name__ == "__main__":
	main()