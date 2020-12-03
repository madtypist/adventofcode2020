def findpair(numberlist):
	index1 = 0
	index2 = len(numberlist) - 1

	for i in range(0,len(numberlist)/2):
		value = numberlist[i] + numberlist[index2]
		while value > 2020:
			index2 = index2 - 1
			value = numberlist[i] + numberlist[index2]
		
		if value == 2020:
			break

	return [i,index2]

def findtriples(numlist):
	# Initial values
	i1 = 0
	i2 = 1
	i3 = len(numlist) - 1

	# GOD FORGIVE ME FOR THE DUPLICATE CODE AND MULTIPLE LOOPS
	# But at least my algorithm isn't as horrifying in terms of runtime as it could be
	
	for i1 in range (0,len(numlist)/2):
		
		# compute the things
		firsttwo = numlist[i1] + numlist[i2]
		value = firsttwo + numlist[i2]

		# did we find it?
		if value == 2020:
			print "Found it! i1: %d value: %d i2: %d value: %d i3: %d value: %d" % (i1, numlist[i1],i2,numlist[i2],i3,numlist[i3])
			results = [i1,i2,i3]
			break

		#If not, first shift cursor 3 right until we get under 2020
		while value > 2020 and i3 > i2:
			i3 = i3 - 1
			value = firsttwo + numlist[i3]

			# did we find it?
			if value == 2020:
				print "Found it! i1: %d value: %d i2: %d value: %d i3: %d value: %d" % (i1, numlist[i1],i2,numlist[i2],i3,numlist[i3])
				results = [i1,i2,i3]
				break

		# At some point, we're under 2020
		# Reset cursor 3
		i3 = len(numlist) - 1
		# Move cursor 2 once place and enter another shifty loopy thing
		i2 += 1

		# Move cursor 2 1 place and try again, moving cursor 3 each time down the line
		while i2 < i3 - 1:
			firsttwo = numlist[i1] + numlist[i2]
			value = firsttwo + numlist[i3]
			if value == 2020:
				print "Found it! i1: %d value: %d i2: %d value: %d i3: %d value: %d" % (i1, numlist[i1],i2,numlist[i2],i3,numlist[i3])
				results = [i1,i2,i3]
				break
			
			# Move cursor 3 but don't go past cursor 2!
			while (value > 2020) and (i3 > i2):
				i3 = i3 - 1
				value = firsttwo + numlist[i3]

				# did we find it?
				
				if value == 2020:
					print "Found it! i1: %d value: %d i2: %d value: %d i3: %d value: %d" % (i1, numlist[i1],i2,numlist[i2],i3,numlist[i3])
					results = [i1,i2,i3]
					break

			i2 += 1

			# Reset cursor 3
			i3 = len(numlist) - 3

		#Okay, we didn't find it, so let's reset cursor 2 two spaces over from cursor 1
		i2 = i1 + 2
		# did we find it?
		if value == 2020:
			print "Found it! i1: %d value: %d i2: %d value: %d i3: %d value: %d" % (i1, numlist[i1],i2,numlist[i2],i3,numlist[i3])
			results = [i1,i2,i3]
			break

	return results

def main():
	# load values from file
	mylist = []

	rd = open("day1input.txt")
	lines = rd.readlines()
	for line in lines:
		mylist.append(int(line.strip()))

	#Sort the list
	mylist.sort()

	# call function to check the addition and return the values
	pair = findpair(mylist)

	# multiply!
	print "mylist[%d] = %d" % (pair[0], mylist[pair[0]])
	print "mylist[%d] = %d" % (pair[1], mylist[pair[1]])
	print mylist[pair[0]] * mylist[pair[1]]

	triples = findtriples(mylist)
	print "Triples result:"
	print triples
	print mylist[triples[0]] * mylist[triples[1]] * mylist[triples[2]]

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()