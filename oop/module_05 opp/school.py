
class Student:
    def __init__(self,name,current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class
        
    
    def __repr__(self) -> str:
        return f'student with name: {self.name},class: {self.current_class}, id: {self.id}'
    
class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject=subject
        self.id = id
    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}, id: {self.id}'

class school:
    def __init__(self,name) ->str:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers)+101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self, name, fee) ->str:
        if fee < 1000:
            print('not enough fee')
        else:
            id = len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee-1200}'
        
       
        
    def __repr__(self) -> str:
        print('welcome to',self.name)
        print('-------our teacher ---------')
        for teacher in self.teachers:
            print(teacher)
        
        print('------------welcome our student-----------------')
        for student in self.students:
            print(student)
        return 'All done for now'




"""alia = Student('ali takrim',9,1)
ali = Student('alia takrim',9,1)
sohag = Teacher('fokir bar0', 'Algorithm', 101)
print(ali)
print(sohag)"""

phitron = school('khadimpur')
phitron.enroll('alia',5200)
phitron.enroll('ali',100)
phitron.enroll('al',2000)

phitron.add_teacher('jhankor vai','data')
phitron.add_teacher('subhasish vai','data stucture')
phitron.add_teacher('mahfuz vai','databage')

print(phitron)





