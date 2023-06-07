class School:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address
        #composition beacuse of many class room
        self.Teachers = []
        self.classrooms = {}
        
    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.Teachers[subject] = teacher

    
    def student_admission(self,student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom as named {className}')
    
    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <=100:
            return 'A+'
        elif 70 <= marks <=79:
            return 'A'
        elif 60 <= marks <=69:
            return 'A'
        
        elif 50 <= marks <=59:
            return 'B'
        elif 40 <= marks <=49:
            return 'C'
        elif 33 <= marks <=39:
            return 'D'
        else: 
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):

        grade_map = {'A+':5.00,
                     'A':4.00,
                     'A-':3.50,
                     'B':3.00,
                     'C':2.00,
                     'D':1.00,
                     'F': 0.00
                     }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(grade):

       if 4.5<= grade<=5.00:
           return 'A+'
       elif 3.5<=grade<4.5:
           return 'A'
       elif 3.0<=grade<4.5:
           return 'A-'
       elif 2.5<=grade<3.5:
           return 'B'
       elif 2.00 <=grade< 2.5:
           return 'C'
       elif 1<= grade < 2:
           return 'D'
       else: 
           return 'F'
           





    def __repr__(self) -> str:
        print('--------All class room in the School--------------')
        for key,value in self.classrooms.items():
            print(key)
        
        print('----------students----------------')
        eight = self.classrooms['eight']
        print(len(eight.students))
        for stds in eight.students:
            print(stds.name,  stds.id)

        print('-----------------subjects--------------------')
        for subject in eight.subjects:
            print(subject.name, subject.teacher.name)
        
        print('--------------------student exam marks------------ ')

        """for key,value in eight.students[0].marks.items():
            print(key, value)"""
        for student in eight.students:
            for key, value in student.marks.items():
                print(student.name, key, value, student.subject_grade[key])
            print('________student end------------')

        
        return ''

class ClassRoom:
    def __init__(self,name) -> None:
        self.name = name 
        self.students = []
        self.subjects = []

    def add_student(self,student):
        serial_id = f'{self.name}-{len(self.students)}'
        student.id = serial_id
        self.students.append(student)

    def add_Subject(self,subject):
        self.subjects.append(subject)


    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

        for student in self.students:
            student.calculate_final_grade()


    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    def get_top_students(self):
        pass

class Subject:
    def __init__(self,name,teacher) -> None:
        self.name = name 
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam(student)
            student.marks[self.name]=mark
            student.subject_grade[self.name] = School.calculate_grade(mark)
        

        