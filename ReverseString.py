
class Solution:
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		return s[::-1]


def main():
	
	solution = Solution()

	userStr = input("Please enter a string to reverse: ")

	reverseStr = solution.reverseWords(userStr)

	print("Output: " + reverseStr)


if __name__ == "__main__":
	main()