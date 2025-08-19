scores_list = [40, 89, 90, 89, 23, 90, 50]

# Get unique scores and sort them in descending order
unique_scores = sorted(set(scores_list), reverse=True)

first_best = unique_scores[0]       # highest score
second_best = unique_scores[1]      # second highest score

print("First best score:", first_best)
print("Second best score:", second_best)
