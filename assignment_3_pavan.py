class Student:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
    def display_id(self):
        print('Name of the student:',self.Name)
        print("Student's age:",self.Age)
    def student_marks_percentage(self,sub1,sub2,sub3,sub4,sub5):
        print('Student Name:',self.Name)
        try:
            percentage=(sub1+sub2+sub3+sub4+sub5)/5
            print('Percentage of the Student is:',percentage)
        except TypeError as e:
            print('error',e)
    def course(self,course_name):
        print('Name of the student:',self.Name)
        try:
            match course_name:
                case 'java':
                    print('The selected course is java')
                case 'python':
                    print('The selected course is python')
                case 'ruby':
                    print('The selected course is ruby')
                case 'r':
                    print('The selected course is r')
                case _:
                    print('The course is not available')
        except TypeError as e:
            print('error',e)
    
        
    def alldetails(*args,**kwargs):
        print('The arguments are')
        for i in args:
            print(i,end=' ')
        print()
        print('The key values')
        for j , k in kwargs.items():
            print(j , k)
                       
object=Student('Pavan',20)
object.display_id()
print()
object.student_marks_percentage(89,60,75,75,55)
print()
object.course('java')
print()
object.student_marks_percentage('java',45,34,34,45)
print()
object.course('ai')
print()
object.alldetails('pavan','cse',course='python',gpa=9.0)
print()
object.course(32)

    