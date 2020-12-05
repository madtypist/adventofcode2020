#!/usr/bin/python
import re

def checkFieldsExist(passport):
	# these are the fields we're looking for:
	result = True
	fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

	#print passport

	for field in fields:
		# Check for mandatory field in passport string
		isMissing = (passport.find(field) == -1)
		if isMissing:
			print "Missing %s" % (field)
			result = False
		#else:
			#print "Found %s" % (field)


	return result

def validatePassport(passport):
	# If all the fields are there, stuff them into a hash so we can just brute force this
	result = checkFieldsExist(passport)
	print "Has all the fields? %r" % (result)

	fields = dict()

	if result:
		# If all the fields are there, stuff them into a hash so we can just brute force this
		temp = passport.split()
		for pair in temp:
			x = pair.split(":")
			fields[x[0]] = x[1]

		# Check the dates
		print "Date %s in range 1920-2002? %r" % (fields['byr'], 1920 <= int(fields['byr']) <= 2002)
		print "Date %s in range 2010-2020? %r" % (fields['iyr'], 2010 <= int(fields['iyr']) <= 2020)
		print "Date %s in range 2020-2030? %r" % (fields['eyr'], 2020 <= int(fields['eyr']) <= 2030)
		result = result and (1920 <= int(fields['byr']) < 2003)
		result = result and (2010 <= int(fields['iyr']) <= 2020)
		result = result and (2020 <= int(fields['eyr']) <= 2030)

		# check height
		if ("cm" in fields['hgt']):
			result = result and (150 <= int(fields['hgt'].strip('cm')) <= 193)
			print fields['hgt']
		else:
			result = result and (59 <= int(fields['hgt'].strip('in')) <= 76)
			print fields['hgt']

		# check hair color - a # followed by exactly six characters 0-9 or a-f
		exp = "#[a-fA-F0-9]{6}"
		if not re.match(exp,fields['hcl']):
			print "Color is invalid: %s" % (fields['hcl'])
			result = False
		else:
			print "Color %s is valid: " % (fields['hcl'])

		# check eye color
		result = result and fields['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']

		# REMOVE
		tmp = fields['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']
		print "Eye color = %s %r" % (fields['ecl'],tmp)

		# check passport id
		exp = "\d{9}"
		if not re.match(exp,fields['pid']):
			result = False
			print "PID is invalid: %s" % (fields['pid'])

	return result


def main():
	rd = open("input-day4.txt")
	#rd = open ("test.txt")
	lines = rd.readlines()

	passport = ""
	countValid = 0

	for line in lines:
		if line == "\n":
			# process current passport
			print passport
			result = validatePassport(passport)
			print "Passport valid? %r \n" % (result)
			if result:
				countValid += 1
				print countValid
			
			# reset passport
			passport = ""
		
		else:
			passport = passport + line.replace('\n',' ')

	if validatePassport(passport):
		countValid += 1
		print "Passport is Valid!"
	else:
		print "Passport invalid"

	print "Valid passports: %d" % (countValid)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()