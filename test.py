

import time
run = raw_input("Start? > ")
mins = 1
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 5:
        print(""), mins
        # Sleep for a minute
        time.sleep(1)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
  