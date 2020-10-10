# readping

I developed this tool to troubleshoot a nagging problem that I was having with my Apple MacBook Pro 2017, currently running macOS Mojave 10.14.6. I was having regular ping related fails on video conferencing. Using this tool I was able to track it to consistently every 5 minutes, nearly to the second. I wasn't sure if it was just me or not until I was watching a webinar including Sir Jeremy Farrar -- mentioned in [this tweet](https://twitter.com/JeremyFarrar/status/1315034276874813446?s=20) and noticed that he was glitching every 5 minutes. After notifying his team that he should try a reboot, it worked. And on the next conference there was only a minor skip every five minutes, which is expected as indicated below.

Note: The problem does not appear to occur on a wired connection. I did try to reduce the HIGH_MULTIPLE variable to 1.5 to see if there was a smaller blip going on with a wired connection, but could not find a consistent pattern.

My end conclusion is that this is an Apple problem. 

## Overview

readping takes input from a ping stream, keeps track of the average ping time and then alerts when a ping time rises above a certain multiple of the average. After this alert is registered, readping will dump the preceding ping and then a minimum of 10 pings showing where the ping times rise above the multiple of the average.

Total number of ping alerts are announced at 10, 100, 500, and every 1000 pings.

### Observations

While pinging to google.com (or any other address for that matter) I will consistently see a small blip with an increased ping time every 5 minutes. After days of not rebooting my computer, this blip will become larger, eventually rising to multiple hundreds and eventually thousands of milliseconds, causing seriously problems on a video conference. After rebooting the machine, it goes back down to blip in line with the example given here.

Samples taken with `HIGH_MULTIPLE = 4`

google.com ping

```

mylaptop:readping me$ ./run_readping.sh 
PING google.com (172.217.9.206): 56 data bytes

============================================================
0 pings run - 0.0 ms average - 0 alerts
============================================================


============================================================
10 pings run - 17.9 ms average - 0 alerts
============================================================


============================================================
100 pings run - 16.5 ms average - 0 alerts
============================================================

============================================================
Alert 221 pings run -   47.5 ms - 10 Oct 2020 22:26:43
Alert 222 pings run -   97.3 ms - 10 Oct 2020 22:26:44
Alert 223 pings run -  149.2 ms - 10 Oct 2020 22:26:46
Alert 224 pings run -   16.2 ms - 10 Oct 2020 22:26:46
Alert 225 pings run -   12.6 ms - 10 Oct 2020 22:26:47
Alert 226 pings run -   13.0 ms - 10 Oct 2020 22:26:48
Alert 227 pings run -   13.1 ms - 10 Oct 2020 22:26:49
Alert 228 pings run -   18.6 ms - 10 Oct 2020 22:26:50
Alert 229 pings run -   19.3 ms - 10 Oct 2020 22:26:51
Alert 230 pings run -   18.7 ms - 10 Oct 2020 22:26:52
Alert 231 pings run -   21.1 ms - 10 Oct 2020 22:26:53
================ 2 Alerts - 17.0 ms average ================

     
============================================================
500 pings run - 16.2 ms average - 2 alerts
============================================================

============================================================
Alert 519 pings run -   14.8 ms - 10 Oct 2020 22:31:42
Alert 520 pings run -  104.4 ms - 10 Oct 2020 22:31:43
Alert 521 pings run -  148.5 ms - 10 Oct 2020 22:31:44
Alert 522 pings run -   35.6 ms - 10 Oct 2020 22:31:45
Alert 523 pings run -   86.9 ms - 10 Oct 2020 22:31:46
Alert 524 pings run -   15.0 ms - 10 Oct 2020 22:31:47
Alert 525 pings run -   17.6 ms - 10 Oct 2020 22:31:48
Alert 526 pings run -   17.3 ms - 10 Oct 2020 22:31:49
Alert 527 pings run -   14.0 ms - 10 Oct 2020 22:31:50
Alert 528 pings run -   16.2 ms - 10 Oct 2020 22:31:51
Alert 529 pings run -   16.4 ms - 10 Oct 2020 22:31:52
================ 5 Alerts - 16.7 ms average ================

    
```


ipchicken.com ping

```

wtcmbp:readping tate$ ping ipchicken.com | ./readping.py 
PING ipchicken.com (104.26.9.109): 56 data bytes

============================================================
0 pings run - 0.0 ms average - 0 alerts
============================================================


============================================================
10 pings run - 16.5 ms average - 0 alerts
============================================================

============================================================
Alert 94 pings run -   11.5 ms - 10 Oct 2020 22:36:42
Alert 95 pings run -  105.2 ms - 10 Oct 2020 22:36:43
Alert 96 pings run -   71.7 ms - 10 Oct 2020 22:36:44
Alert 97 pings run -  124.7 ms - 10 Oct 2020 22:36:45
Alert 98 pings run -   10.7 ms - 10 Oct 2020 22:36:46
Alert 99 pings run -   42.4 ms - 10 Oct 2020 22:36:47
Alert 100 pings run -   10.5 ms - 10 Oct 2020 22:36:48

============================================================
100 pings run - 18.1 ms average - 3 alerts
============================================================

Alert 101 pings run -   13.8 ms - 10 Oct 2020 22:36:49
Alert 102 pings run -   15.4 ms - 10 Oct 2020 22:36:50
Alert 103 pings run -   14.4 ms - 10 Oct 2020 22:36:51
Alert 104 pings run -   16.5 ms - 10 Oct 2020 22:36:52
================ 3 Alerts - 18.0 ms average ================

============================================================
Alert 394 pings run -   18.6 ms - 10 Oct 2020 22:41:43
Alert 395 pings run -  166.6 ms - 10 Oct 2020 22:41:44
Alert 396 pings run -  127.7 ms - 10 Oct 2020 22:41:45
Alert 397 pings run -   15.8 ms - 10 Oct 2020 22:41:46
Alert 398 pings run -   51.2 ms - 10 Oct 2020 22:41:47
Alert 399 pings run -   96.7 ms - 10 Oct 2020 22:41:48
Alert 400 pings run -   18.7 ms - 10 Oct 2020 22:41:49
Alert 401 pings run -   17.4 ms - 10 Oct 2020 22:41:50
Alert 402 pings run -   17.0 ms - 10 Oct 2020 22:41:51
Alert 403 pings run -   18.3 ms - 10 Oct 2020 22:41:52
Alert 404 pings run -   14.9 ms - 10 Oct 2020 22:41:53
================ 6 Alerts - 17.0 ms average ================

    
```


### system.log output

There do not seem to be any specific issues in the /var/log/system.log or /var/log/wifi.log

system.log

```

mylaptop:log me$ tail -n 500 system.log

....snip....

Oct 10 22:24:59 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0B000000-0000-0000-0000-000000000000[38732]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:00 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.05000000-0000-0000-0000-000000000000[38639]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:00 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.04000000-0000-0000-0000-000000000000[38741]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:02 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0F000000-0000-0000-0000-000000000000[38750]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:03 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.06000000-0000-0000-0000-000000000000[38742]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:06 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.01000000-0000-0000-0000-000000000000[38743]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:09 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.02000000-0000-0000-0000-000000000000[38744]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:12 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.03000000-0000-0000-0000-000000000000[38748]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:14 wtcmbp kcm[38760]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:25:34 wtcmbp kcm[38763]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:25:36 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.10000000-0000-0000-0000-000000000000[38756]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:43 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.10000000-0000-0000-0000-000000000000[38758]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:50 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0E000000-0000-0000-0000-000000000000[38749]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:25:54 wtcmbp kcm[38766]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:26:14 wtcmbp kcm[38769]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:26:34 wtcmbp kcm[38776]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:26:54 wtcmbp kcm[38781]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:26:54 wtcmbp syslogd[49]: ASL Sender Statistics
Oct 10 22:27:12 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.09000000-0000-0000-0000-000000000000[38755]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:27:14 wtcmbp kcm[38787]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:27:34 wtcmbp kcm[38791]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:27:38 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0C000000-0000-0000-0000-000000000000[38751]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:27:43 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.10000000-0000-0000-0000-000000000000[38785]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:27:54 wtcmbp kcm[38798]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:28:14 wtcmbp kcm[38801]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:28:21 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0F000000-0000-0000-0000-000000000000[38757]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:28:34 wtcmbp kcm[38804]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:28:37 wtcmbp login[38808]: USER_PROCESS: 38808 ttys001
Oct 10 22:28:37 wtcmbp com.apple.xpc.launchd[1] (com.ShareSync.AutoUpdater[38806]): Service exited with abnormal code: 1
Oct 10 22:28:54 wtcmbp kcm[38822]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:29:04 wtcmbp login[38824]: USER_PROCESS: 38824 ttys002
Oct 10 22:29:04 wtcmbp login[38824]: DEAD_PROCESS: 38824 ttys002
Oct 10 22:29:07 wtcmbp com.apple.xpc.launchd[1] (com.apple.imfoundation.IMRemoteURLConnectionAgent): Unknown key for integer: _DirtyJetsamMemoryLimit
Oct 10 22:29:12 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.10000000-0000-0000-0000-000000000000[38778]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:29:14 wtcmbp kcm[38837]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:29:34 wtcmbp kcm[38843]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:29:43 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.10000000-0000-0000-0000-000000000000[38834]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:29:54 wtcmbp kcm[38846]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:30:02 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0C000000-0000-0000-0000-000000000000[38796]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:30:14 wtcmbp kcm[38850]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:30:14 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0E000000-0000-0000-0000-000000000000[38784]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:30:33 wtcmbp kcm[38864]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:30:53 wtcmbp kcm[38869]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:31:13 wtcmbp kcm[38873]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:31:13 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.05000000-0000-0000-0000-000000000000[38373]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:31:14 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0F000000-0000-0000-0000-000000000000[38840]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:31:33 wtcmbp kcm[38878]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:31:43 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.10000000-0000-0000-0000-000000000000[38857]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:31:53 wtcmbp kcm[38886]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:32:02 wtcmbp com.apple.xpc.launchd[1] (com.apple.mdworker.shared.0E000000-0000-0000-0000-000000000000[38852]): Service exited due to SIGKILL | sent by mds[75]
Oct 10 22:32:13 wtcmbp kcm[38890]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
Oct 10 22:32:33 wtcmbp kcm[38897]: DEPRECATED USE in libdispatch client: Setting timer interval to 0 requests a 1ns timer, did you mean FOREVER (a one-shot timer)?; set a breakpoint on _dispatch_bug_deprecated to debug
```

And wifi.log

```
mylaptop:log me$ date
Sat Oct 10 22:40:59 BST 2020

mylaptop:log me$ tail -n 20 wifi.log

...snip...

Sat Oct 10 20:24:04.036 <kernel> ABCDEFGHI1VirtualInterface::controllerWillChangePowerState : Bringing down link
Sat Oct 10 20:24:04.064 <kernel> ABCDEFGHIVirtualInterface::handleSIOCSIFFLAGS : Source controllerWillChangePowerState calling peerManager->disable
Sat Oct 10 20:24:04.064 <kernel> wl0: wl_update_tcpkeep_seq: Original Seq: 4265376705, Ack: 2706457720, Win size: 2048
Sat Oct 10 20:24:04.064 <kernel> wl0: wl_update_tcpkeep_seq: Updated seq/ack/win from UserClient Seq 4265376705, Ack 2706457720, Win size 991
Sat Oct 10 20:24:04.064 <kernel> wl0: leaveModulePoweredForOffloads: Wi-Fi will stay on.
Sat Oct 10 20:24:04.064 <kernel> AirPort_ABCDEFGHI::platformWoWEnable: WWEN[enable], in_fatal_err[0]
Sat Oct 10 20:24:04.064 <kernel> AirPort_ABCDEFGHI::syncPowerState: WWEN[enabled]
Sat Oct 10 20:24:04.769 <airportd[172]> ERROR: rapportd (336) is not entitled for com.apple.wifi.join_history, will not allow request
Sat Oct 10 20:24:04.777 <airportd[172]> ERROR: sharingd (351) is not entitled for com.apple.wifi.join_history, will not allow request
Sat Oct 10 20:24:05.898 <kernel> AirPort_ABCDEFGHI::platformWoWEnable: WWEN[disable], in_fatal_err[0]
Sat Oct 10 20:24:09.935 <kernel> Setting BTCoex Config: enable_2G:1, profile_2g:0, enable_5G:1, profile_5G:0

```



