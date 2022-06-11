def seconds_to_minutes(seconds):
    minute = seconds / 60.0
    return minute

def minutes_to_hours(minutes):
    hours = minutes / 60.0
    return hours

def seconds_to_hour(seconds):
    hour  = seconds / 3600.0
    return hour

print(seconds_to_minutes(120))
print(minutes_to_hours(120))
print(seconds_to_hour(7200))

