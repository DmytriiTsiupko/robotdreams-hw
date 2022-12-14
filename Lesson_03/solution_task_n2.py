# 2. Create a program that will print “I love Python” to the console every 4.2 seconds until its execution is manually
# interrupted.

import time


while True:

    time_out = time.sleep(4.2)
    print("I love Python")