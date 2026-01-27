print("="*50)
print("Question 4")
print("="*50)

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")

print("Monday Class", monday_class)
print("Wednesday Class", wednesday_class)

both_classes = monday_class & wednesday_class
print("Attended both classes:", both_classes)

all_students = monday_class | wednesday_class
print("Attended either: ", all_students)

only_monday = monday_class - wednesday_class
print("Only attended Monday class:", only_monday)

only_one = monday_class ^ wednesday_class
print("Attended only one class:", only_one)
print("Is Monday subset of alll students?", monday_class <= all_students)

