# Day format from two parameters

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
shortday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
char = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]

def FormatDay(day, format):
    day -= 1
    if format == "day":
        return days[day]
    elif format == "shortday":
        return shortday[day]
    elif format == "char":
        return char[day]
