grades = [[100, 99, 98, 99, 100],
			[95, 0, 85, 0, 70],
			[90, 91, 95, 97, 99]]


def print_board(board):

	print("------------------")
	for row in grades:
		output = "|"
		for item in row:
			if item == "True":
				output += str(item) + ' |'
			else:
				output += str(item) + '|'
		print(output)
		
		print("------------------")
					
def average_grades_rows():
	
	row1 = grades[0][0] + grades[0][1] + grades[0][2] + grades[0][3] + grades[0][4]
	row2 = grades[1][0] + grades[1][1] + grades[1][2] + grades[1][3] + grades[1][4]
	row3 = grades[2][0] + grades[2][1] + grades[2][2] + grades[2][3] + grades[2][4]
	lenRow1 = len(grades[0])
	lenRow2 = len(grades[1])
	lenRow3 = len(grades[2])
	averageRow1 = row1 / lenRow1
	averageRow2 = row2 / lenRow2
	averageRow3 = row3 / lenRow3
	averageList = row1 / lenRow1 + row2 / lenRow2 + row3 / lenRow3
			
	return (averageRow1, averageRow2, averageRow3, averageList)
	
print_board(grades)
print("The average for the numbers in the each row is and the last one is the average for the whole list: {}" .format(average_grades_rows()))



