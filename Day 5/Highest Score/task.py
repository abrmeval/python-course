student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#Built in function to sum all the numbers
total_exam_score= sum(student_scores)
print(total_exam_score)

total_exam_score = 0
for score in student_scores:
    total_exam_score+= score

print(total_exam_score)
print(range(1, 10))

#Built in function to get the max number of a collection
max(student_scores)

max_number = 0
for score in student_scores:
   if score > max_number:
       max_number = score

print(max_number)
