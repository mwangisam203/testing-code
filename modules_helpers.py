"""Helper functions for the modules_imports lesson."""


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def format_money(amount):
    return f"${amount:.2f}"
