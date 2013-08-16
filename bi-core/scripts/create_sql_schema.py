import sys

# create the schema for in form of SQL

def create_table_schema(filepath, table_name):
	""" 
	filepath - the path of the csv file
	table_name - the name of the table
	"""
	stmt = "CREATE TABLE " + table_name + "("

	with open(filepath) as file:
		lines = file.readlines()
		for line in lines[:-1]:
			tokens = line.split('\t')
			stmt += tokens[0] 
			if len(tokens) >= 3:
				stmt += " " + tokens[2] + "\n"
			else:
				stmt += " varchar(64)\n"
		last_line = lines[-1]
		tokens = last_line.split('\t')
		if len(tokens) >= 3:
			stmt += " " + tokens[2]+ "\n"
		else:
			stmt += " varchar(64)\n"

	stmt += ") ENGINE=InnoDB DEFAULT CHARSET=utf8\n";
	print stmt

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "\tYou input %d parameters" % len(sys.argv)
		print "\tusage: create_schema filepath table_name\n"
	else:
		create_table_schema(sys.argv[1], sys.argv[2])
