"""Topic 16: combining sequences with zip."""


names = ["Ava", "Noah", "Mia"]
scores = [91, 84, 96]

# Step 1: Both lists store related data in matching positions.
# Step 2: zip creates pairs: ("Ava", 91), ("Noah", 84), and so on.
# Step 3: the loop unpacks one pair into `name` and `score` each time.
for name, score in zip(names, scores):
    # Step 4: the f-string displays the two values from the current pair.
    print(f"{name} scored {score}")

# Important: zip stops when the shortest sequence runs out of items.

score_lookup = dict(zip(names, scores))
print(f"Score lookup: {score_lookup}")

name_score_pairs = list(zip(names, scores))
print(f"Name and score pairs: {name_score_pairs}")

total_scores = sum(score for name, score in zip(names, scores))
print(f"Combined scores: {total_scores}")

best_pair = max(zip(names, scores), key=lambda pair: pair[1])
print(f"Best score pair: {best_pair}")

print(f"Number of score pairs: {len(list(zip(names, scores)))}")

score_gaps = [abs(first - second) for first, second in zip(scores, reversed(scores))]
print(f"Score gaps: {score_gaps}")

last_score_pair = list(zip(names, scores))[-1]
print(f"Last name and score: {last_score_pair}")
