# The football.csv file contains the results from the English Premier League. 
# The columns labeled "Goals" and "Goals Allowed" contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in "for" and "against" goals.

import csv

def read_data(filename):
	file = open(filename, 'r')

	dataList = []
	temp = []
	team = []
	games = []
	wins = []
	loss = []
	draws = []
	goal_for = []
	goal_against = []
	points = []

	goal_diff = {}

	reader = csv.reader(file, delimiter=',')
	for row in reader:
		team.append(row[0])
		games.append(row[1])
		wins.append(row[2])
		loss.append(row[3])
		draws.append(row[4])
		goal_for.append(row[5])
		goal_against.append(row[6])
		points.append(row[7])

	dataList = [team, games, wins, loss, draws, goal_for, goal_against, points]
	
	return dataList

def get_index(goals):
	def get_diff(goal_for, goal_against):
		if goal_for >= goal_against:
			return int(goal_for) - int(goal_against)
		else:
			return int(goal_against) - int(goal_for)
    
	temp = []
	temp.append('Score Diff')
	for x in range(1, len(goals[0])):
		temp.append(get_diff(goals[5][x], goals[6][x]))

	return temp.index(min(temp[1:]))

def get_team(index, parsed):
	return parsed[0][index]


def main():
	footballTable = read_data('football.csv')
	minRow = get_index(footballTable)
	print(str(get_team(minRow, footballTable)))

if __name__ == '__main__':
	main()