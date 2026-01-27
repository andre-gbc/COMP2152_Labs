print("="*50)
print("Question 1: Student Grade List")
print("="*50)

grades = [85,97,53,67,78]
grades.append(90)
grades.sort()

print("Sorted Grades:", grades)
print("Highest Grade:", grades[-1])
print("Lowest Grade:", grades[0])
print("Total Number of Grades:", len(grades))