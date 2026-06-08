students = {"25MCA001": 77, "25MCA009": 60, "25MCA025": 99,"25MCA007": 84, "25MCA012": 45, "25MCA021": 86,"25MCA032": 83, "25MCA018": 40, "25MCA014": 67}

print("Student IDs:", students.keys())
print("Student Grades: ", students.values())
print("Items: ", students.items())

maximum = max(students.values())
minimum = min(students.values())
print("Maximum:", maximum)
print("Minimum:", minimum)

dis_li, merit_li, avg_lis = [], [], []
distinct, merit, Pass, fail = 0, 0, 0, 0

for student_id, marks in students.items():
    if marks >= 86 and marks <= 100:
        distinct += 1
        dis_li.append(student_id)
    elif marks >= 76 and marks <= 85:
        merit += 1
        merit_li.append(student_id)
    elif marks >= 60 and marks <= 75:
        Pass += 1
    else:
        fail += 1

print(f"Distinction: {distinct} -> {dis_li}")
print(f"Merit: {merit} -> {merit_li}")
print("Pass count:", Pass)
print("Fail count:", fail)

len_dic = len(students)
class_avg = float(sum(students.values())//len_dic)
print("Class Average:", class_avg)

print("Below Average Students:")
for student_id, marks in students.items():
    if marks < class_avg:
        avg_lis.append(student_id)
print(avg_lis)

print("===== Leaderboard =====")
print(f"Distinction: {dis_li}")
