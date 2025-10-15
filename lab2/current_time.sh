#!/bin/bash

set -euo pipefail

current_time=$(date +%H:%M)
current_hour=$(date +%H)
current_minute=$(date +%M)
workday_end=18

echo "Current time: $current_time"

if (( current_hour >= workday_end )); then
    echo "Workday is over for today!"
else
    hours_left=$((workday_end - current_hour - 1))
    minutes_left=$((60 - current_minute))

    if (( minutes_left == 60 )); then
        minutes_left=0
        hours_left=$((hours_left + 1))
    fi

    echo "Time remaining until end of workday: $hours_left hours and $minutes_left minutes."
fi

