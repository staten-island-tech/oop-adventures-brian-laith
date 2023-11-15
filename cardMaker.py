import json
import os
## Create Class for creating new dictionaries here

nameinput = input("Name: ")
gradeinput = input("Grade: ")
classinput = input("Class: ")
teacherinput = input("Teacher: ")
periodinput = input("Period: ")
averageinput = input("Class Average: ")
print("Thank you for your information, it is now publicly displayed in data.json")
class student:
    def __init__(self, name, grade, class1, teacher, period, average):
        self.name = name
        self.grade = grade
        self.class1 = class1
        self.teacher = teacher
        self.period = period
        self.average = average
    def create(self):
        data.append({'name': self.name, 'grade': self.grade, 'class': self.class1, 'teacher': self.teacher, 'period': self.period, 'class average': self.average})



with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    
    run = student(f"{nameinput}", f"{gradeinput}", f"{classinput}", f"{teacherinput}", f"{periodinput}", f"{averageinput}")
    run.create()






#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent=4)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")