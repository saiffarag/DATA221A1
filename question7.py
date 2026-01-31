def convert_seconds(total_seconds):
    if total_seconds < 0 or total_seconds >= 86400: # Validate input range (0 to 86399 seconds)
        print("Invalid input: Time cannot be negative and time cannot exceed one full day from midnight")
        return

    hours24 = total_seconds // 3600 # Convert total seconds into 24-hour format components
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60

    if hours24 == 0: # Convert 24-hour time to 12-hour format with AM/PM
        hours12 = 12
        period = "AM"
    elif hours24 < 12:
        hours12 = hours24
        period = "AM"
    elif hours24 == 12:
        hours12 = 12
        period = "PM"
    else:
        hours12 = hours24 - 12
        period = "PM"

    print(f"{hours12}:{minutes:02d}:{seconds:02d} {period}") # Print formatted time

convert_seconds(0)
# 12:00:00 AM

convert_seconds(3661)
# 1:01:01 AM

convert_seconds(43200)
# 12:00:00 PM

convert_seconds(86399)
# 11:59:59 PM

convert_seconds(90000)
# Invalid input