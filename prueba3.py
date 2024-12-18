import os
import time


# Función para leer un archivo de texto
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

# Function to write to the text file
def write_file(file_path, students):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for student in students:
                subjects = ",".join([f"{s['name']}|{s['code']}|{s['grade']}|{s['credits']}"
                                     for s in student['subjects']])
                file.write(f"{student['code']},{student['name']},{subjects}\n")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

# Process the content in the file and convert it to a list of dictionaries
def process_content(lines):
    students = []
    
    for line in lines:
        data = line.strip().split(',')
        student_code = data[0].strip()
        student_name = data[1].strip()
        subjects = []
        i = 2
        while i < len(data):
            name, code, grade, credits = data[i].split('|')
            subjects.append({
                'name': name.strip(),
                'code': code.strip(),
                'grade': float(grade),
                'credits': int(credits)
            })
            i += 1
        students.append({'code': student_code, 'name': student_name, 'subjects': subjects})
    return students

# Function to calculate the weighted average
def calculate_average(subjects):
    weighted_sum = sum(s['grade'] * s['credits'] for s in subjects)
    total_credits = sum(s['credits'] for s in subjects)
    return round(weighted_sum / total_credits, 2) if total_credits > 0 else 0

# CRUD: Function to create a new student profile
def create_student(students):
    code = input("Enter the student code: ").strip()
    name = input("Enter the student name: ").strip()
    subjects = []
    
    while True:
        
        subject = input("""Enter subject
         (follow this format: Name|Code|Grade|Credits or 'end' to finish): """)
        
        if subject.lower() == 'end':
            break
        try:
            name_sub, code_sub, grade, credits = subject.split('|')
            subjects.append({
                'name': name_sub.strip(),
                'code': code_sub.strip(),
                'grade': float(grade),
                'credits': int(credits)
            })
        except ValueError:
            print("Error: Incorrect format, please try again.")
    students.append({'code': code, 'name': name, 'subjects': subjects})

# CRUD: Function to consult students in the text file
def consult_students(students):
    for student in students:
        print(f"\nCode: {student['code']}")
        print(f"Name: {student['name']}")
        for subject in student['subjects']:
            print(f"  - {subject['name']} ({subject['code']}): Grade {subject['grade']}, Credits {subject['credits']}")
        print(f"Weighted Average: {calculate_average(student['subjects'])}")

# CRUD: Function to update student profiles
def update_student(students):
    code = input("Enter the code of the student to update: ").strip()
    
    for student in students:
        
        if student['code'] == code:
            print("Student found. Update the data.")
            student['name'] = input("New student name: ").strip()
            student['subjects'] = []  # Reset subjects
            
            while True:
                subject = input("Enter subject (Name|Code|Grade|Credits or 'end' to finish): ")
                if subject.lower() == 'end':
                    break
                try:
                    name, code, grade, credits = subject.split('|')
                    student['subjects'].append({
                        'name': name.strip(),
                        'code': code.strip(),
                        'grade': float(grade),
                        'credits': int(credits)
                    })
                except ValueError:
                    print("Error.")
            return
    print("Student not found in the CRUD.")

# CRUD: Function to delete student profiles
def delete_student(students):
    code = input("Enter the code of the student to delete: ").strip()
    for i, student in enumerate(students):
        if student['code'] == code:
            students.pop(i)
            print("Student successfully deleted.")
            return
    print("Student not found.")

# Filter for highest average
def filter_highest_average(students):
    if not students:
        print("No students registered.")
        return
    top_student = max(students, key=lambda e: calculate_average(e['subjects']))
    print(f"Student with highest average: {top_student['name']} ({top_student['code']})")
    print(f"Weighted Average: {calculate_average(top_student['subjects'])}")

# The previous functions are used to support (auxiliary)
# the main function and thus shorten it
# Main function

def main():
    file_path = "not_ing_1.txt"
    students = []

    if os.path.exists(file_path):
        content = read_file(file_path)
        if content:
            students = process_content(content)

    while True:
        time.sleep(0.8)
        os.system("clear")
        print("\n--- Grade Management System ---")
        print("1. Register student")
        print("2. Consult information")
        print("3. Update student")
        print("4. Delete student")
        print("5. Filter student with highest average")
        print("6. Save and exit")
        option = input("Select an option: ")

        if option == '1':
            create_student(students)
        elif option == '2':
            consult_students(students)
        elif option == '3':
            update_student(students)
        elif option == '4':
            delete_student(students)
        elif option == '5':
            filter_highest_average(students)
        elif option == '6':
            write_file(file_path, students)
            print("Data saved. Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
