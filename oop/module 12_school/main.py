from School import School, ClassRoom, Subject
from Persons import Student,Teacher
def main():
    school = School('adam jee', 'uttara')

    eight = ClassRoom('eight')
    school.add_classroom(eight)

    nine = ClassRoom('nine')
    school.add_classroom(nine)

    ten = ClassRoom('ten')
    school.add_classroom(ten)

    abul = Student('abir khan', eight)
    school.student_admission(abul)

    hasan = Student('hasan khan', eight)
    school.student_admission(hasan)

    shohel = Student('shohel khan', eight)
    school.student_admission(shohel)
    
    
    physics_teacher = Teacher('shahjahan tapon rana')
    physics = Subject('physics', physics_teacher)
    eight.add_Subject(physics)


    chemistry_teacher = Teacher('hardon nag')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_Subject(chemistry)

    Biology_teacher = Teacher('Gazy ajmal')
    Biology = Subject('Biology', Biology_teacher)
    eight.add_Subject(Biology)

    eight.take_semester_final()



    print(school)


if __name__ == '__main__':
    main()