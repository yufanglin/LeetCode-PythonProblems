"""
Title: 	Baseball Game
By:		Yufang Lin

My solution to the leetCode problem, "Baseball Game":
https://leetcode.com/problems/baseball-game/description/
"""

class Solution:
	def calPoints(self, ops):
		"""
		:Calculate the total sum of a score set.
			Int: Directly represents the number of points you get in this round.
			"+": Represents that the points you get in this round are the sum of 
				 the last two valid round's points.
			"D": Represents that the points you get in this round are the doubled 
			  	 data of the last valid round's points.
			"C": Represents the last valid round's points you get were invalid and 
				 should be removed.

		:type ops	: List[str]
		:rtype		: int
		"""

		# Case: check if list is empty
		if not ops:
			# break out method
			return

		# Create a storage of valid scores
		validScores = []


		# loop through the list
		for score in ops:
			# Remove last valid points
			if score is 'C':
				# check to see if there are any valid scores
				if validScores:
					# remove last score
					validScores.pop()
					# continue to next score
					continue
				# else, continue to next score
				continue

			# Double last valid points for this round's points
			elif score is 'D':
				# check to see if there are any valid scores
				if validScores: 
					# double last valid score and append
					validScores.append(validScores[-1] * 2)
					# continue to next score
					continue
				# else, continue to next score
				continue

			# Add last two valid points for this round's points
			elif score is '+':
				# check to see if there are any valid scores
				if (len(validScores) > 1):
					# append this round's score to list of valid scores
					validScores.append(validScores[-1] + validScores[-2])
					#continue to next score
					continue
				# else, continue to next score
				continue

			# add points to current
			else:
				# append score to the list of validScores
				validScores.append(int(score))
				# continue to next score
				continue

		# return the calculated score
		return sum(validScores)

def main():
	# create an instance of the solution class
	sol = Solution()

	# create two list examples
	score1 = ["5","2","C","D","+"]
	score2 = ["5","-2","4","C","D","9","+","+"]

	# get the sum of the scores
	score1Sum = sol.calPoints(score1)
	score2Sum = sol.calPoints(score2)

	# print out the solution
	print("Total Points 1: ", score1Sum)
	print("Total Points 2: ", score2Sum)


if __name__ == "__main__":
	main()