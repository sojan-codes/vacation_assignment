marks = [78, 45, 92, 66, 91, 59]
ref = marks[0]

for i in marks:
    if i > ref:
        ref = i
marks.remove(ref)
second_ref = marks[0]
for i in marks:
    if i > second_ref:
        second_ref = i

print(second_ref)
    