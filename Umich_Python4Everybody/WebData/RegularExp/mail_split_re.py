import re

hand = open("mbox-short.txt")

for line in hand:
	line = line.rstrip()
	# if re.search('^From:', line):
	if re.search('^F..m:.+@', line):
	# the "." represent one character, and ".+" represent all
	# the characters between ":" and "@" in the above expression
		print line + " " + str(len(line))
	# To avoid "greedy" search
	# See https://docs.python.org/2/howto/regex.html#greedy-versus-non-greedy
