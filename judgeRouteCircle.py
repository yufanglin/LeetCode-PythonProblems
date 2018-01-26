class Solution:
	def judgeCircleBetter(self, moves):
		"""
		: Checks if the moves lead back to the original position
		: the better version
		: type moves	: str
		: rtype			: bool
		"""

		return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

	def judgeCircle(self, moves):
		"""
		: Checks if the moves lead back to the original position
		: type moves	: str
		: rtype			: bool
		"""

		# keep track of the x, y positions
		pos = [0, 0]			# [x, y]

		# loop through the moves 
		for move in moves:
			# Check if the move is right
			if move == 'R':
				# increment the x pos of the position array
				pos[0] += 1
				# continue to the next move
				continue

			# Check if the move is left
			elif move == 'L':
				# decrement the x pos of the position array
				pos[0] -= 1
				# continue to the next move
				continue

			# Check if the move is up
			elif move == 'U':
				# increment the y pos of the position array
				pos[1] += 1
				# continue to the next move
				continue

			# Check if the move is down
			elif move == 'D':
				# decrement the y pos of the position array
				pos[1] -= 1
				# continue to the next move
				continue


		# check if the position is still 0,0
		if pos == [0,0]:
			# route is a circle
			return True

		# else the route is not a cicle
		return False


def main():
	# Create an instance of the solution class
	sol = Solution()

	# Print out instructions
	print("""\n Judge Route Circle \n
		Instruction:	input moves in the form of a string
		Example:	 	UD
		Movies:			Up: U | Down: D | Left: L | Right: R\n""")
	
	# Get user input for the moves
	moves = input("Input the moves in the form of a string: ")

	# Get the answer to whether or not the moves leads back to original position
	ans = sol.judgeCircle(moves)

	print("The route is a circle: ", ans)

if __name__ == '__main__':
	main();