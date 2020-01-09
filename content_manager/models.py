from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

SEMESTER_CHOICES = (('s1', 'Semester 1'),
                    ('s2', 'Semester 2'),
                    ('s3', 'Semester 3'),
                    ('s4', 'Semester 4'),
                    ('s5', 'Semester 5'),
                    ('s6', 'Semester 6'),
                    ('s7', 'Semester 7'),
                    ('s8', 'Semester 8'),
                    )


class Course(models.Model):
    code = models.CharField(max_length=5, unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    credits = models.IntegerField(null=False, blank=False, validators=[
        MaxValueValidator(4),
        MinValueValidator(1)
    ])
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)

    def __str__(self):
        return '{}'.format(self.id)


class Module(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL)
    no = models.IntegerField(null=False, blank=False, validators=[
        MaxValueValidator(6),
        MinValueValidator(1)
    ])
    weightage = models.IntegerField(null=False, blank=False, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])

    def __str__(self):
        return '{}'.format(self.id)


class Topic(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    importance = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)


class VideoLecture(models.Model):
    
    def __str__(self):
        return '{}'.format(self.id)


class VideoComment(models.Model):
    comment = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.id)


class QuestionPaper(models.Model):
    STREAM_CHOICE = (('regular', 'Regular'), ('supply', 'Supplymentry'))
    title = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False, validators=[
        MinValueValidator(2015)
    ])
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
    stream = models.CharField(max_lenght=10, choices=STREAM_CHOICE)
    link = models.CharField(max_length=500, null=False, blank=False)
    video_link = models.CharField(max_length=500, null=True, blank=True)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL)
    def __str__(self):
        return '{}'.format(self.id)


class QuestionSoluntion(models.Model):
    QuestionPaper = models.OneToOneField(QuestionPaper)
    def __str__(self):
        return '{}'.format(self.id)
