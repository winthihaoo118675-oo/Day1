scores = [55, 80, 35, 90, 65]

scores.append(75)
scores[1] = 85
print(scores)

print(max(scores))
print(min(scores))

print(sum(scores)/len(scores))

for score in scores:
    if(scores >=80):
        print(scores)
        
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")

average = sum(scores)/len(scores)
print(f"Average Scores: {average}")

for score in scores:
    if score >=80:
        print(f"Greater than 80 : {scores}")

