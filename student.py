class Student:
    student_id = '512'
    student_name = 'Sharon'

print("Original attributes and their values of the Student class:")
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

print("\nAfter adding the student_class, attributes and their values with the said class:")
Student.student_class  = 'Engineering'
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

print("\nAfter removing the student_name, attributes and their values from the said class:")
del Student.student_name
#delattr(Student, 'student_name')
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
