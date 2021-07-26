

# Function for Calculating Duration in hrs, min, second from time_difference
def time_difference_in_hours(difference):
    days, seconds = difference.days, difference.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours} hr {minutes} min"


def duration_in_days(seconds):
    time = seconds
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return "d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds)
