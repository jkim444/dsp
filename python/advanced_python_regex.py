##############################################################
## NOTE: Type-O found
## Line number 26, Michelle Elena Ross
## ~ Professor "is" Biostatistics ~ 
## For the purpose of this practice, I corrected the csv file
## from "is" to "of"
##
## Please take this modification into account 
##############################################################


import re
import csv
import pprint as pp
from collections import defaultdict

def readCsv(filename):
	file = open(filename, 'r')

	numDegrees_temp = []
	numDegrees_dict = defaultdict(int)
	numTitles = defaultdict(int)
	emailAdd = []
	emailDomain = defaultdict(int)

	for line in file.readlines():
		regex_degree = re.findall(r'PhD|Ph.D|MA|MD|Sc.D|ScD|MD|MPH|BSEd|B.S.Ed|MS|M.S|JD|0', line)
		regex_title = re.search(r'[^,]*Professor[^,]*', line)
		regex_email = re.search(r'[^,]*[@].*\.edu', line)
		regex_domain = re.search(r'[@].*\.edu', line)

		if regex_degree:
			#numDegrees[regex_degree.group()] += 1
			numDegrees_temp.append(regex_degree)

		if regex_title:
			numTitles[regex_title.group()] += 1

		if regex_email:
			emailAdd.append(regex_email.group())

		if regex_domain:
			emailDomain[regex_domain.group()] += 1

	for item in numDegrees_temp:
		for x in item:
			if x == "Sc.D" or x == "ScD":
				numDegrees_dict["ScD"] += 1
			if x == "MD" or x == "M.D":
				numDegrees_dict["MD"] += 1
			if x == "Ph.D" or x == "PhD":
				numDegrees_dict["PhD"] += 1
			if x == "JD" or x == "J.D":
				numDegrees_dict["JD"] += 1
			if x == "B.S.Ed" or x == "BSEd":
				numDegrees_dict["BSEd"] += 1
			if x == "M.P.H" or x == "MPH":
				numDegrees_dict["MPH"] += 1
			if x == "M.S" or x == "MS":
				numDegrees_dict["MS"] += 1
			if x == "M.A" or x == "MA":
				numDegrees_dict["MA"] += 1
			if x == "0":
				numDegrees_dict["None"] += 1

	return numDegrees_dict, numTitles, emailAdd, emailDomain

def main():
	degrees, titles, addresses, domains = readCsv("faculty.csv")

	print "\nQ1: How many degrees and their frequencies?"
	for key in degrees:
		print key, ":", degrees[key]

	print "\nQ2: How many different professions and their frequencies?"
	for key in titles:
		print key, ":", titles[key]

	print "\nQ3: Email address lists"
	for email in addresses:
		print email

	print "\nQ4: How many different email domains? List them."
	print len(domains), "types of domains (listed as below)"
	for key in domains:
		print key


if __name__ == "__main__":
	main()