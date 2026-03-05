# Filter students who passed (marks ≥ 40).
#
# Use map to extract their names.
#
# Use reduce to calculate the total marks.
#
# Use zip to pair names with marks.
#
# Use sorted to rank students by marks.
from functools import reduce
students=[
    {"name":"sasi","mark":90},
    {"name":"raj","mark":94},
    {"name":"vimal","mark":40},
    {"name":"prabu","mark":10},
    {"name":"ram","mark":100},
    {"name":"gopal","mark":80},
    {"name":"salmon","mark":39},
    {"name":"vikram","mark":30},
    {"name":"kumar","mark":50},
]

passed_student=list(filter(lambda x:x["mark"]>=40 ,students))
print(passed_student)

pass_students_names=list(map(lambda x: x["name"],passed_student))
print(pass_students_names)

total_marks=reduce(lambda x,y:x+y["mark"],students,0)
print(total_marks)

names=[x["name"] for x in students]
print(names)

marks=[x["mark"] for x in students]
print(marks)

names_and_marks=list(zip(names,marks))
print(names_and_marks)

rank=sorted(students,key=lambda x: x["mark"],reverse=True)
print(rank)

