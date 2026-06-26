"""Topic 20: while loops and control flags."""


energy = 3

# While-loop thinking:
# Use a `while` loop when you do not know the exact number of repeats upfront.
# The loop continues as long as the condition stays True.
while energy > 0:
    print(f"Keep practicing. Energy left: {energy}")

    # This line is important.
    # Without changing `energy`, the condition would stay True forever.
    energy -= 1

print("Take a break.")


password = "python123"
guess = "python123"
is_logged_in = False

# A flag is a boolean variable that remembers whether something happened.
# Here, `is_logged_in` starts False and changes only after a correct password.
if guess == password:
    is_logged_in = True

if is_logged_in:
    print("Welcome back!")

# Common while-loop checklist:
# 1. What condition keeps the loop running?
# 2. What changes inside the loop?
# 3. What stops the loop?
