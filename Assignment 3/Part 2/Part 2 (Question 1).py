labels = ["Name", "Age", "Course", "Is Attending"]
student_data = ["Tahir", 44, "AI and Data Science", True]

for label, item in zip(labels, student_data):
    print(f"{label}: {item}")
