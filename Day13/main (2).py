print("Exam Grade Caculator")
exam_name = input("Enter exam name: ")
Max_score = float(input("Max Possible Score: "))
Score = float(input("Your Score: "))
percentage = round((Score/Max_score)*100,2)
if percentage >= 90:
  grade = "A+"
elif percentage >= 80:
  grade = "A"
elif percentage >= 70:
  grade = "B"
elif percentage >= 60:
  grade = "C"
elif percentage >= 50:
  grade = "D"
else:
  grade = "U"
print("You got", percentage, "% which is a",grade)

