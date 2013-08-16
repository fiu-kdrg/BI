import sys

def create_table_schema(filepath, table_name):
	stmt = "CREATE TABLE " + table_name + "("

	with open(filepath) as file:
		lines = file.readlines()
		for line in lines:
			stmt += line.split('\t')[0] + " STRING,\n"	

	stmt += ")\n" + "ROW FORMAT DELIMITED FIELDS TERMINATED BY '9' LINES TERMINATED BY '10'\n" + "STORED AS TEXTFILE"
	print stmt

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "\tYou input %d parameters" % len(sys.argv)
		print "\tusage: create_schema filepath table_name\n"
	else:
		create_table_schema(sys.argv[1], sys.argv[2])

