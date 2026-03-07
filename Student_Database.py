def Management(n):
    Database = {}

    for i in range(1, n + 1):
        student = input("Enter the Name of the Student: ")
        marks = int(input("Enter the Marks of the Student: "))
        Database[student] = marks
    
    average = sum(Database.values()) / n
    print(f"Average Marks of the Students: {average}")

    return Database

def Search(Database, name):
    if name in Database:
        print(f"{name} has Scored {Database[name]}")
    else:
        print(f"{name} is not a Student in the Database")

def Update(Database, student, marks_old, marks_new):
    if student in Database:
        if Database[student] == marks_old:
            Database[student] = marks_new
            print(f"{student}'s marks have been updated to {marks_new}")
        elif Database[student] == marks_new:
            print(f"{student} already has the new marks {marks_new}. No update needed.")
        else:
            print(f"Update failed for {student}.")
    else:
        print(f"{student} is not a Student in the Database. Update failed.")

    return Database


n = int(input("Enter the number of students: "))

student_database = Management(n)
print(f"Student Database:\t{student_database}")


name = input("Enter the name of the student to search: ")

Search(student_database, name)


student = input("Enter the name of the student whose marks you want to update: ")
marks_old, marks_new = map(int, input("Enter the old marks and new marks separated by space: ").split())

student_updated_database = Update(student_database, student, marks_old, marks_new)
print(f"Updated Student Database:\t{student_updated_database}")

from binascii import Error
import json

try:
    with open("student_database.json", "w") as file:
        for i in student_updated_database:
            json.dump({i: student_updated_database[i]}, file)
            file.write("\n")
except Error as e:
    print(f"Error saving student database to file: {e}")

