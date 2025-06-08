import time
# This script implements a simple countdown timer that beeps when the time is up.
import winsound  # Windows-specific module

# Get the countdown time from the user

seconds = int(input("Enter countdown time in seconds: "))
print("Countdown starts now...")

while seconds > 0:
    print(f"{seconds} seconds remaining...")
    # Wait for 1 second
    # The time.sleep function is used to pause the program for a specified number of seconds.
    # This is necessary to create the countdown effect.
    # The countdown will print the remaining seconds every second.
    time.sleep(1)
    # Decrease the seconds by 1
    seconds -= 1
    
# When the countdown reaches zero, print a message and beep
print("Time's up!")
winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second