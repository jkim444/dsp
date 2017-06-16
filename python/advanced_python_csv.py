import csv
import advanced_python_regex

def main():
	degrees, titles, addresses, domains = advanced_python_regex.readCsv("faculty.csv")
	
	writeFile = open("emails.csv", 'w')
	for email in addresses:
		writeFile.write(email + "\n")

	writeFile.close()

if __name__ == "__main__":
	main()