student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇


def getGrade(num):
    match num:
        case num if num > 90:
            return "Outstanding"
        case num if num > 80:
            return "Exceeded Expectations"
        case num if num > 70:
            return "Acceptable"
        case num if num < 70:
            return "Fail"

def main():
	student_grade = map(lambda key:
						(key, getGrade(student_scores[key])), student_scores)
	for k,v in student_grade:
		student_grades[k] = v
main()


# 🚨 Don't change the code below 👇
print(student_grades)