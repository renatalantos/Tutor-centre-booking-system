from django.contrib import admin
from .models import Student, Booking


# Register your models here.

@admin.register(Student)    
class StudentAdmin(admin.ModelAdmin):

    list_display = ('student_name', 'student_email')
    list_filter = ('student_name', 'student_email') 


@admin.register(Booking)    
class BookingAdmin(admin.ModelAdmin):
    
    list_display = ('student', 'title')
    list_filter = ('student', 'title')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True) 