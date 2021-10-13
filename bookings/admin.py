from django.contrib import admin
from .models import Student, Booking

# Register your models here.

admin.site.register(Booking)
#admin.site.register(Slot)
admin.site.register(Student)