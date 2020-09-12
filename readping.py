#! /usr/local/bin/python3
#
# Having problems with my wi-fi. I want to see when I am going to have
# trouble with my video calls but I don't want to have to monitor a continuous
# ping. I can run this command with stdin piped in from a `ping google.com` command
# for example
#
# Holds a buffer of the last ping so in case things go over HIGH_MULTIPLE
# the previous value prints. 10 pings return to show the trajectory. Another
# 10 will fire if the pings are still higher
#
#
#
import sys
import re
from time import localtime, gmtime, strftime

# this lines things up with the icmp_seq (todo - I should update to actually use the icmp_seq instead of an iterative)
iterations = -2
cumsum = 0
alert_num = 0
HIGH_MULTIPLE = 3
alert_buffer = ""

for line in sys.stdin:
	line.rstrip()
	iterations += 1
	result = re.search(r"time\=[0-9]*\.[0-9]*", line)
	if result:
		x = result.group(0).split("=")
		pingtime = float(x[1])
		cumsum += pingtime
		average = cumsum / iterations
		currtime = strftime("%a, %d %b %Y %H:%M:%S", localtime())
		alert = "Alert @ {} pings run -- {:8.2f} -- {:6.1f} average -- {}".format(iterations, pingtime, average, currtime)
		if pingtime > HIGH_MULTIPLE * average:
			alert_num += 1
			if(alert_num == 1):
				print("===================================")
				print(alert_buffer)
			print(alert)
		elif alert_num < 10 and alert_num != 0:
			print(alert)
			alert_num += 1
		else:
			alert_num = 0
			alert_buffer = alert
		if iterations % 1000 == 0 or iterations == 10 or iterations == 100 or iterations == 500:
			print ("{} pings run".format(iterations))
	else:
		other_msg = re.search(r".*", line)
		if other_msg:
			print(other_msg.group(0))




