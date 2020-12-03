def toboggan(course,right,down):
	trees = 0

	#initialize our position tracker
	x = 0
	y = 0
	stoppingpoint = len(course) - 1

	while y < stoppingpoint:
		# update sled position
		x = x + right
		y = y + down
		
		row = course[y]
		column = x % 31

		#print "y = %d temp = %d" % (y,column)

		# Check if we hit a tree
		if row[column] == "#":
			trees += 1
		#print row[column]

	return trees

def main():
	# Read file with day 3 inputs
	rd = open("input-day3.txt")
	lines = rd.readlines()

	slope = []

	# make the board
	for line in lines:
		temp = []
		for char in line.strip():
			temp.append(char)
		#print temp
		slope.append(temp)
	#print "%d %d %d %d %d" % (toboggan(slope,3,1),toboggan(slope,1,1),toboggan(slope,5,1),toboggan(slope,7,1),toboggan(slope,2,1))
	run1 = toboggan(slope,1,1)
	run2 = toboggan(slope,3,1)
	run3 = toboggan(slope,5,1)
	run4 = toboggan(slope,7,1)
	run5 = toboggan(slope,1,2)

	print run1
	print run2
	print run3
	print run4
	print run5
	print run1 * run2 * run3 * run4 * run5

	#print "Product of trees = %d" % (result)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()