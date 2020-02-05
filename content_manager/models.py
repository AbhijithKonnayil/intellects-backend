from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user_manager.models import User
from django.core.exceptions import ValidationError

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


class Course(models.Model):
    code = models.CharField(max_length=5, unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    credits = models.IntegerField(null=False, blank=False, validators=[
        MaxValueValidator(4),
        MinValueValidator(1)
    ])
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return '{}'.format(self.id)


class Module(models.Model):
    def validate_file(file):
        pass
    title = models.CharField(max_length=100, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)
    no = models.IntegerField(null=False, blank=False, validators=[
        MaxValueValidator(6),
        MinValueValidator(1)
    ])
    weightage = models.IntegerField(null=False, blank=False, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])
    notes = models.FileField(upload_to='notes',validators=[validate_file])
    def __str__(self):
        return '{}'.format(self.id)


class Topic(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    importance = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)


class VideoLecture(models.Model):
    def validate_image(file_obj):
        filesize = file_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    def clean(self, *args, **kwargs):
        print(self.thumbnail.width)
        if self.thumbnail.width>72: 
            raise ValidationError("Width exceeds by %s px" % str(self.thumbnail.width-72))
        if self.thumbnail.height>128:
            raise ValidationError("Height exceeds by %s px" % str(self.thumbnail.height-128))

    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    thumbnail = models.ImageField(upload_to='thumbnail',validators=[validate_image])
    src = models.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return '{}'.format(self.id)


class VideoComment(models.Model):
    video = models.ForeignKey(VideoLecture,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
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
    stream = models.CharField(max_length=10, choices=STREAM_CHOICE)
    link = models.CharField(max_length=500, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return '{}'.format(self.id)


class QuestionSoluntion(models.Model):
    QuestionPaper = models.OneToOneField(QuestionPaper,on_delete=models.CASCADE)
    video_link = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id)
