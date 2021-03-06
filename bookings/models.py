import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# STATUS = ((0, ""), (1, ""))


class Student(models.Model):
    student_name = models.CharField(max_length=15)
    student_email = models.EmailField(max_length=25, unique=True)
    

    def __str__(self):
        return self.student_name


# class Slot(models.Model):
#     SUBJECT_TITLE = (
#         ('BUS', 'BUSINESS'),
#         ('EN', 'ENGLISH'),
#         ('FR', 'FRENCH'),
#         ('GER', 'GERMAN'),
#         ('GEO', 'GEOGRAPHY'),
#         ('IR', 'IRISH'),
#         ('MAT', 'MATHS'), 
#         ('SPA', 'SPANISH'),
#     )
#     title = models.CharField(max_length=3, choices=SUBJECT_TITLE)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     duration = datetime.timedelta(hours=1)
#     number_of_students = models.IntegerField()
    
class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="tutored_student")
    # could User be Student here?
    # slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="booking_slot")
    booking_time = models.DateTimeField(auto_now_add=True)
    SUBJECT_TITLE = (
        ('BUS', 'BUSINESS'),
        ('EN', 'ENGLISH'),
        ('FR', 'FRENCH'),
        ('GER', 'GERMAN'),
        ('GEO', 'GEOGRAPHY'),
        ('IR', 'IRISH'),
        ('MAT', 'MATHS'), 
        ('SPA', 'SPANISH'),
    )
    title = models.CharField(max_length=3, choices=SUBJECT_TITLE, default='BUS')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = datetime.timedelta(hours=1)
    number_of_students = models.IntegerField(default=1)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    def __str__(self):
        return f'{self.student} has booked {self.title} between {self.start_date} and {self.end_date} for {self.number_of_students} student(s)'

    class Meta:
        ordering = ["booking_time"]    