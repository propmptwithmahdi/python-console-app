# school.py

import json

student_file = "students.json"
teacher_file = "teachers.json"

def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def add_student(students):
    name = input("👦 Enter student name: ")
    age = input("🎂 Enter age: ")
    grade = input("🏫 Enter grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print("✅ Student added.")

def add_teacher(teachers):
    name = input("👩‍🏫 Enter teacher name: ")
    subject = input("📚 Enter subject: ")
    teacher = {"name": name, "subject": subject}
    teachers.append(teacher)
    print("✅ Teacher added.")

def view_students(students):
    if not students:
        print("❌ No students found.")
    else:
        print("\n📋 Student List:")
        for i, s in enumerate(students, 1):
            print(f"{i}. {s['name']} | Age: {s['age']} | Grade: {s['grade']}")

def view_teachers(teachers):
    if not teachers:
        print("❌ No teachers found.")
    else:
        print("\n📋 Teacher List:")
        for i, t in enumerate(teachers, 1):
            print(f"{i}. {t['name']} | Subject: {t['subject']}")

def search_person(people, role):
    name = input(f"🔍 Enter {role} Id to search: ").lower()
    for p in people:
        if p["name"].lower() == name:
            print(f"✅ Found: {p}")
            return
    print(f"❌ {role.capitalize()} not found.")

def main():
    students = load_data(student_file)
    teachers = load_data(teacher_file)

    while True:
        print("\n--- SCHOOL SYSTEM MENU ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. View Students")
        print("4. View Teachers")
        print("5. Search Student")
        print("6. Search Teacher")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            add_teacher(teachers)
        elif choice == "3":
            view_students(students)
        elif choice == "4":
            view_teachers(teachers)
        elif choice == "5":
            search_person(students, "student")
        elif choice == "6":
            search_person(teachers, "teacher")
        elif choice == "7":
            save_data(students, student_file)
            save_data(teachers, teacher_file)
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()