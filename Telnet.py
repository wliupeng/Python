#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Liupeng's Python Shell
# Network device Xunjian
import telnetlib,time
tn = telnetlib.Telnet('1.1.1.1',23)
tn.write(b'admin\n')
time.sleep(0.1)
tn.write(b'sythq1219114\n')
time.sleep(0.1)
tn.write(b'display ip interface brief\n')
time.sleep(0.1)
tn.write(b' ')
time.sleep(0.1)
xs = (tn.read_very_eager()).decode('utf8')
print(xs)
