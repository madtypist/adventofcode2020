def processAnswers(answers):
	result = {}

	for answer in answers:
		for char in answer:
			if char in result.keys():
				result[char] += 1
			else:
				result[char] = 1
	
	#print len(result)

	count = 0
	groupsize = len(answers)
	for key in result.keys():
		if result[key] == groupsize:
			count += 1

	return count

def main():
	rd = open("input-day6.txt")
	lines = rd.readlines()
	
	# initialize list and count
	groupanswers = []
	count = 0

	for line in lines:
		if (line != "\n"):
			# If it's not a newline, then it's still part of a group's answer
			groupanswers.append(line.strip())
		else:
			# If we've hit a newline, process the existing group answers, then reset the list
			count = count + processAnswers(groupanswers)
			groupanswers = []
	# do the final element, since we don't hit a final lone newline
	count = count + processAnswers(groupanswers)
	print count

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()