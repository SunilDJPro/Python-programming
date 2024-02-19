class Student:
    def __init__(self, name, roll_num, dept, sem):
        self.name = name
        self.roll_num = roll_num
        self.dept = dept
        self.sem = sem
        self.next = None
        

class StudentPortal:
    
    def __init__(self):
        self.head = None
        
    def add_student(self, name, roll, dept, sem):
        new_student = Student(name, roll, dept, sem)
        if not self.head:
            self.head = new_student
        else:
            current_student = self.head
            while current_student.next:
                current_student = current_student.next
            current_student.next = new_student
            
    
    def display_students(self):
        current_student = self.head
        while current_student:
            print(f"Name: {current_student.name}")
            print(f"Roll Number: {current_student.roll_num}")
            print(f"Department: {current_student.dept}")
            print(f"Semester: {current_student.sem}")
            print("--------------------------------------")
            current_student = current_student.next
            

if __name__ == "__main__":
    portal = StudentPortal()
    
    portal.add_student("Sunil", "6002", "Computer Science and Electronics", "1st")
    portal.add_student("ksheeraja", "7002", "Electrical Engineering", "2nd")
    portal.add_student("Jhanvi", "6003", "Computer Science", "2nd")
    portal.add_student("Sidharth", "6001", "Computer Science and Electronics", "1st")
    
    
    portal.display_students()
            