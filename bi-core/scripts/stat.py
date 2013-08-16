import sys

token_map = dict() 
count = 0
for line in sys.stdin:
	count += 1
	num = len(line.split('\t'))
	if num in token_map:
		token_map[num] += 1
	else:
		token_map[num] = 1

print count
