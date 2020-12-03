def getrules(strRules):
	temp = strRules.split()

	# parse out letter
	letter = temp[1]

	# parse out ranges, cast them to ints
	temp2 = temp[0].split("-")
	lower = int(temp2[0])
	higher = int(temp2[1])

	#print "lower = %d and higher = %d" % (lower,higher)

	return [lower,higher,letter]

def checkPassword(input):
	# get the rule set
	chunks = input.split(": ")
	ruleset = getrules(chunks[0])
	password = chunks[1].strip()

	#print password
	letterCount = 0

	for char in password:
		if char == ruleset[2]:
			letterCount += 1

	print "letterCount for %s = %d" % (ruleset[2],letterCount)
	if letterCount >= ruleset[0] and letterCount <= ruleset[1]:
		result = True
		print "Valid Password!\n"
	else:
		result = False
		print "Invalid Password :(\n"

	#print input
	return result

def otherCheckPassword(input):
	# get the rule set
	chunks = input.split(": ")
	ruleset = getrules(chunks[0])
	password = chunks[1].strip()
	letterCount = 0

	# This time, need to check if it appears only once in index 1 and 2
	pos1 = password[ruleset[0]-1]
	pos2 = password[ruleset[1]-1]
	
	print password
	print "pos %d %s pos %d %s" % (ruleset[0],pos1,ruleset[1],pos2)

	if pos1 == ruleset[2]:
		letterCount += 1
	if pos2 == ruleset[2]:
		letterCount += 1

	result = (letterCount == 1) 
	print "looking for %s in pos %d or pos %d %s \n" % (ruleset[2],ruleset[0],ruleset[1],result)

	return result

def main():
	validPasswords = 0
	
	# Read in input from password
	rd = open("day2input.txt")
	lines = rd.readlines()
	for line in lines:
		# if checkPassword(line):
		if otherCheckPassword(line):
		 	validPasswords += 1
		

	print validPasswords

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()