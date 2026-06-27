"""Topic 34: dates, times, and timedeltas."""


from datetime import date, datetime, timedelta


today = date.today()
next_week = today + timedelta(days=7)

print(f"Today: {today}")
print(f"Next week: {next_week}")


deadline = datetime(2026, 7, 15, 17, 0)
now = datetime.now()
time_left = deadline - now

# Date/time thinking:
# `date` is for calendar days.
# `datetime` is for calendar day + clock time.
# `timedelta` is a duration, like 7 days or 3 hours.
print(f"Deadline: {deadline}")
print(f"Days left: {time_left.days}")


def is_overdue(due_date: date) -> bool:
    return date.today() > due_date


print(f"Is yesterday overdue? {is_overdue(today - timedelta(days=1))}")

# Dates are useful for deadlines, logs, reports, reminders, and filtering data.
