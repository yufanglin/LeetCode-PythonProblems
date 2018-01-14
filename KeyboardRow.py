
class Solution:
	row1 = "qwertyuiop"
	row2 = "asdfghjkl"
	row3 = "zxcvbnm"

	def testWord(self, word):
		"""
		:type word: String
		:rtype:		Bool
		"""

		# create a set for the word to get rid of duplicates
		wordAsSet = "".join(set(word.lower()))
		
		# get the length of the word with no duplicate chars
		wordLength = len(wordAsSet)

		# create an index for the word
		index = 0

		# check if word is in row one
		for char in wordAsSet:
			# check if char is in row
			if char not in self.row1:
				# reset index and break out of loop
				index = 0
				break

			# check if this is the last character in word
			if index == wordLength-1:
				# word can be created from one keyboard row, return true
				return True

			# increment index
			index += 1


		# check if word is in row two
		for char in wordAsSet:
			# check if char is in row
			if char not in self.row2:
				# reset index and break out of loop
				index = 0
				break

			# check if this is the last character in word
			if index == wordLength-1:
				# word can be created from one keyboard row, return true
				return True

			# increment index
			index += 1


		# check if word is in row three
		for char in wordAsSet:
			# check if char is in row
			if char not in self.row3:
				# reset index and break out of loop
				index = 0
				break

			# check if this is the last character in word
			if index == wordLength-1:
				# word can be created from one keyboard row, return true
				return True

			# increment index
			index += 1
			


	def findWords(self, words):
		"""
		:type words: 	List[str]
		:rtype: 		List[str]
		"""
		# create a flag to check if words fit on one keyboard row
		fitOnOne = True

		# create an empty list to append one row words
		oneRowWords = []

		for word in words:
			# find out if the word can be made from one keyboard row
			fitOnOne = self.testWord(word)
			
			# If the word can, then append word to list
			if fitOnOne:
				oneRowWords.append(word)
		
		# return the list of words
		return oneRowWords

	


def main():
	# create an instance of the Solution class
	solution = Solution();

	# get an array of words
	test = ["Hello", "Alaska", "Dad", "Peace"]

	# pass the list from user to the solution class's method, and get the returned list
	returnedList = solution.findWords(test)

	print(returnedList)

if __name__ == "__main__":
	main()