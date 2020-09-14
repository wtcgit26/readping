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

# adjustible variables
HIGH_MULTIPLE = 4
separator = "="
info_width = 60

# program variables preset
# this lines things up with the icmp_seq 
# TODO - I should update to actually use the icmp_seq instead of an iterative)
iterations = -2
pingtime = 0.0
cumsum = 0.0
average = 0.0
alert_num = 0
alert_total = 0
alert_active = False
alert_buffer = ""

for line in sys.stdin:
	line.rstrip()
	iterations += 1
	result = re.search(r"time\=[0-9]*\.[0-9]*", line)
	if result:
		x = result.group(0).split("=")
		if (iterations > 0):
			pingtime = float(x[1])
			cumsum += pingtime
			average = cumsum / iterations
		currtime = strftime("%d %b %Y %H:%M:%S", localtime())
		alert = "Alert {} pings run - {:6.1f} ms - {}".format(iterations, pingtime, currtime)
		if pingtime > HIGH_MULTIPLE * average:
			alert_num += 1
			alert_total += 1
			if(alert_num == 1):
				print(separator * info_width)
				print(alert_buffer)
			print(alert)
			alert_active = True
		elif alert_num < 10 and alert_num != 0:
			print(alert)
			alert_num += 1
			alert_active = True
		else:
			alert_num = 0
			alert_buffer = alert
			if alert_active:
				alert_print = " {} Alerts - {:.1f} ms average ".format(alert_total, average)
				alert_pad = info_width - len(alert_print)
				alert_left_pad = separator * int(alert_pad / 2)
				alert_right_pad = alert_left_pad
				if alert_pad % 2 != 0:
					alert_right_pad += separator
				print(alert_left_pad + alert_print + alert_right_pad)
				print("")
				alert_active = False
		if iterations % 1000 == 0 or iterations == 10 or iterations == 100 or iterations == 500 and iterations > 0:
			print("")
			print(separator * info_width)
			print ("{} pings run - {:.1f} ms average - {} alerts".format(iterations, average, alert_total))
			print(separator * info_width)
			print("")
	else:
		other_msg = re.search(r".*", line)
		if other_msg:
			print(other_msg.group(0))




