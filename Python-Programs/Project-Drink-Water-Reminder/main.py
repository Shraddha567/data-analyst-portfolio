# import time
# from plyer import notification

# def water_reminder():
#     while True:
#         notification.notify(
#             title="Water Reminder",
#             message="Time to sip some water!",
#             timeout=10
#         )
#         time.sleep(3600)  # remind every hour
#         # time.sleep(3)   # for testing purposes, remind after every 3 seconds

# water_reminder()

"""
NOTE:
The Above  code may NOT work on macOS because the 'plyer' library
does not have a stable notification backend for macOS.
It works reliably on Windows, but macOS requires a native
solution like 'osascript' for notifications.
"""

import time
import os

def water_reminder():
    try:
        while True:
            os.system("""
            osascript -e 'display notification "Time to sip some water!" with title "Water Reminder"'
            """)
            time.sleep(3600)
    except KeyboardInterrupt:
        print("Water reminder stopped by user.")

water_reminder()

