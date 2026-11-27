"""Topic 42: logging instead of only printing."""


import logging


logging.basicConfig(
    filename="learning.log",
    level=logging.INFO,
    format="%(levelname)s:%(message)s",
)


def divide(total, people):
    logging.info("Trying to divide %s by %s", total, people)

    if people <= 0:
        logging.error("Invalid people count: %s", people)
        return None

    return total / people


share = divide(45, 3)

if share is not None:
    print(f"Each person pays ${share:.2f}")


logging.warning("This is a practice warning message.")

# Logging thinking:
# `print` is fine for learning and quick checks.
# `logging` is better when you want a record of what happened.
#
# Common levels:
# DEBUG: tiny details while developing
# INFO: normal events
# WARNING: suspicious but not broken
# ERROR: something failed

logging.info("Logging lesson completed.")

logging.info("Finished calculating the example bill")

logging.info("Example report is ready")

logging.info("Example values have been counted")

logging.info("Finished the small calculation example")

logging.info("Finished reviewing the example values")

logging.info("Example list processing is complete")

logging.info("Profile example has been prepared")
