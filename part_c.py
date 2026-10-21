# C1
foods = ["sel roti", "masu", "chiura", "achar"]
foods.append("dahi")
foods.insert(1, "bara")
foods.remove("achar")
print(foods)
print("Length: ", len(foods))

# C2
marks = [78, 45, 92, 66, 88, 59]
highest = marks[0]
lowest = marks[0]
total = 0
for i in marks:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total += i

avg = total / len(marks)
print(highest, lowest)
print("Total :", total,"\nAverage :", avg)

print("Highest:", max(marks))
print("Lowest:", min(marks))
marks.sort()
print("ascending :", marks)
marks.reverse()
print("descending : ", marks)

# C3
dashain_days = ("Ghatasthapana", "Fulpati", "Maha Ashtami", "Maha Navami", "Vijaya Dashami")
print("First Day:", dashain_days[0])
print("Last Day:", dashain_days[len(dashain_days) - 1])
print("Total number of Days:", len(dashain_days))
fulpati_exist = False
for i in dashain_days:
    if i == "Fulpati":
        fulpati_exist = True
if fulpati_exist:
    print("Yes, Fulpati exists in the Tuple.")
else:
    print("No, Fulpati Does not Exists in the Tuple.")
#Tuple is immutable so elements cannot be changed, added or removed once tuple is created.

# C4
ram_family = {"Hari", "Sita", "Gopal", "Maya"}
sita_family = {"Maya", "Bikash", "Hari", "Anju"}

print("Relatives in both families:", ram_family.intersection(sita_family))
print("All relatives:", ram_family.union(sita_family))
print("Only in ram_family:", (ram_family - sita_family))

# C5






