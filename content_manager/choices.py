SEMESTER_CHOICES = (('s1', 'Semester 1'),
                    ('s2', 'Semester 2'),
                    ('s3', 'Semester 3'),
                    ('s4', 'Semester 4'),
                    ('s5', 'Semester 5'),
                    ('s6', 'Semester 6'),
                    ('s7', 'Semester 7'),
                    ('s8', 'Semester 8'),
                    )
DEPARTMENT_CHOICES = (('cse', 'Computer Science & Engineering'),
                      ('ece', 'Electronics & Communication Engineering'),
                      ('eee', 'Electrical & Electronics Engineering'),
                      ('me', 'Mechanical Engineering'),
                      ('ce', 'Civil Engineering')
                      )

COLLEGE_CHOICES = (('nil', 'No College Selected'),
                   ('kte', 'Rajiv Gandhi Institute of Technology'),)


def college_list():

    return COLLEGE_CHOICES
