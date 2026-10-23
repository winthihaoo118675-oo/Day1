def greet():
    print('Hello from UCSPyay')
    
    
greet()

def greet(name):
    print(f"Hello, {name}!")
    
    
greet('Ma Ma')
greet('Ko Ko')

def calculate_average(scores):
    if len(scores) ==  0:
        return 0
    return sum(scores)/len(scores)
    
scores = [45, 70, 85]
result = calculate_average(scores)
print(f"The average score is:{result}")



def calculate_total(scores):
    return sum(scores)

def calculate_average(scores):
    if len(scores) ==  0:
        return 0
    return sum(scores)/len(scores)

def classify_score(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

def count_passed(scores):
    passed_scores = 0
    for score in scores:
        if score >=40:
            passed_scores +=1
    return passed_scores


scores = [45, 70, 85, 30, 90, 55]

result_total = calculate_total(scores)
result_grade = classify_score(90)
result_average = calculate_average(scores)
result_passed = count_passed( scores)

print(f"Total: {result_total}")
print(f"Average: {result_average}")
print(f"Grade: {result_grade}")
print(f"Passed Count: {result_passed}")