import pandas

students_scores = {
    "students": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "scores": [85, 92, 78, 88, 95, 81, 90]
}

data_frame = pandas.DataFrame(students_scores)
print(data_frame)
data_frame.to_csv("test_output.csv")