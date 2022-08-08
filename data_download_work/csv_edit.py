#!/bin/python3
import csv

loto6_all_cols = {
	'number' : 0,
	'date'   : 1,
	'ball_1' : 2,
	'ball_2' : 3,
	'ball_3' : 4,
	'ball_4' : 5,
	'ball_5' : 6,
	'ball_6' : 7,
	'ball_b' : 8
}

loto6_jnb_cols = {
	'date'   : 1,
	'ball_1' : 3,
	'ball_2' : 4,
	'ball_3' : 5,
	'ball_4' : 6,
	'ball_5' : 7,
	'ball_6' : 8,
	'ball_b' : 9
}

loto7_all_cols = {
	'number' : 0,
	'date'   : 1,
	'ball_1' : 2,
	'ball_2' : 3,
	'ball_3' : 4,
	'ball_4' : 5,
	'ball_5' : 6,
	'ball_6' : 7,
	'ball_7' : 8,
	'ball_b1': 9,
	'ball_b2': 10
}

loto7_jnb_cols = {
	'date'   : 1,
	'ball_1' : 3,
	'ball_2' : 4,
	'ball_3' : 5,
	'ball_4' : 6,
	'ball_5' : 7,
	'ball_6' : 8,
	'ball_7' : 9,
	'ball_b1': 10,
	'ball_b2': 11
}

def csv_output(output_file, input_file, column_dict):
	with open(output_file, 'w') as o:
		writer = csv.writer(o)
		csv_input(writer, input_file, column_dict)

def csv_output2(output_file, input_file, column_dict):
	with open(output_file, 'a') as o:
		writer = csv.writer(o)
		csv_input2(writer, input_file, column_dict)

def csv_input(writer, input_file, column_dict):
	c = 0
	with open(input_file) as i:
		reader = csv.reader(i)
		for row in reader:
			c += 1
			orec = []
			if 1 == c:
				continue

			for key in column_dict:
				orec.append(row[column_dict[key]])
			writer.writerow(orec)

def csv_input2(writer, input_file, column_dict):
	c = 0
	with open('loto6jnb.csv', encoding='sjis') as i:
		reader = csv.reader(i)
		for row in reader:
			c += 1
			orec = []
			if 1 == c:
				continue

			orec.append(row[0].replace('第', '').replace('回', ''))
			for key in column_dict:
				orec.append(row[column_dict[key]])
			writer.writerow(orec)

csv_output('../mysql/loto6.csv', 'LOTO6_ALL.csv', loto6_all_cols)
# csv_output2('../mysql/loto6.csv', 'loto6jnb.csv', loto6_jnb_cols)
csv_output('../mysql/loto7.csv', 'LOTO7_ALL.csv', loto7_all_cols)
# csv_output2('../mysql/loto7.csv', 'loto7jnb.csv', loto7_jnb_cols)

