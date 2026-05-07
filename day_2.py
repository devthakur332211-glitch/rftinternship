def analyze_scores(marks):
    # 1. Basic Statistics
    avg_score = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    
    # 2. Count students above average
    # We use a list comprehension to filter scores > average
    above_avg_count = len([score for score in marks if score > avg_score])
    
    # Bonus: Grade Distribution
    # A: 90+, B: 80-89, C: 70-79, FAIL: <70
    distribution = {"A": 0, "B": 0, "C": 0, "FAIL": 0}
    
    for score in marks:
        if score >= 90:
            distribution["A"] += 1
        elif score >= 80:
            distribution["B"] += 1
        elif score >= 70:
            distribution["C"] += 1
        else:
            distribution["FAIL"] += 1
            
    return avg_score, highest, lowest, above_avg_count, distribution

# Given Data
MARKS = [78, 85, 90, 67, 85, 92, 78]

# Execute
avg, high, low, above_avg, grades = analyze_scores(MARKS)

# Display Insights
print(f"--- Student Score Analysis ---")
print(f"Average Score: {avg:.2f}")
print(f"Highest Score: {high}")
print(f"Lowest Score:  {low}")
print(f"Students Above Average: {above_avg}")
print(f"\n--- Grade Distribution ---")
for grade, count in grades.items():
    print(f"Grade {grade}: {count} students")
