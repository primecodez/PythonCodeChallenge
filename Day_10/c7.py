#Using BOTH enumerate() and zip():

students = ["Aman", "Riya", "Kabir"]
marks = [85, 90, 88]

combined = zip(students, marks)

for i, (student, mark) in enumerate(combined, start=1):
    print(f"{i}. {student} scored {mark}")