from django.db import models


class SemesterPack(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount = models.DecimalField(max_digits=6,decimal_places=2)
    title = models.CharField(max_length=150)
    def __str__(self):
        return "{}".format(title)
    
class CoursePack(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount = models.DecimalField(max_digits=6,decimal_places=2)
    title = models.CharField(max_length=150)
    semester_pack = models.ForeignKey(SemesterPack,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return "{}".format(title)

class ModulePack(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount = models.DecimalField(max_digits=6,decimal_places=2)
    title = models.CharField(max_length=150)
    course_pack = models.ForeignKey(CoursePack,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return "{}".format(title)

class QuestionPack(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount = models.DecimalField(max_digits=6,decimal_places=2)
    title = models.CharField(max_length=150)
    course_pack = models.ForeignKey(CoursePack,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return "{}".format(title)
