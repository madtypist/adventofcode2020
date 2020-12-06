def getSeat(ticket):
	row = 0
	rowEnd = 127
	col = 0
	colEnd = 7
	
	maxrow = 127
	maxcol = 7

	# process the ticket
	for char in ticket.strip():
		if char == "F":
			maxrow = maxrow / 2
			rowEnd = rowEnd - maxrow - 1
		if char == "B":
			maxrow = maxrow / 2
			row = row + maxrow + 1
		if char == "L":
			maxcol = maxcol / 2 
			colEnd = colEnd - maxcol - 1
		if char == "R":
			maxcol = maxcol / 2
			col = col + maxcol + 1

		#print "%s Row: %s RowEnd: %s Col: %s ColEnd: %s Max col and row: %s, %s" % (char, row, rowEnd, col, colEnd, maxcol, maxrow)
	
	seatNum = (row * 8) + col
	print "Final result: Row %s Col %s ID: %s" % (row,col, seatNum)
	
	return seatNum

def findMySeat(ids):
	for i in range(1,len(ids)-2):
		if ids[i] == (ids[i-1] + 2):
			print "IDs: %s and %s" % (ids[i], ids[i-1])
	return 0

def main():
	rd = open("input-day5.txt")
	lines = rd.readlines()
	highestSeat = 0
	seatIDs = []

	for line in lines:
		if (line != "\n"):
			currentSeat = getSeat(line)
			if currentSeat > highestSeat:
				highestSeat = currentSeat
			seatIDs.append(currentSeat)
		else:
			print "\n"

	print "Highest seat is: %s" % (highestSeat)
	seatIDs.sort()
	findMySeat(seatIDs)
	#print seatIDs


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()