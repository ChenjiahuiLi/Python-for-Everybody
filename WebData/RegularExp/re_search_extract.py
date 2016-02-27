import re

hand = open('mbox-short.txt')

for line in hand:
	line = line.rstrip()

	#if re.search('^X-.*: [0-9.]+', line):
		#print line
	#X-DSPAM-Confidence: 0.8475
	#X-DSPAM-Probability: 0.0000
	#X-DSPAM-Confidence: 0.6178
	#X-DSPAM-Probability: 0.0000

	#if re.search('^X-.*Confidence: [0-9.]+', line):
		#print line
	# X-DSPAM-Confidence: 0.8475
	# X-DSPAM-Confidence: 0.6178
	# X-DSPAM-Confidence: 0.6961

	# Only extract the float numbers in these lines
	lst = re.findall('^X\S*: ([0-9.]+)', line)
	#if len(lst)>0: print lst

	#lst2 = re.findall('^Details:.*rev=([0-9.]+)',line) # float & int
	lst2 = re.findall('^Details:.*rev=([0-9]+)',line) # only int
	# if len(lst2)>0: print lst2

	#lst3 = re.findall('^From .* ([0-9][0-9]):',line) # the hour
	lst3 = re.findall('From .* [0-9][0-9]:([0-9][0-9]):', line) # the minute
	#if len(lst3)>0: print lst3

x = 'We just recieved $10.00 for cookied'
y = re.findall('\$[0-9.]+',x)
print y
