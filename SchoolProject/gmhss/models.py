from django.db import models

# Create your models here.
class Student(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    class_std = models.CharField(max_length=20,verbose_name='class')
    ad_no = models.IntegerField(verbose_name='Admission Number')
    place = models.CharField(max_length=50)
    phone = models.IntegerField()

class Teacher(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField() 