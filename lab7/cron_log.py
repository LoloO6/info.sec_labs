#!/usr/bin/env python3
import datetime

with open(r"C:\Users\user\info.sec_labs\lab7\cron_log.txt", "a") as f:
    f.write(f"Log entry at {datetime.datetime.now()}\n")
